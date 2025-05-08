# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "0d4a5a43-8347-463f-ade7-a406a7b26b4a",
# META       "default_lakehouse_name": "test",
# META       "default_lakehouse_workspace_id": "7b811294-f45e-4563-835b-b5cfa80ed6b2",
# META       "known_lakehouses": [
# META         {
# META           "id": "0d4a5a43-8347-463f-ade7-a406a7b26b4a"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

TENANT_ID = "eac95919-a7ae-4dad-9b67-43815f6dc5e1"
CLIENT_ID = "edf8cb32-5fc7-4aaf-8b85-140a93f1235b"
CLIENT_SECRET = "7ab55044-fe10-4833-b938-e242c519d43e"
WORKSPACE_ID = "daa68fe7-49a6-477b-8c2b-ef26e391a1bd"
PIPELINE_ID = "b6123a0a-4507-4b73-82ce-018b6a9ed23d"

def get_access_token():
    url = f"https://login.microsoftonline.com/eac95919-a7ae-4dad-9b67-43815f6dc5e1/oauth2/v2.0/token"
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
    url = f"https://api.fabric.microsoft.com/v1/workspaces/daa68fe7-49a6-477b-8c2b-ef26e391a1bd/deploymentPipelines/b6123a0a-4507-4b73-82ce-018b6a9ed23d/deploy"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
