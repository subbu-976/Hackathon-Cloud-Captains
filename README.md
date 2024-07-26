## Hackathon-Cloud-Captains

Cloud function(runtime as Python 3.12) is used to identify the servers which are unused. There are 2 files involved for the same and the details are as follows:
1) Hackathon-Cloud-Captains\Cloud_function\main.py: Which have function used to gather the information
2) Hackathon-Cloud-Captains\Cloud_function\requirements.txt: Which have details of version to improted for respective modules.

# Cloud Function url: https://us-central1-lloyds-hack-grp-25.cloudfunctions.net/cloud-captains-function

# Inputs

Input 1: "project_name":"gcp"
Input 2: "zone":"us-east"

# Output

Instance which can be migrated is <Instance name>

# Curl url

curl -X POST "https://us-central1-lloyds-hack-grp-25.cloudfunctions.net/cloud-captains-function" -H "Content-Type: application/json" --data '{"project_name":"gcp","zone":"us-east"}'

