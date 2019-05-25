from jus_brasil.crawlers import cpopg, cposg, utils
from jus_brasil.crawlers.models import QueryInput, QueryOutput


async def execute_crawler_first_jurisdiction(query_input: QueryInput):

    jurisdiction_url = await utils.get_first_jurisdiction(query_input.process_court)
    return await cpopg.execute_query(jurisdiction_url, query_input)


async def execute_crawler_second_jurisdiction(query_input: QueryInput):

    jurisdiction_url = await utils.get_second_jurisdiction(query_input.process_court)
    return await cposg.execute_query(jurisdiction_url, query_input)


async def execute_crawler_second_appeal_jurisdiction(query_input: QueryInput):

    jurisdiction_url = await utils.get_second_appeal_jurisdiction(
        query_input.process_court
    )

    if jurisdiction_url:
        return await cposg.execute_query(jurisdiction_url, query_input)
    return []


async def execute_crawler(query_input: QueryInput) -> QueryOutput:

    first_juristiction = await execute_crawler_first_jurisdiction(query_input)
    second_juristiction = await execute_crawler_second_jurisdiction(query_input)
    second_jurisdiction_appeal = await execute_crawler_second_appeal_jurisdiction(
        query_input
    )

    return QueryOutput(
        first_juristiction=first_juristiction,
        second_juristiction=second_juristiction,
        second_jurisdiction_appeal=second_jurisdiction_appeal,
    )
