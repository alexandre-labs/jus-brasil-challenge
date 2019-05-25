from jus_brasil.crawlers import cpopg, cposg, utils
from jus_brasil.crawlers.models import KnownCourts, QueryInput, QueryOutput


async def get_all_urls(process_court: KnownCourts):
    return (
        await utils.get_first_jurisdiction(process_court),
        await utils.get_second_jurisdiction(process_court),
        await utils.get_second_jurisdiction_appeal(process_court),
    )


async def execute_crawler(query_input: QueryInput) -> QueryOutput:

    first, second, second_appeal = await get_all_urls(query_input.process_court)

    first_juristiction = await cpopg.execute_query(first, query_input)

    second_juristiction = await cposg.execute_query(second, query_input)

    if second_appeal:
        second_jurisdiction_appeal = await cposg.execute_query(
            second_appeal, query_input
        )
    else:
        second_jurisdiction_appeal = None

    return QueryOutput(
        first_juristiction=first_juristiction,
        second_juristiction=second_juristiction,
        second_jurisdiction_appeal=second_jurisdiction_appeal,
    )
