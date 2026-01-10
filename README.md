# cfn-changeset-analyzer

CloudFormation ChangeSetの内容をAmazon Bedrockを使用して分析するツール

このツールは、AWS CloudFormation ChangeSetの変更内容をAmazon Bedrockを用いて分析した結果を出力する。

## 必要な前提条件

- Python 3.10以上
- AWS認証情報が設定されていること（AWS CLIまたは環境変数で設定）
- CloudFormationへのアクセス権限
- Bedrock APIへのアクセス権限

## セットアップ

```bash
pip3 install -r requirements.txt
```

## 使用方法

```bash
python3 main.py <ChangeSetARN>
```

例：
```bash
python3 main.py arn:aws:cloudformation:ap-northeast-1:123456789012:changeSet/abcdefg/hijklmn-opqrstu-vwxyz
```

## 出力

ツールは、ChangeSetの変更内容をBedrockで分析した結果を表示する。

### 出力例

```
## 実行時の挙動
既存のVPCリソース(MyVPC)の設定変更とSubnetリソース(PublicSubnet1)の追加が行われる。

## ユーザー影響
VPCの設定変更によりDNS解決や名前付けが有効化されるが、既存リソースへの影響はない。新しいSubnetが追加されるだけで、既存リソースの動作に変更はない。

## ロールバック時のリスク
ロールバックが必要な場合、VPCの設定変更は元に戻るが、追加されたSubnetリソースは削除される。

## 運用上の注意
情報不足。追加されるSubnetの用途やVPCの設定変更の目的が不明なため、ネットワーク構成全体への影響を評価できない。ロールバック時に削除されるSubnetにリソースが存在する場合の影響も不明。
```

## トラブルシューティング

- **認証エラーが出る場合**: AWS認証情報が正しく設定されているか確認すること
- **ChangeSetが見つからない場合**: ChangeSet ARNが正しいか、削除されていないか確認すること
- **Bedrockエラーが出る場合**: リージョンがBedrockに対応しているか確認すること

## 実行環境

- Python 3.10以上
- AWS SDK for Python (boto3)