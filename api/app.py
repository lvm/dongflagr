from grpc import aio
from os import environ as env

from flask import Flask
from flask import jsonify
from flask import request

from echo_pb2 import EchoRequest
from echo_pb2_grpc import EchoStub


app = Flask(__name__)

ECHO_HOST = env.get("ECHO_HOST", "localhost")


@app.route("/")
def index() -> str:
    return jsonify(status="operational")


@app.route("/echo/", methods=["POST"])
async def echo() -> str:
    data = request.get_json()
    async with aio.insecure_channel(f"{ECHO_HOST}:50051") as channel:
        stub = EchoStub(channel)
        response = await stub.Say(
            EchoRequest(message=data.get("message", ""))
        )

        return jsonify(message=response.message)
