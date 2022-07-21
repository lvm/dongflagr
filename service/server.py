import grpc
import asyncio

from echo_pb2 import EchoRequest
from echo_pb2 import EchoReply

import echo_pb2_grpc


class Echo(echo_pb2_grpc.EchoServicer):
    async def Say(
        self, request: EchoRequest, context: grpc.aio.ServicerContext
    ) -> EchoReply:
        if not request.message:
            context.abort(grpc.StatusCode.NOT_FOUND, "...Is anybody out there?")

        return EchoReply(message=request.message)


async def serve():
    server = grpc.aio.server()
    echo_pb2_grpc.add_EchoServicer_to_server(Echo(), server)

    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
