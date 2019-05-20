import re

from bs4 import BeautifulSoup


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
