from my_ya import create_folder
import pytest

def test_ya():
    expected = (201, 409)
    result = create_folder('Enter your Ya token', 'Enter the name of folder')
    assert result in expected 