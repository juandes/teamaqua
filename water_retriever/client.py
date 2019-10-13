import grpc
import fitbit
import os
import sys
import time
import logging
import app.api.v1.endpoint_pb2 as endpoint_pb2
import app.api.v1.endpoint_pb2_grpc as endpoint_pb2_grpc

from google.protobuf.timestamp_pb2 import Timestamp

waiting_time = 60 * 30


def run():
    starttime = time.time()
    # keep track of the last water consumption id
    last_log_id = 0

    client = fitbit.Fitbit(os.environ['FITBIT_KEY'], os.environ['FITBIT_SECRET'],
                           access_token=os.environ['ACCESS_TOKEN'],
                           refresh_token=os.environ['REFRESH_TOKEN'],
                           system='en_DE')

    with grpc.insecure_channel('localhost:50051') as channel:
        while True:
            print('iterating...')
            # result looks like this: {'summary': {'water': 500}, 'water': [{'amount': 500, 'logId': 6630477481}]}
            result = client.foods_log_water(date='today').get('water', None)

            print(result)
            # if no water has been consumed...
            if result is None or len(result) == 0 or result[-1]['logId'] == last_log_id:
                time.sleep(waiting_time -
                           ((time.time() - starttime) % waiting_time))
                continue

            stub = endpoint_pb2_grpc.DrinkWaterStub(channel)
            try:
                timestamp = Timestamp()
                timestamp.GetCurrentTime()
                response = stub.LogSplash(endpoint_pb2.Splash(
                    amount=result[-1]['amount'],
                    ts=timestamp
                ))
                print("Splash logged. Response: {}".format(response))
            except Exception as e:
                print(e)

            time.sleep(waiting_time -
                       ((time.time() - starttime) % waiting_time))
            print('end')
            last_log_id = result[-1]['logId']


if __name__ == '__main__':
    logging.basicConfig()
    run()
