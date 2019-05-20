import pytest
from bs4 import BeautifulSoup


from jus_brasil.esaj.tjsp.cpopg import parsing


@pytest.mark.asyncio
async def test_process_details(cpopg_process_page):
    """Fixture details:

        Processo:
        1002298-86.2015.8.26.0271
        Classe:
        Procedimento Comum Cível

        Área: Cível
        Assunto: Franquia
        Outros assuntos: Indenização por Dano Material,Indenização por Dano Moral,
        Obrigações,Perdas e Danos
        Distribuição: 26/05/2015 às 18:31 - Livre
                2ª Vara Cível - Foro de Itapevi
        Controle: 	2015/001380
        Juiz: 	Márcia Blanes
        Valor da ação: 	R$ 866.000,00
    """

    process_soup = BeautifulSoup(cpopg_process_page, "lxml")
    process_details = await parsing.parse_process_details(process_soup)

    assert process_details["process_number"] == "1002298-86.2015.8.26.0271"
    assert process_details["process_class"] == "Procedimento Comum Cível"
    assert process_details["process_area"] == "Cível"
    assert process_details["process_subject"] == "Franquia"
    assert process_details["process_subject_details"] == (
        "Indenização por Dano Material,Indenização por Dano Moral,"
        "Obrigações,Perdas e Danos"
    )
    assert process_details["process_distribution"] == (
        "26/05/2015 às 18:31 - Livre 2ª Vara Cível - Foro de Itapevi"
    )
    assert process_details["process_control_number"] == "2015/001380"
    assert process_details["process_judge"] == "Márcia Blanes"
    assert process_details["process_action_value"] == "R$ 866.000,00"


@pytest.mark.asyncio
async def test_process_parts(cpopg_process_page):
    """Fixture details:
         Partes do processo

        Exibindo todas as partes.
        Reqte:  	DOLCE DUO COMÉRCIO VAREJISTA DE DOCES BALAS BOMBONS E SEMELHANTES LTDA ME
        Advogada:  Paula Rodrigues da Silva
        Advogado:  Diego Gomes Dias
        Advogada:  Karina de Almeida Batistuci
        Reprtate:  MARIANA REBELLO MARQUES DA COSTA SANTOS
        Reqte:  	REBELLOS COMÉRCIO VAREJISTA DOCES BALAS BOMBONS LTDA
        Advogada:  Paula Rodrigues da Silva
        Reprtate:  MARIANA REBELLO MARQUES DA COSTA SANTOS
        Reqte:  	MARIANA REBELLO MARQUES DA COSTA SANTOS
        Advogada:  Paula Rodrigues da Silva
        Reqte:  	FÁBIO FURQUIM DA COSTA SANTOS
        Advogada:  Paula Rodrigues da Silva
        Reqte:  	YARA SILVIA REBELLO
        Advogada:  Paula Rodrigues da Silva
        Reqdo:  	FRANQUIA SHOW ASSESSORIA EM NEGÓCIOS LTDA
        Advogado:  Andre Boschetti Oliva
        Reqdo:  	IBAC INDÚSTRIA BRASILEIRA DE ALIMENTOS E CHOCOLATES LTDA
        Advogado:  Andre Boschetti Oliva
    """

    process_soup = BeautifulSoup(cpopg_process_page, "lxml")
    process_parts = await parsing.parse_process_parts(process_soup)

    assert (
        (
            "Reqte:",
            "DOLCE DUO COMÉRCIO VAREJISTA DE DOCES BALAS BOMBONS E SEMELHANTES LTDA ME",
        ),
        [
            ("Advogada:", "Paula Rodrigues da Silva"),
            ("Advogado:", "Diego Gomes Dias"),
            ("Advogada:", "Karina de Almeida Batistuci"),
            ("Reprtate:", "MARIANA REBELLO MARQUES DA COSTA SANTOS"),
        ],
    ) in process_parts, process_parts

    assert (
        ("Reqte:", "REBELLOS COMÉRCIO VAREJISTA DOCES BALAS BOMBONS LTDA"),
        [
            ("Advogada:", "Paula Rodrigues da Silva"),
            ("Reprtate:", "MARIANA REBELLO MARQUES DA COSTA SANTOS"),
        ],
    ) in process_parts

    assert (
        ("Reqte:", "MARIANA REBELLO MARQUES DA COSTA SANTOS"),
        [("Advogada:", "Paula Rodrigues da Silva")],
    ) in process_parts

    assert (
        ("Reqte:", "FÁBIO FURQUIM DA COSTA SANTOS"),
        [("Advogada:", "Paula Rodrigues da Silva")],
    ) in process_parts

    assert (
        ("Reqte:", "YARA SILVIA REBELLO"),
        [("Advogada:", "Paula Rodrigues da Silva")],
    ) in process_parts

    assert (
        ("Reqdo:", "FRANQUIA SHOW ASSESSORIA EM NEGÓCIOS LTDA"),
        [("Advogado:", "Andre Boschetti Oliva")],
    ) in process_parts

    assert (
        ("Reqdo:", "IBAC INDÚSTRIA BRASILEIRA DE ALIMENTOS E CHOCOLATES LTDA"),
        [("Advogado:", "Andre Boschetti Oliva")],
    ) in process_parts
