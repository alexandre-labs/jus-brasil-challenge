import asynctest
import pytest

from jus_brasil.crawlers import cpopg


@pytest.mark.asyncio
@asynctest.patch("jus_brasil.crawlers.cpopg._extract_unified_year_and_jurisdiction")
async def test_build_query(mocked_extractor_function):

    mocked_extractor_function.return_value = "XXXXX", "YYYY"

    query_url = await cpopg.build_query_url("https://esaj.gov.br", "the-process-number")

    mocked_extractor_function.assert_called_once_with("the-process-number")

    assert query_url.startswith("https://esaj.gov.br") is True
    assert "XXXXX" in query_url
    assert "YYYY" in query_url


@pytest.mark.asyncio
async def test_extract_process_details_valid_process_data():

    result = await cpopg._extract_process_details(
        "Classe: process-class\nÁrea: Civil\nAssunto: Franquia"
        "Distribuição: 10/10/2010\nControle:teste\nJuiz: Test\n"
        "Valor da ação: 1000.00"
    )
    expected_result = {
        "class": " process-class ",
        "area": " Civil ",
        "subject": " Franquia",
        "distribution": " 10/10/2010 ",
        "judge": " Test ",
        "action": " 1000.00",
    }

    assert result == expected_result


@pytest.mark.asyncio
async def test_extract_process_details_invalid_process_data():

    with pytest.raises(ValueError):
        await cpopg._extract_process_details("invalid-process-data")


@pytest.mark.asyncio
@asynctest.patch("jus_brasil.crawlers.cpopg.parse_process")
@asynctest.patch("jus_brasil.crawlers.cpopg.download_process_page")
@asynctest.patch("jus_brasil.crawlers.cpopg.build_query_url")
async def test_execute_query(
    mocked_build_query_url, mocked_download_process_page, mocked_parse_process
):
    mocked_build_query_url.return_value = "the-query-url"
    mocked_download_process_page.return_value = "the-process-page"

    query_input = cpopg.QueryInput(
        process_number="1002298-86.2015.8.26.0271", process_court="TJSP"
    )

    await cpopg.execute_query("https://esaj.gov.br", query_input)

    mocked_build_query_url.assert_called_once_with(
        "https://esaj.gov.br", query_input.process_number
    )
    mocked_download_process_page.assert_called_once_with("the-query-url")
    mocked_parse_process.assert_called_once()
