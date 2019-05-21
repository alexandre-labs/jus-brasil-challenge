import pytest
from bs4 import BeautifulSoup


from jus_brasil.crawlers.tjsp.cpopg import parsing


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
        Controle:       2015/001380
        Juiz:   Márcia Blanes
        Valor da ação:  R$ 866.000,00
    """

    process_soup = BeautifulSoup(cpopg_process_page, "lxml")
    process_details = await parsing.parse_process_details(process_soup)

    assert process_details["number"] == "1002298-86.2015.8.26.0271"
    assert process_details["class"] == "Procedimento Comum Cível"
    assert process_details["area"] == "Cível"
    assert process_details["subject"] == "Franquia"
    assert process_details["subject_details"] == (
        "Indenização por Dano Material,Indenização por Dano Moral,"
        "Obrigações,Perdas e Danos"
    )
    assert process_details["distribution"] == (
        "26/05/2015 às 18:31 - Livre 2ª Vara Cível - Foro de Itapevi"
    )
    assert process_details["control_number"] == "2015/001380"
    assert process_details["judge"] == "Márcia Blanes"
    assert process_details["action_value"] == "R$ 866.000,00"


@pytest.mark.asyncio
async def test_process_parts(cpopg_process_page):
    """Fixture details:
         Partes do processo

        Exibindo todas as partes.
        Reqte: DOLCE DUO COMÉRCIO VAREJISTA DE DOCES BALAS BOMBONS E SEMELHANTES LTDA ME
        Advogada: Paula Rodrigues da Silva
        Advogado: Diego Gomes Dias
        Advogada: Karina de Almeida Batistuci
        Reprtate: MARIANA REBELLO MARQUES DA COSTA SANTOS
        Reqte:         REBELLOS COMÉRCIO VAREJISTA DOCES BALAS BOMBONS LTDA
        Advogada: Paula Rodrigues da Silva
        Reprtate: MARIANA REBELLO MARQUES DA COSTA SANTOS
        Reqte:         MARIANA REBELLO MARQUES DA COSTA SANTOS
        Advogada: Paula Rodrigues da Silva
        Reqte:         FÁBIO FURQUIM DA COSTA SANTOS
        Advogada: Paula Rodrigues da Silva
        Reqte:         YARA SILVIA REBELLO
        Advogada: Paula Rodrigues da Silva
        Reqdo:         FRANQUIA SHOW ASSESSORIA EM NEGÓCIOS LTDA
        Advogado: Andre Boschetti Oliva
        Reqdo:         IBAC INDÚSTRIA BRASILEIRA DE ALIMENTOS E CHOCOLATES LTDA
        Advogado: Andre Boschetti Oliva
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


@pytest.mark.asyncio
async def test_process_activities(cpopg_process_page):
    """Fixture details (some of them):
         Movimentações

        Exibindo todas as movimentações.   >>Listar somente as 5 últimas.
        Data            Movimento

        04/03/2019              Suspensão do Prazo
        Prazo referente ao usuário foi alterado para 16/07/2019 devido à
        alteração da tabela de feriados
        24/12/2018              Suspensão do Prazo
        Prazo referente ao usuário foi alterado para 15/07/2019 devido à
        alteração da tabela de feriados
        29/11/2018              Petição Juntada
        Nº Protocolo: WITV.18.70063977-0 Tipo da Petição: Petições Diversas
        Data: 29/11/2018 11:41
        14/11/2018              Certidão de Publicação Expedida
        Relação :0520/2018 Data da Disponibilização: 14/11/2018
        Data da Publicação: 21/11/2018 Número do Diário: 2700 Página: 444/460
    """
    process_soup = BeautifulSoup(cpopg_process_page, "lxml")
    process_activities = await parsing.parse_process_activities(process_soup)

    assert (
        "04/03/2019",
        "Suspensão do Prazo Prazo referente ao usuário foi alterado para "
        "16/07/2019 devido à alteração da tabela de feriados",
    ) in process_activities
