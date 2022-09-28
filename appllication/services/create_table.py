from appllication.services.db_connection import DBConnection


def phone_table():
    with DBConnection() as connection:  # we creat connection and return it trough context manager
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS phones (
                    PhoneID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    ContactName TEXT NOT NULL,
                    PhoneValue INTEGER NOT NULL
                )
            """
            )
