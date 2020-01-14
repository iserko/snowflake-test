from environs import Env

env = Env()
env.read_env()

SNOWFLAKE_USER = env("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = env("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = env("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_DATABASE = env("SNOWFLAKE_DATABASE")
SNOWFLAKE_WAREHOUSE = env("SNOWFLAKE_WAREHOUSE")

LOG_FORMAT = (
    "%(asctime)s %(name)s {%(module)s:%(lineno)d} %(levelname)s - %(message)s"
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": LOG_FORMAT, "class": "logging.Formatter"}
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "standard",
        }
    },
    "loggers": {
        "snowflake_test": {"level": "INFO"},
        "snowflake.sqlalchemy": {"level": "DEBUG"},
        "snowflake.connector": {"level": "DEBUG"},
        "botocore": {"level": "DEBUG"},
        "": {"handlers": ["console"], "level": "WARNING"},
    },
}
