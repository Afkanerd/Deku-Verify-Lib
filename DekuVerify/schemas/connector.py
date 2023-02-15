"""Database Connector"""
import logging
from contextlib import closing

from mysql.connector import connect
from peewee import MySQLDatabase

from DekuVerify.database_credentials import MySQL
from DekuVerify.main import Main

logger = logging.getLogger(__name__)

DB_PARAMS = Main.database_params

if isinstance(DB_PARAMS, MySQL):
    # MYSQL Database connection
    MYSQL_HOST = DB_PARAMS.host
    MYSQL_USER = DB_PARAMS.user
    MYSQL_PASSWORD = DB_PARAMS.password
    MYSQL_DATABASE = DB_PARAMS.database

    try:
        with closing(
            connect(user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                host=MYSQL_HOST,
                auth_plugin="mysql_native_password")
            ) as connection:
            query = f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE}"

            with closing(connection.cursor()) as cursor:
                cursor.execute(query)

    except Exception as error:
        logger.error("[!] Error creating database. See logs below")
        raise error

    try:
        db = MySQLDatabase(
            database = MYSQL_DATABASE,
            host = MYSQL_HOST,
            password = MYSQL_PASSWORD,
            user = MYSQL_USER
        )

    except Exception as error:
        raise error

else:
    raise TypeError("[!] Invalid database parameters.")
