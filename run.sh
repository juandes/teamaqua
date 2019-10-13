#!/usr/bin/env bash

echo "Starting Server"
screen -d -m build/startserver --gcp-project=$GCP_PROJECT --bq-dataset=$BQ_DATASET --bq-table=$BQ_TABLE

echo "Starting Reminder"
screen -d -m build/reminder --project-id=$GCP_PROJECT --token=$FB_TOKEN --google-credentials=secrets/teamaqua.json 

screen -list

echo "Starting Water Retriever"
python3 water_retriever/client.py
