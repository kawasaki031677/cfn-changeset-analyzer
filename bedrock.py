"""
Bedrockを使用してテキスト生成を行う
"""

# Python外部ライブラリのインポート
import boto3
import json

def invoke_bedrock(changeset, region_name='us-east-1'):
    # Bedrockクライアントの作成
    bedrock_runtime = boto3.client("bedrock-runtime", region_name=region_name)

    # system_prompt.txt からプロンプトを読み込む
    with open('system_prompt.txt', 'r', encoding='utf-8') as f:
        system_prompt_text = f.read()

    # changesetをJSON文字列に変換
    changeset_text = json.dumps(changeset, indent=2)

    # リクエストボディを定義
    inference_config = {"maxTokens": 1000}
    messages = [{
        "role": "user",
        "content": [{"text": changeset_text}]
    }]
    system = [{"text": system_prompt_text}]

    # モデルを定義（Claude 3 Sonnet）
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

    # レスポンスを定義
    response = bedrock_runtime.converse(
        modelId=model_id,
        inferenceConfig=inference_config,
        messages=messages,
        system=system
    )
    answer = response["output"]["message"]["content"][0]["text"]

    # 生成されたテキストをコンソールに表示
    return answer