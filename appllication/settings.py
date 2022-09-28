import pathlib  # to creat route to our future database file

ROOT_PATH = pathlib.Path(__file__).parents[1]
DB_PATH = ROOT_PATH.joinpath("db", "db.sqlite")
