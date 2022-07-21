import grpc
import asyncio

import echo_pb2
import echo_pb2_grpc

from echo_pb2 import EchoRequest
from echo_pb2_grpc import EchoStub

async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = EchoStub(channel)
        request = EchoRequest(message='testing, testing, 123')
        response = await stub.Say(request)
        print (f"[!] EchoReply: {response.message}")


if __name__ == '__main__':
    asyncio.run(run())


