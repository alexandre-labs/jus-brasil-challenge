import itertools as i
import re
import typing as t

from bs4 import BeautifulSoup
from bs4.element import Tag


async def _extract_process_details(process_data: str):

    process_details_regex = (
        r"Processo:(?P<process_number>.+(?=Classe:))"
        r"Classe:(?P<process_class>.+(?=Área:))"
        r"Área:(?P<process_area>.+(?=Assunto:))"
        r"Assunto:(?P<process_subject>.+(?=Outros assuntos:))"
        r"Outros assuntos:(?P<process_subject_details>.+(?=Distribuição:))"
        r"Distribuição:(?P<process_distribution>.+(?=Controle:))"
        r"Controle:(?P<process_control_number>.+(?=Juiz:))"
        r"Juiz:(?P<process_judge>.+(?=Valor da ação:))"
        r"Valor da ação:(?P<process_action_value>.+)"
    )
    process_details = re.search(
        process_details_regex, re.sub("[\n\r\t]", " ", process_data)
    )
    if not process_details:
        raise ValueError
    return process_details.groupdict()


async def parse_process_details(process_soup: BeautifulSoup):

    raw_process_details = (
        process_soup.find(text=re.compile("Dados do processo"))
        .find_next("table")
        .text.strip()
    )
    process_details = await _extract_process_details(raw_process_details)

    return {
        key: re.sub(" +", " ", value).strip() for key, value in process_details.items()
    }


async def _extract_process_parts(parts_table: Tag):

    initial_parts_data = i.chain.from_iterable(
        td.text.split("\n") for td in parts_table.find_all("td")
    )
    text_parts = tuple(
        data.strip() for data in filter(lambda x: x.strip(), initial_parts_data)
    )

    return list(zip(text_parts[::2], text_parts[1::2]))


async def _group_parts_and_lawyers(parts: t.List[t.Tuple[str]]):

    if len(parts) < 2:
        return parts

    part: t.Tuple[str] = parts[0]
    part_lawyers: t.List[t.Tuple[str]] = list(
        i.takewhile(lambda item: not item[0].startswith("Req"), parts[1:])
    )
    stopped_at: int = parts.index(part_lawyers[-1]) + 1

    return [(part, part_lawyers)] + await _group_parts_and_lawyers(parts[stopped_at:])


async def parse_process_parts(process_soup: BeautifulSoup):

    parsed_data = await _extract_process_parts(
        process_soup.select_one("#tableTodasPartes")
    )

    grouped_parts = await _group_parts_and_lawyers(parsed_data)

    return grouped_parts
