import pytest
import pyperclip

from controller.clipboard import set_clipboard, get_clipboard


@pytest.fixture
def keep_clipboard():
    old = pyperclip.paste()   # runs BEFORE the test: remember what you had
    yield                     # the test runs here
    pyperclip.copy(old)       # runs AFTER the test: put it back

def test_set_than_get_give_same_text(keep_clipboard):
    w=set_clipboard("hello clipboard")
    assert w["ok"] is True

    r=get_clipboard()
    assert r["ok"] is True
    assert r["data"]=="hello clipboard"

def test_set_refuses_non_text(keep_clipboard):
    set_clipboard("before")

    w=set_clipboard(1234)
    assert w["ok"] is False
    assert get_clipboard()["data"]=="before"

def test_multiline_text(keep_clipboard):
    text="This is line one\nThis is line Two"

    r=set_clipboard(text)
    assert r["ok"] is True
    assert get_clipboard()["data"]==text