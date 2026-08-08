# cfn-changeset-analyzer

A tool for analyzing AWS CloudFormation ChangeSets using Amazon Bedrock

This tool outputs the results of analyzing CloudFormation ChangeSet contents using Amazon Bedrock.

## Prerequisites

- Python 3.10 or higher
- AWS credentials configured (via AWS CLI or environment variables)
- Access permissions to CloudFormation
- Access permissions to the Bedrock API

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

The tool displays the results of analyzing ChangeSet contents with Bedrock.

### Output Example

```
## Behavior at Execution
Configuration changes to the existing VPC resource (MyVPC) and addition of the Subnet resource (PublicSubnet1) will be performed.

## User Impact
DNS resolution and naming will be enabled by the VPC configuration change, but there is no impact on existing resources. Only a new Subnet will be added, with no changes to the behavior of existing resources.

## Rollback Risks
If a rollback is required, the VPC configuration changes will be reverted and the added Subnet resource will be deleted.

## Operational Notes
Insufficient information. The purpose of the added Subnet and the VPC configuration change are unclear, making it impossible to assess the overall impact on the network configuration. The impact of a rollback deleting a Subnet that contains resources is also unknown.
```

## Troubleshooting

- **Authentication errors**: Verify that your AWS credentials are correctly configured
- **ChangeSet not found**: Verify that the ChangeSet ARN is correct and has not been deleted
- **Bedrock errors**: Verify that your region supports Bedrock

## Runtime Environment

- Python 3.10 or higher
- AWS SDK for Python (boto3)
