from flask import Flask, Response
from webargs import fields  # creation Custom Fields  Using the
# Method and Function fields requires that you pass the deserialize parameter
from webargs.flaskparser import use_args  # parsed arguments dictio

from appllication.services import DBConnection
from appllication.services import phone_table

# nary will be injected as a parameter of your view function or as keyword arguments, respectively.

app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return "Hi World!"


@app.route("/phones/create")
@use_args(
    {"ContactName": fields.Str(required=True), "PhoneValue": fields.Int(required=True)},
    location="query",
)
def phones_create(args):
    with DBConnection() as connection:  # we connect to database (its our context manager).
        # For every action we creat new connection and than it close according with DBconnection  class
        with connection:  # to save our chages ( using context manager)
            # and request itsself
            connection.execute(
                "INSERT INTO phones (ContactName, PhoneValue) VALUES (:ContactName, :PhoneValue);",
                {"ContactName": args["ContactName"], "PhoneValue": args["PhoneValue"]},
            )

    return "Ok"


@app.route("/phones/update/<int:pk>")
@use_args(
    {"PhoneValue": fields.Int(), "ContactName": fields.Str()}, location="query"
)  # optional arguments here,
# with change of one, second should be change
# thats why we dont put requerements
def phones__update(
    args,
    pk: int,
):
    with DBConnection() as connection:
        with connection:
            ContactName = args.get(
                "ContactName"
            )  # here we get our value, through get ,
            # for if there is no value will return none
            PhoneValue = args.get("PhoneValue")
            if (
                ContactName is None and PhoneValue is None
            ):  # if both values is one will get message below
                # Response should be imported (flask)< autmat message
                return Response(
                    "Need to provide at least one argument",
                    status=400,
                )

            args_for_request = []
            if ContactName is not None:
                args_for_request.append("ContactName=:ContactName")
            if PhoneValue is not None:
                args_for_request.append("PhoneValue=:PhoneValue")

            args_2 = ", ".join(args_for_request)
            # if all ok we rassembler part for request
            connection.execute(
                "UPDATE phones " f"SET {args_2} " "WHERE PhoneID=:PhoneID;",
                {
                    "PhoneID": pk,
                    "PhoneValue": PhoneValue,
                    "ContactName": ContactName,
                },
            )

    return "Ok"


@app.route("/phones/delete/<int:pk>")
def phones__delete(pk):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "DELETE " "FROM phones " "WHERE (PhoneID=:PhoneID);",
                {
                    "PhoneID": pk,
                },
            )

    return "Ok"


@app.route("/phones/read-all")
def phones__read_all():
    with DBConnection() as connection:
        phones = connection.execute("SELECT * FROM phones;").fetchall()

    return "<br>".join(
        [
            f'{user["PhoneID"]}: {user["ContactName"]} - {user["PhoneValue"]}'
            for user in phones
        ]
    )  # "USER" SHOULD BE NT CHANGE


@app.route("/phones/read/<int:pk>")
def users__read(pk: int):  # PK SHOULD NOT BE CHANGE
    with DBConnection() as connection:
        user = connection.execute(
            "SELECT * " "FROM phones " "WHERE (PhoneID=:PhoneID);",
            {
                "PhoneID": pk,
            },  # PK SHOULD NOT BE CHANGE
        ).fetchone()

    return f'{user["PhoneID"]}: {user["ContactName"]} - {user["PhoneValue"]}'  # "USER" SHOULD BE NT CHANGE


phone_table()


if __name__ == "__main__":
    app.run()
