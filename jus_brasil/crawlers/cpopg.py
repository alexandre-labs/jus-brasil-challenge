import re
import typing as t

from jus_brasil.crawlers.models import QueryInput
from jus_brasil.crawlers.parsing import _simplify_process_data
from jus_brasil.crawlers.parsing import parse_process
from jus_brasil.crawlers.utils import _extract_unified_year_and_jurisdiction
from jus_brasil.crawlers.utils import download_process_page


async def build_query_url(base_url: str, process_number: str) -> str:

    unif_year, jurisdiction = await _extract_unified_year_and_jurisdiction(process_number)

    return (
        f"{base_url}?conversationId=&dadosConsulta.localPesquisa.cdLocal=-1&"
        f"cbPesquisa=NUMPROC&dadosConsulta.tipoNuProcesso=UNIFICADO&"
        f"numeroDigitoAnoUnificado={unif_year}&foroNumeroUnificado={jurisdiction}&"
        f"dadosConsulta.valorConsultaNuUnificado={process_number}&"
        f"dadosConsulta.valorConsulta=&uuidCaptcha="
    )


async def _extract_process_details(process_data: str) -> t.Dict[str, str]:

    process_details_regex = (
        r"Classe:(?P<class>.+(?=Área:))"
        r"Área:(?P<area>.+(?=Assunto:)).*"
        r"Assunto:(?P<subject>.+(?=Distribuição:)).*"
        r"Distribuição:(?P<distribution>.+(?=Controle:)).*"
        r"Juiz:(?P<judge>.+(?=Valor da ação:))"
        r"Valor da ação:(?P<action>.+)"
    )
    process_data = await _simplify_process_data(process_data)

    process_details = re.search(process_details_regex, process_data, re.IGNORECASE)
    if not process_details:
        raise ValueError

    return process_details.groupdict()


async def execute_query(base_url: str, query_input: QueryInput):

    query_url = await build_query_url(base_url, query_input.process_number)
    process_page = await download_process_page(query_url)
    process = await parse_process(
        query_input.process_number,
        process_page,
        details_extractor=_extract_process_details,
    )

    return process
