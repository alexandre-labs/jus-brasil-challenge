from fastapi import APIRouter

from jus_brasil.crawlers import execute_crawler
from jus_brasil.crawlers.models import QueryInput, QueryOutput


router = APIRouter()


@router.post("/query", response_model=QueryOutput)
async def query_process_data(query_input: QueryInput) -> QueryOutput:
    return await execute_crawler(query_input)
