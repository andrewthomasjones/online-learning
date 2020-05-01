#python -m venv env
#source env/bin/activate
#pip install -r requirements.txt
#export GOOGLE_APPLICATION_CREDENTIALS="/Users/andrewjones/Projects/online-learning/sandbox-vm.json"

"""Publishes multiple messages to a Pub/Sub topic with an error handler."""
import time
import datetime
import json
from google.cloud import pubsub_v1
import numpy as np

project_id = "sandbox-vm-252402"
topic_name = "svm-data-stream"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

futures = dict()

def generateSim():
  DELTA = 2
  split = 0.5
  class_names = ["A", "B"]

  cov1 = [[1, 0], [0, 1]]
  cov2 = [[1, 0], [0, 1]]

  mean1 = [DELTA, DELTA]
  mean2 = [-DELTA, -DELTA]

  if(np.random.random()<split):
      x, y = np.random.multivariate_normal(mean1, cov1, 1).T
      c = class_names[0]
  else:
      x, y = np.random.multivariate_normal(mean2, cov2, 1).T
      c = class_names[1]

  payload = {
        "x": float(x),
        "y": float(y),
        "class": str(c)
        }

  return payload

while(True):
    payload = generateSim()
    data =  json.dumps(payload)
    print(data)
    futures.update({data: None})
    # When you publish a message, the client returns a future.
    future = publisher.publish(
        topic_path,
        data=data.encode("utf-8"),
        timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        )
    # Publish failures shall be handled in the callback function.
    #print(future.result())
    # Wait for all the publish futures to resolve before exiting.
    time.sleep(.5)
