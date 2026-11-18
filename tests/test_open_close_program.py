from pathlib import Path
from controller.open_close_program import open_program

def test_if_open_program():
    p = open_program("notepad.exe", allow_multiple=False)

    assert p["ok"] is True
    assert p["data"]["started"] is False
    assert p["data"]["already_running"] is True
    assert p["data"]["name"] == "notepad.exe"


