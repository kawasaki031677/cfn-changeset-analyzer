"""
Generates text using Bedrock
"""

# Import external libraries
import boto3
import json

def invoke_bedrock(changeset, region_name='us-east-1'):
    # Create Bedrock client
    bedrock_runtime = boto3.client("bedrock-runtime", region_name=region_name)

    # Load prompt from system_prompt.txt
    with open('system_prompt.txt', 'r', encoding='utf-8') as f:
        system_prompt_text = f.read()

    # Convert changeset to JSON string
    changeset_text = json.dumps(changeset, indent=2)

    # Define request body
    inference_config = {"maxTokens": 1000}
    messages = [{
        "role": "user",
        "content": [{"text": changeset_text}]
    }]
    system = [{"text": system_prompt_text}]

    # Define model (Claude 3 Sonnet)
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

    # Define response
    response = bedrock_runtime.converse(
        modelId=model_id,
        inferenceConfig=inference_config,
        messages=messages,
        system=system
    )
    answer = response["output"]["message"]["content"][0]["text"]

    # Return generated text
    return answer