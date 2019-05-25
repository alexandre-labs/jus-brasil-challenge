import asyncio
import re
import typing as t
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from jus_brasil.crawlers import utils
from jus_brasil.crawlers.models import QueryInput
from jus_brasil.crawlers.parsing import _simplify_process_data, parse_process


async def build_query_url(base_url: str, process_number: str) -> str:

    unif_year, jurisdiction = await utils._extract_unified_year_and_jurisdiction(
        process_number
    )

    return (
        f"{base_url}?conversationId=&paginaConsulta=1&"
        f"localPesquisa.cdLocal=-1&cbPesquisa=NUMPROC&"
        f"tipoNuProcesso=UNIFICADO&numeroDigitoAnoUnificado={unif_year}&"
        f"foroNumeroUnificado={jurisdiction}&dePesquisaNuUnificado={process_number}&"
        f"dePesquisa=&uuidCaptcha="
    )


async def is_query_result_a_process_list(query_result: str):
    # Searching by the div id related to all process' link
    return bool(re.search("listagemDeProcessos", query_result))


async def download_processes_pages(processes_urls: t.List[str]):

    processses_pages_tasks = asyncio.as_completed(
        [asyncio.create_task(utils.download_process_page(url)) for url in processes_urls]
    )

    for process_page in processses_pages_tasks:
        yield await process_page


async def _extract_processes_urls(base_url: str, processes_list_page: str) -> t.List[str]:

    _soup = BeautifulSoup(processes_list_page)
    return [urljoin(base_url, a.get("href")) for a in _soup.select(".linkProcesso")]


async def _extract_process_details(process_data: str) -> t.Dict[str, str]:

    process_details_regex = (
        r"Classe:(?P<class>.+(?=Área\s+))"
        r"Área\s+?:(?P<area>.+(?=Assunto:)).*"
        r"Assunto:(?P<subject>.+(?=Origem:)).*"
        r"Distribuição:(?P<distribution>.+(?=Relator:))"
    )
    process_data = await _simplify_process_data(process_data)

    match_data = re.search(process_details_regex, process_data, re.IGNORECASE)

    if not match_data:
        raise ValueError

    # In this context, there is no judge or action value info...
    return {**{"judge": "", "action": ""}, **match_data.groupdict()}


async def execute_query(base_url: str, query_input: QueryInput):

    query_url = await build_query_url(base_url, query_input.process_number)
    query_result = await utils.download_process_page(query_url)
    is_process_list = await is_query_result_a_process_list(query_result)

    if is_process_list:

        processes_urls = await _extract_processes_urls(base_url, query_result)
        # TODO: If there is many processes urls, consider refactoring this function to
        # become an async generator too.
        return [
            await parse_process(query_input.process_number, process_page)
            async for process_page in download_processes_pages(processes_urls)
        ]

    else:

        return [await parse_process(query_input.process_number, query_result)]
