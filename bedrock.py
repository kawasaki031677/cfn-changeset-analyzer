"""
Generates text using Bedrock
"""

# Import external Python libraries
import boto3
import json

def invoke_bedrock(changeset, region_name='us-east-1'):
    # Create a Bedrock client
    bedrock_runtime = boto3.client("bedrock-runtime", region_name=region_name)

    # Load the prompt from system_prompt.txt
    with open('system_prompt.txt', 'r', encoding='utf-8') as f:
        system_prompt_text = f.read()

    # Convert the changeset to a JSON string
    changeset_text = json.dumps(changeset, indent=2)

    # Define the request body
    inference_config = {"maxTokens": 1000}
    messages = [{
        "role": "user",
        "content": [{"text": changeset_text}]
    }]
    system = [{"text": system_prompt_text}]

    # Define the model (Claude 3 Sonnet)
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

    # Get the response
    response = bedrock_runtime.converse(
        modelId=model_id,
        inferenceConfig=inference_config,
        messages=messages,
        system=system
    )
    answer = response["output"]["message"]["content"][0]["text"]

    # Return the generated text
    return answer
