import pytest
from hypothesis import assume
from hypothesis import given
from hypothesis import settings
from hypothesis import strategies as st

from jus_brasil.crawlers import utils


@pytest.mark.asyncio
@given(st.from_regex(utils.RE_UNIFIED_YEAR_AND_JUS))
@settings(max_examples=200)
async def test_extract_unified_year_and_juristiction(process_number: str):

    assume(process_number[-1].isdigit())  # Avoiding samples that ends with "\W"

    unif_year, jurisdiction = process_number[0:15], process_number[-4:]
    result = await utils._extract_unified_year_and_jurisdiction(process_number)

    assert (unif_year, jurisdiction) == result


@pytest.mark.asyncio
async def test_extract_unified_year_and_juristiction_invalid_number():

    process_number = "00000.00000.0000.0"

    result = await utils._extract_unified_year_and_jurisdiction(process_number)

    assert ("", "") == result


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "court,expected",
    [
        (utils.KnownCourts.tjsp, utils.config.TJSP_PG),
        (utils.KnownCourts.tjms, utils.config.TJMS_PG),
    ],
)
async def test_get_first_jurisdiction(court, expected):
    assert await utils.get_first_jurisdiction(court) == expected


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "court,expected",
    [
        (utils.KnownCourts.tjsp, utils.config.TJSP_SG),
        (utils.KnownCourts.tjms, utils.config.TJMS_SG),
    ],
)
async def test_get_second_jurisdiction(court, expected):
    assert await utils.get_second_jurisdiction(court) == expected


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "court,expected",
    [(utils.KnownCourts.tjsp, utils.config.TJSP_SG_REC), (utils.KnownCourts.tjms, None)],
)
async def test_get_second_appeal_jurisdiction(court, expected):
    assert await utils.get_second_appeal_jurisdiction(court) == expected
