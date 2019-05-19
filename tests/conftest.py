import pytest


from tests.fixtures import fixture_tjsp_pg
from tests.fixtures import fixture_tjsp_sg


@pytest.fixture(scope="module")
def cpopg_process_page():
    return fixture_tjsp_pg.DATA


@pytest.fixture(scope="module")
def cposg_process_page():
    return fixture_tjsp_sg.DATA
