import fitbit
import os

# key and secrets are kept as env variables
client = fitbit.Fitbit(os.environ['FITBIT_KEY'], os.environ['FITBIT_SECRET'],
                       access_token=os.environ['ACCESS_TOKEN'], refresh_token=os.environ['REFRESH_TOKEN'],
                       system='en_DE')



summary = client.foods_log_water(date='today')
print(summary['water'])

result = client.time_series(resource='foods/log/water', base_date='today',
                            period='1d')
print(result)
