import logging
import logging.config

import pandas
from snowflake_test import settings
from snowflake.connector import connect

SQL = """-- Test query for snowflake-test
SELECT *
FROM lyst_analytics.raw_page_views
WHERE event_timestamp >= '2020-01-01'
AND event_timestamp < '2020-01-13'
"""

log = logging.getLogger("snowflake_test.query")


def query():
    logging.config.dictConfig(settings.LOGGING)
    log.info("Starting to test querying against Snowflake")
    with connect(
        user=settings.SNOWFLAKE_USER,
        password=settings.SNOWFLAKE_PASSWORD,
        account=settings.SNOWFLAKE_ACCOUNT,
        database=settings.SNOWFLAKE_DATABASE,
        role=settings.SNOWFLAKE_ROLE,
    ) as conn:
        with conn.cursor() as cursor:
            log.info("Switching to warehouse %s", settings.SNOWFLAKE_WAREHOUSE)
            cursor.execute(
                f"USE WAREHOUSE {settings.SNOWFLAKE_WAREHOUSE.upper()};"
            )
            log.info("Executing query")
            cursor.execute(SQL)
            log.info("Iterating over query results")
            rows = 0
            while True:
                data = cursor.fetchmany(100_000)
                log.info("Fetched %s rows", len(data))
                if not data:
                    break
                df = pandas.DataFrame(data, columns=cursor.description)
                rows += df.shape[0]
                log.info("Have iterated over %s rows so far", rows)
            log.info("Finished query after %s", rows)


if __name__ == "__main__":
    query()
