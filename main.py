"""
CloudFormation ChangeSetの内容をAmazon Bedrockで分析し、
分析結果を出力する。
"""

from changeset import get_changeset
from bedrock import invoke_bedrock
import sys

def main():
    # コマンドライン引数をチェック
    if len(sys.argv) < 2:
        print("<ChangeSetARN>を指定してください。")
        sys.exit(1)
    
    changeset_name = sys.argv[1]
    
    # CloudFormationの変更セットを取得する
    changes = get_changeset(changeset_name)
    # Bedrockを使用してテキスト生成を行う
    answer = invoke_bedrock(changes)
    print(answer)

if __name__ == "__main__":
    main()