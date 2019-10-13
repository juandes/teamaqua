import grpc
import app.api.v1.endpoint_pb2 as endpoint_pb2
import app.api.v1.endpoint_pb2_grpc as endpoint_pb2_grpc
import sys


with grpc.insecure_channel('localhost:50051') as channel:
    stub = endpoint_pb2_grpc.DrinkWaterStub(channel)
    print('hi')
    stub.LogSplash(endpoint_pb2.Splash(
        amount=4321
    ))

