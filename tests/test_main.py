import pytest
from main import say_hello, sum

def test_say_hello(capsys):
    say_hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
