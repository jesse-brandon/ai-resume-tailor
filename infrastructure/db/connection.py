import os

import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv()

psycopg2.extras.register_uuid()


def get_connection():
    db_url = os.getenv("DATABASE_URL")

    if not db_url:
        raise Exception("DATABASE_URL is not set")

    return psycopg2.connect(db_url)
