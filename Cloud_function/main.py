from google.cloud import compute_v1
from datetime import datetime, timedelta, timezone
import functions_framework

@functions_framework.http
def cloud_captains_vms(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    # Getting details from json inputs
    request_json = request.get_json(silent=True)
    request_args = request.args
    # passing the project_id and zone
    project_id = "lloyds-hack-grp-25"#request_json['project_name']
    zone = "asia-south1-a"#request_json['project_name']
   
    # List all instances in the specified project and zone
    compute_client = compute_v1.InstancesClient()
    # List all instances in the specified project and zone
    instances = compute_client.list(project=project_id, zone=zone)
    
    unused_instances = []
    idle_threshold_hours = 24
    for instance in instances:
        if instance.status == 'TERMINATED':
            unused_instances.append(instance.name)
        
    return 'Instance which can be migrated is {}!'.format(unused_instances)