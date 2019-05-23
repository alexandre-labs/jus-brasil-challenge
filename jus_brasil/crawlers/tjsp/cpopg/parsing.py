import asyncio
import itertools as i
import re
import typing as t

from bs4 import BeautifulSoup
from bs4.element import Tag

from jus_brasil.crawlers import models


async def _extract_process_details(process_data: str) -> t.Dict[str, str]:

    process_details_regex = (
        r"Processo:(?P<number>.+(?=Classe:))"
        r"Classe:(?P<class>.+(?=Área:))"
        r"Área:(?P<area>.+(?=Assunto:))"
        r"Assunto:(?P<subject>.+(?=Outros assuntos:))"
        r"Outros assuntos:(?P<subject_details>.+(?=Distribuição:))"
        r"Distribuição:(?P<distribution>.+(?=Controle:))"
        r"Controle:(?P<control>.+(?=Juiz:))"
        r"Juiz:(?P<judge>.+(?=Valor da ação:))"
        r"Valor da ação:(?P<action>.+)"
    )
    process_details = re.search(
        process_details_regex, re.sub("[\n\r\t]", " ", process_data)
    )
    if not process_details:
        raise ValueError

    return {
        key: re.sub(" +", " ", value).strip()
        for key, value in iter(process_details.groupdict().items())
    }


async def parse_process_details(process_soup: BeautifulSoup) -> t.Dict[str, str]:

    raw_process_details = (
        process_soup.find(text=re.compile("Dados do processo"))
        .find_next("table")
        .text.strip()
    )

    return await _extract_process_details(raw_process_details)


async def _extract_process_parts(parts_table: Tag) -> t.List[t.Tuple[str, str]]:

    initial_parts_data = i.chain.from_iterable(
        td.text.split("\n") for td in parts_table.find_all("td")
    )
    text_parts = tuple(
        data.strip() for data in filter(lambda x: x.strip(), initial_parts_data)
    )

    return list(zip(text_parts[::2], text_parts[1::2]))


async def _parse_part(part: t.Tuple[str, str]) -> models.Part:
    return models.Part(role=part[0], identification=part[1])


async def _group_parts_and_lawyers(
    parts: t.List[t.Tuple[str, str]]
) -> t.List[t.List[models.Part]]:

    if not parts:
        return []

    part = parts[0]
    part_lawyers = tuple(
        i.takewhile(lambda item: not item[0].startswith("Req"), parts[1:])
    )
    stopped_at = len(part_lawyers) + 1
    part_and_lawyers = [await _parse_part(_p) for _p in (part, *part_lawyers)]

    return [part_and_lawyers] + await _group_parts_and_lawyers(parts[stopped_at:])


async def parse_process_parts(process_soup: BeautifulSoup) -> t.List[t.List[models.Part]]:

    parsed_data = await _extract_process_parts(
        process_soup.select_one("#tableTodasPartes")
    )

    grouped_parts = await _group_parts_and_lawyers(parsed_data)

    return grouped_parts


async def _parse_activity(
    activity_date: str, activity_text: t.List[str]
) -> models.Activity:

    return models.Activity(
        date=re.sub(r"[\s\n]+", " ", activity_date),
        activity=re.sub(r"[\s\n]+", " ", "".join(activity_text)),
    )


async def _group_activity_data(activities_data: t.List):

    if not activities_data:
        return []

    activity_date = activities_data[0]
    activity_text = list(
        i.takewhile(
            lambda item: not re.match(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$", item),
            activities_data[1:],
        )
    )
    stopped_at = len(activity_text) + 1

    return [asyncio.create_task(_parse_activity(activity_date, activity_text))] + (
        await _group_activity_data(activities_data[stopped_at:])
    )


async def parse_process_activities(
    process_soup: BeautifulSoup
) -> t.List[models.Activity]:  # noqa

    activities_data = list(
        td.text.strip()
        for td in process_soup.find(text=re.compile("Movimentações"))
        .find_next("table")
        .select("td", attr={"class": ""})
        if td.text.strip()
    )

    process_activities = []
    for res in asyncio.as_completed((await _group_activity_data(activities_data))):
        process_activities.append((await res))

    return process_activities


async def parse_process(process_page: str) -> models.Process:

    process_soup = BeautifulSoup(process_page, "lxml")

    return models.Process(
        **(await parse_process_details(process_soup)),
        parts=(await parse_process_parts(process_soup)),
        activities=(await parse_process_activities(process_soup)),
    )
