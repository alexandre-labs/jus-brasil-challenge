import pytest

from hypothesis import assume
from hypothesis import given
from hypothesis import settings
from hypothesis import strategies as st

from jus_brasil.esaj.tjsp import download


@pytest.mark.asyncio
@given(st.from_regex(download.RE_UNIFIED_YEAR_AND_JUS))
@settings(max_examples=200)
async def test_extract_unified_year_and_juristiction(process_number: str):

    assume(process_number[-1].isdigit())  # Avoiding samples that ends with "\W"

    unif_year, jurisdiction = process_number[0:15], process_number[-4:]
    result = await download._extract_unified_year_and_jurisdiction(process_number)

    assert (unif_year, jurisdiction) == result


@pytest.mark.asyncio
@given(st.from_regex(download.RE_UNIFIED_YEAR_AND_JUS))
@settings(max_examples=1)
async def test_build_query_url(process_number):

    query_url: str = await download.build_query_url('https://esaj.tjsp.site', process_number)

    assert query_url.startswith('https://esaj.tjsp.site')
    assert f"numeroDigitoAnoUnificado={process_number[:15]}" in query_url
    assert f"foroNumeroUnificado={process_number[-4:]}" in query_url
    assert f"dadosConsulta.valorConsultaNuUnificado={process_number}" in query_url
