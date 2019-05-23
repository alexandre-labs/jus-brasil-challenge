from fastapi import APIRouter

from jus_brasil.crawlers import execute_crawler
from jus_brasil.crawlers.models import QueryInput, QueryOutPut


router = APIRouter()


@router.post("/query", response_model=QueryOutPut)
async def query_process_data(query_input: QueryInput):
    return await execute_crawler(query_input)
