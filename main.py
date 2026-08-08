"""
Analyzes the contents of a CloudFormation ChangeSet using Amazon Bedrock
and outputs the analysis result.
"""

from changeset import get_changeset
from bedrock import invoke_bedrock
import sys

def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        print("Please specify a <ChangeSetARN>.")
        sys.exit(1)

    changeset_name = sys.argv[1]
    
    # Retrieve the CloudFormation change set
    changes = get_changeset(changeset_name)
    # Generate text using Bedrock
    answer = invoke_bedrock(changes)
    print(answer)

if __name__ == "__main__":
    main()
