"""
CloudFormationの変更セットを取得する
"""

import boto3
import json

def get_changeset(changeset_name, region_name=None):
    client = boto3.client('cloudformation', region_name=region_name)
    response = client.describe_change_set(
        ChangeSetName=changeset_name
    )
    return response['Changes']