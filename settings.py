"""File with settings and configs for the project"""

from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@0.0.0.0:5434/postgres"
)  # connect string for the database
TEST_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@0.0.0.0:5435/postgres_test"
)  # connect string for the database
