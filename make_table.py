from google.cloud import bigquery

project_id = "sandbox-vm-252402"
dataset_id = "stream_test2"
table_id = "table1"


# Construct a BigQuery client object.
client = bigquery.Client()


# TODO(developer): Set dataset_id to the ID of the dataset to create.
dataset_name = project_id + "." + dataset_id

# Construct a full Dataset object to send to the API.
dataset = bigquery.Dataset(dataset_name)

# TODO(developer): Specify the geographic location where the dataset should reside.
dataset.location = "US"

# Send the dataset to the API for creation.
# Raises google.api_core.exceptions.Conflict if the Dataset already
# exists within the project.
dataset = client.create_dataset(dataset)  # Make an API request.
print("Created dataset {}.{}".format(client.project, dataset.dataset_id))



table_name = project_id + "." + dataset_id + "." + table_id

schema = [
    bigquery.SchemaField("x", "FLOAT", mode="REQUIRED"),
    bigquery.SchemaField("y", "FLOAT", mode="REQUIRED"),
    bigquery.SchemaField("class", "String", mode="REQUIRED"),
]

table = bigquery.Table(table_name, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)
