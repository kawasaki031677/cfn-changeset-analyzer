"""
main.py のテストコード
"""

import sys
import pytest
from unittest.mock import patch
from main import main


@patch('main.invoke_bedrock')
@patch('main.get_changeset')
def test_main_works(mock_get_changeset, mock_invoke_bedrock):
    """main関数が正しく動作することを確認"""
    # ダミーデータを準備
    mock_get_changeset.return_value = [{"Type": "Resource"}]
    mock_invoke_bedrock.return_value = "分析結果"
    
    # テスト実行
    with patch.object(sys, 'argv', ['main.py', 'test-changeset']):
        with patch('builtins.print') as mock_print:
            main()
    
    # 結果を確認
    assert mock_print.called
    assert mock_print.call_args[0][0] == "分析結果"


def test_main_requires_argument():
    """引数がない場合、sys.exitが呼ばれることを確認"""
    with pytest.raises(SystemExit):
        with patch.object(sys, 'argv', ['main.py']):
            main()
