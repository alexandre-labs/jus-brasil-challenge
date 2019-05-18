import aiohttp
import pytest

from jus_brasil.esaj.tjsp import download


@pytest.mark.asyncio
async def test_get_process_page(aresponses):

    query_url = "https://esaj.tjsp.jus.br/cpopg/show.do?processo.codigo=7J0001D040000"
    aresponses.add("esaj.tjsp.jus.br", response="some weird html", match_querystring=True)

    async with aiohttp.ClientSession() as session:
        process_page = await download.get_process_page(session, query_url)

    assert process_page == "some weird html"


@pytest.mark.asyncio
async def test_download_page(aresponses):

    aresponses.add("esaj.tjsp.jus.br", response="some weird html", match_querystring=True)

    query_url = "https://esaj.tjsp.jus.br/cpopg/show.do?processo.codigo=7J0001D040000"
    process_page = await download.download_process_page(query_url)

    assert process_page == "some weird html"
