import sqlite3

from appllication.settings import DB_PATH


class DBConnection:
    def __init__(self):
        self._connection: sqlite3.Connection | None = (
            None  # we reserve field for database connection
        )

    # None : Open a connection to an SQLite database.
    # Parameters None to disable opening transactions implicitly.

    def __enter__(self):
        self._connection = sqlite3.connect(
            DB_PATH
        )  # here we creat connection with sqlite 3 lib
        self._connection.row_factory = sqlite3.Row  # we set how will be return data
        # highly optimized sqlite3.Row type. Row provides both index-based
        # and case-insensitive name-based access to columns with almost no memory overhead.
        # It will probably be better than your
        # own custom dictionary-based approach or even a db_row based solution.
        return self._connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()  # we end connection
