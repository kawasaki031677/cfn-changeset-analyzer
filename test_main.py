"""
Test code for main.py
"""

import sys
import pytest
from unittest.mock import patch
from main import main


@patch('main.invoke_bedrock')
@patch('main.get_changeset')
def test_main_works(mock_get_changeset, mock_invoke_bedrock):
    """Verify that the main function works correctly"""
    # Prepare dummy data
    mock_get_changeset.return_value = [{"Type": "Resource"}]
    mock_invoke_bedrock.return_value = "analysis result"

    # Run test
    with patch.object(sys, 'argv', ['main.py', 'test-changeset']):
        with patch('builtins.print') as mock_print:
            main()

    # Verify result
    assert mock_print.called
    assert mock_print.call_args[0][0] == "analysis result"


def test_main_requires_argument():
    """Verify that sys.exit is called when no argument is provided"""
    with pytest.raises(SystemExit):
        with patch.object(sys, 'argv', ['main.py']):
            main()
