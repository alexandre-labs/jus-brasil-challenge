from jus_brasil import config
from jus_brasil.crawlers import download
from jus_brasil.crawlers.models import QueryInput
from .parsing import parse_process


async def execute_query(query_input: QueryInput):

    query_url = await download.build_query_url(config.TJSP_PG, query_input.process_number)
    process_page = await download.download_process_page(query_url)
    process = await parse_process(process_page)

    return process
