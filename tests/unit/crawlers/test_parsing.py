import asynctest
import pytest


from jus_brasil.crawlers import parsing
from jus_brasil.crawlers.models import Activity, Part


@pytest.mark.asyncio
async def test_simplify_process_data():

    process_data = "\n\n\n\r\r\r\t\tsome data\n\n\n\n\n\n"

    assert await parsing._simplify_process_data(process_data) == " some data "


@pytest.mark.asyncio
async def test_parse_process_details(mocker):

    _mock = mocker.Mock()

    async def details_extractor(process_soup):
        nonlocal _mock
        _mock(process_soup)

    process_soup = parsing.BeautifulSoup(
        "<h1>Dados do processo</h1>" "<table>process-details</table>", "lxml"
    )

    await parsing.parse_process_details(details_extractor, process_soup)

    _mock.assert_called_once_with("process-details")


@pytest.mark.asyncio
async def test_parse_process_parts():

    process_soup = parsing.BeautifulSoup(
        """
        <table id="tablePartesPrincipais"
        style="margin-left:15px; margin-top:1px;"
               width="98%" cellspacing="0" cellpadding="0" border="0" align="center">
        <tbody><tr class="fundoClaro">
                <td style="padding-bottom: 5px" width="141" valign="top" align="right">
                        <span class="mensagemExibindo">Autor:&nbsp;</span>
                </td>
                <td style="padding-bottom: 5px" width="*" align="left">
                                                Justiça Pública
                        </td>
        </tr>
        <tr class="fundoClaro">
                <td style="padding-bottom: 5px" width="141" valign="top" align="right">
                        <span class="mensagemExibindo">Réu:&nbsp;</span>
                </td>
                <td style="padding-bottom: 5px" width="*" align="left">
                                                TEST PART 1
                        </td>
        </tr>
        <tr class="fundoClaro">
                <td style="padding-bottom: 5px" width="141" valign="top" align="right">
                        <span class="mensagemExibindo">Advogada:&nbsp;</span>
                </td>
                <td style="padding-bottom: 5px" width="*" align="left">
                                                TEST PART 2
                        </td>
        </tr>

        </tbody></table>
    """,
        "lxml",
    )

    result = await parsing.parse_process_parts(process_soup)
    expected_result = [
        [
            Part(role="Autor:", identification="Justiça Pública"),
            Part(role="Réu:", identification="TEST PART 1"),
            Part(role="Advogada:", identification="TEST PART 2"),
        ]
    ]

    assert result == expected_result


@pytest.mark.asyncio
async def test_parse_process_activities():

    process_soup = parsing.BeautifulSoup(
        """
    <table width="100%" cellspacing="0" cellpadding="0" border="0">
     <tbody><tr valign="top">
     <td valign="top" nowrap="nowrap" height="21"
        background="tjsp-first-jurisdiction_files/fundo_subtitulo.gif">
     <h2 class="subtitle">
     Movimentações
     </h2>
     </td>
     <td aria-hidden="true" width="90%" valign="top"
        background="tjsp-first-jurisdiction_files/fundo_subtitulo2.gif">
     <img src="tjsp-first-jurisdiction_files/final_subtitulo.gif"
        tabindex="-1" width="16" height="20">
     </td>
     </tr>
    </tbody></table>
    </div>
    <div id="divLinksTituloBlocoMovimentacoes">
    <input id="mensagemNaoExibidamovimentacoes" type="hidden"
        value="Exibindo todas as movimentações.">
    <input id="linkNaoExibidomovimentacoes" type="hidden"
        value="&lt;span id=&quot;setasDireitamovimentacoes&quot;
     class=&quot;setasDireita&quot;&gt;&amp;gt;&amp;gt;
        &lt;/span&gt;Listar somente as 5 últimas.">
    <span id="mensagensExibindomovimentacoes"
        class="mensagemExibindo">Exibindo 5 últimas.</span>
    &nbsp; <a id="linkmovimentacoes" href="javascript:" class="linkNaoSelecionado">
    <span id="setasDireitamovimentacoes"
        class="setasDireita">&gt;&gt;</span>Listar todas as movimentações.</a>
    </div>
    <table style="margin-left:15px; margin-top:1px;"
        width="98%" cellspacing="0" cellpadding="0" border="0" align="center">
    <thead>
    <tr>
    <th class="label" style="vertical-align: bottom" width="120">Data</th>
    <th aria-hidden="true" width="20" valign="middle">&nbsp;</th>
    <th class="label" valign="middle">Movimento</th>
    </tr>
    <tr class="fundoEscuro" aria-hidden="true" height="2">
    <td></td>
    <td></td>
    <td></td>
    </tr>
    </thead>
    <tbody id="tabelaUltimasMovimentacoes">
    <tr class="fundoClaro" style="">
    <td style="vertical-align: top" width="120">
    30/04/2019
    </td>
    <td aria-hidden="true" width="20" valign="top">
    </td>
    <td style="vertical-align: top; padding-bottom: 5px">
    Autos no Prazo
    <br>
    <span style="font-style: italic;">
    16/06 <br><b>Vencimento: </b>16/06/2019
    </span>
    </td>
    </tr>
    """,
        "lxml",
    )  # noqa

    expected_result = [
        Activity(
            date="30/04/2019", activity="Autos no Prazo 16/06 Vencimento: 16/06/2019"
        )
    ]

    assert await parsing.parse_process_activities(process_soup) == expected_result


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "process_soup, expected",
    [
        (
            parsing.BeautifulSoup(
                "Não existem informações disponíveis para os parâmetros informados.",
                "lxml",
            ),
            False,
        ),
        (
            parsing.BeautifulSoup(
                "Some html that not contains the phrase indicating the process exists",
                "lxml",
            ),
            True,
        ),
    ],
)
async def test_ensure_process_exists(process_soup, expected):
    assert await parsing.ensure_process_exists(process_soup) is expected


@pytest.mark.asyncio
@asynctest.patch("jus_brasil.crawlers.parsing.parse_process_details")
@asynctest.patch("jus_brasil.crawlers.parsing.parse_process_parts")
@asynctest.patch("jus_brasil.crawlers.parsing.parse_process_activities")
async def test_parse_process(
    mocked_parse_process_activities,
    mocked_parse_process_parts,
    mocked_parse_process_details,
):

    with asynctest.patch("jus_brasil.crawlers.parsing.models.Process"):
        await parsing.parse_process(
            "the-process-number",
            process_page="process-html-page",
            details_extractor=lambda x: x,
        )

    mocked_parse_process_details.assert_called_once()
    mocked_parse_process_parts.assert_called_once()
    mocked_parse_process_activities.assert_called_once()
