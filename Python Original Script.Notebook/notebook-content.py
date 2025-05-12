# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

python
CopyEdit
import requests

# Replace with your real values
TENANT_ID = "your-tenant-id"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
WORKSPACE_ID = "your-fabric-workspace-id"
PIPELINE_ID = "your-deployment-pipeline-id"

# Step 1: Get access token
def get_access_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    headers = { "Content-Type": "application/x-www-form-urlencoded" }
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "https://graph.microsoft.com/.default"
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception("Failed to get access token: " + response.text)

# Step 2: Trigger Fabric pipeline
def trigger_pipeline(access_token):
    url = f"https://api.fabric.microsoft.com/v1/workspaces/{WORKSPACE_ID}/deploymentPipelines/{PIPELINE_ID}/deploy"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # You can add a specific stageId if needed, otherwise it triggers default
    response = requests.post(url, headers=headers)
    if response.status_code == 202:
        print("✅ Pipeline triggered successfully.")
    else:
        raise Exception("❌ Failed to trigger pipeline: " + response.text)

# Run it
token = get_access_token()
trigger_pipeline(token)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
