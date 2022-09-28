from appllication.services.db_connection import DBConnection


def phone_table():
    with DBConnection() as connection:  # we creat connection and return it trough context manager
        with connection:  # context manager for connection for possible changes of the data
            ## table creation , if it isn't exist' (column1 datatype),
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS phones ( 
                    PhoneID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    ContactName TEXT NOT NULL,
                    PhoneValue INTEGER NOT NULL
                )
            """
            )
