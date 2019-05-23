from .models import KnownCourts, QueryInput, QueryOutPut
from .tjsp.cpopg import crawler as tjsp_pg_crawler


async def execute_crawler(query_input: QueryInput) -> QueryOutPut:

    if query_input.process_court == KnownCourts.tjsp:
        return await tjsp_pg_crawler.execute_query(query_input)
    else:
        raise NotImplementedError
