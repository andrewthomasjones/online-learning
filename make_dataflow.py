# importing the requests library
import requests
from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials

project_id = "sandbox-vm-252402"
topic_name = "svm-data-stream"
sub_name = "svm-test-sub"
dataset_id = "stream_test"
table_id = "table1"
job_id = "df_job_4"
gs_path = "gs://dataflow-templates/latest/PubSub_Subscription_to_BigQuery"

credentials = GoogleCredentials.get_application_default()
service = build('dataflow', 'v1b3', credentials=credentials)

# data to be sent to api
data = {"jobName": job_id,
        "parameters": {
            "inputSubscription": "projects/"+ project_id +"/subscriptions/" + sub_name ,
            "outputTableSpec": project_id+":" + dataset_id + "." + table_id
            },
            "environment": { "zone": "australia-southeast1-a" }
        }

request = service.projects().templates().launch(projectId=project_id, gcsPath=gs_path, body=data)
response = request.execute()
