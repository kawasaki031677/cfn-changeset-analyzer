"""
Analyzes CloudFormation ChangeSet contents using Amazon Bedrock
and outputs the analysis results.
"""

from changeset import get_changeset
from bedrock import invoke_bedrock
import sys

def main():
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Please specify <ChangeSetARN>.")
        sys.exit(1)

    changeset_name = sys.argv[1]

    # Retrieve the CloudFormation changeset
    changes = get_changeset(changeset_name)
    # Generate text using Bedrock
    answer = invoke_bedrock(changes)
    print(answer)

if __name__ == "__main__":
    main()