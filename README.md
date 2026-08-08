# cfn-changeset-analyzer

A tool that analyzes the contents of a CloudFormation ChangeSet using Amazon Bedrock

This tool outputs the results of analyzing the changes in an AWS CloudFormation ChangeSet using Amazon Bedrock.

## Prerequisites

- Python 3.10 or later
- AWS credentials configured (via AWS CLI or environment variables)
- Permission to access CloudFormation
- Permission to access the Bedrock API

## Setup

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
python3 main.py <ChangeSetARN>
```

Example:
```bash
python3 main.py arn:aws:cloudformation:ap-northeast-1:123456789012:changeSet/abcdefg/hijklmn-opqrstu-vwxyz
```

## Output

The tool displays the results of analyzing the ChangeSet's changes with Bedrock.

### Example output

```
## Behavior at execution time
The settings of the existing VPC resource (MyVPC) will be changed, and a Subnet resource (PublicSubnet1) will be added.

## User impact
The VPC configuration change enables DNS resolution and hostnames, but there is no impact on existing resources. Only a new Subnet is added; there is no change to the behavior of existing resources.

## Risk on rollback
If a rollback is required, the VPC configuration change will be reverted, but the added Subnet resource will be deleted.

## Operational notes
Insufficient information. The purpose of the added Subnet and the reason for the VPC configuration change are unknown, so the impact on the overall network configuration cannot be assessed. The impact is also unknown if resources exist in the Subnet that would be deleted on rollback.
```

## Troubleshooting

- **If you get an authentication error**: Check that your AWS credentials are configured correctly
- **If the ChangeSet cannot be found**: Check that the ChangeSet ARN is correct and has not been deleted
- **If you get a Bedrock error**: Check that the region supports Bedrock

## Runtime environment

- Python 3.10 or later
- AWS SDK for Python (boto3)
