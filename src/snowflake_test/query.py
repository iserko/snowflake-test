import logging
import logging.config

import pandas
from snowflake_test import settings
from snowflake.connector import connect

SQL = """-- Test query for snowflake-test
SELECT *
FROM lyst_analytics.raw_page_views
WHERE event_timestamp >= '2020-01-01'
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
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"USE {settings.SNOWFLAKE_WAREHOUSE};")
            cursor.execute(SQL)
            rows = 0
            while True:
                data = cursor.fetchmany(50_000)
                if not data:
                    break
                df = pandas.DataFrame(data, columns=cursor.description)
                rows += df.shape[0]
            print(rows)


if __name__ == "__main__":
    query()
