import pathlib

import pytest


@pytest.fixture
def tjsp_first_jurisdiction():
    cwd = pathlib.Path(__file__).cwd()
    with open(f"{cwd}/tests/fixtures/tjsp-first-jurisdiction.html") as f:
        yield f.read()


@pytest.fixture
def tjsp_second_jurisdiction():
    cwd = pathlib.Path(__file__).cwd()
    with open(f"{cwd}/tests/fixtures/tjsp-second-jurisdiction.html") as f:
        yield f.read()


@pytest.fixture
def tjsp_second_appeal_jurisdiction():
    cwd = pathlib.Path(__file__).cwd()
    with open(f"{cwd}/tests/fixtures/tjsp-second-appeal-jurisdiction.html") as f:
        yield f.read()
