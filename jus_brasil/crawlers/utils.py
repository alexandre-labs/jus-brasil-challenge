import re
import typing as t

import aiohttp

from jus_brasil import config
from jus_brasil.crawlers.models import KnownCourts, RE_UNIFIED_YEAR_AND_JUS


async def _extract_unified_year_and_jurisdiction(process_number: str) -> t.Sequence[str]:

    match_strings = re.search(RE_UNIFIED_YEAR_AND_JUS, process_number)
    if not match_strings:
        return "", ""

    return match_strings.groups()


async def get_process_page(session: aiohttp.ClientSession, process_url: str):
    async with session.get(process_url, ssl=False) as response:
        return await response.text()


async def download_process_page(process_url: str):
    async with aiohttp.ClientSession() as session:
        return await get_process_page(session, process_url)


async def get_first_jurisdiction(known_court: KnownCourts) -> str:
    return config.TJSP_PG if known_court == KnownCourts.tjsp else config.TJMS_PG


async def get_second_jurisdiction(known_court: KnownCourts) -> str:
    return config.TJSP_SG if known_court == KnownCourts.tjsp else config.TJMS_SG


async def get_second_appeal_jurisdiction(known_court: KnownCourts) -> t.Optional[str]:

    if known_court == KnownCourts.tjsp:
        return config.TJSP_SG_REC
    return None
