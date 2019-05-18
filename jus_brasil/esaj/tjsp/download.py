import re
import re.Match
import typing as t

import aiohttp


RE_UNIFIED_YEAR_AND_JUS = r"^(?P<unif_year>[0-9]{7}\-[0-9]{2}\.[0-9]{4})\.[0-9]\.[0-9]{2}\.(?P<jurisdiction>[0-9]{4})$"  # noqa


async def _extract_unified_year_and_jurisdiction(
    process_number: str
) -> t.Sequence[str]:  # noqa

    match_strings = re.search(RE_UNIFIED_YEAR_AND_JUS, process_number)
    if not match_strings:
        return "", ""

    return match_strings.groups()


async def build_query_url(base_url: str, process_number: str) -> str:

    unif_year, jurisdiction = await _extract_unified_year_and_jurisdiction(process_number)

    return (
        f"{base_url}?conversationId=&dadosConsulta.localPesquisa.cdLocal=-1&"
        f"cbPesquisa=NUMPROC&dadosConsulta.tipoNuProcesso=UNIFICADO&"
        f"numeroDigitoAnoUnificado={unif_year}&foroNumeroUnificado={jurisdiction}&"
        f"dadosConsulta.valorConsultaNuUnificado={process_number}&"
        f"dadosConsulta.valorConsulta=&uuidCaptcha="
    )


async def get_process_page(session: aiohttp.ClientSession, process_url: str):
    async with session.get(process_url, verify_ssl=False) as response:
        return await response.text()


async def download_process_page(process_url: str):
    async with aiohttp.ClientSession() as session:
        return await get_process_page(session, process_url)
