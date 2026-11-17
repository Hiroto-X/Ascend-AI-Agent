import os
from pathlib import Path
from controller.file import write_text_file, read_text_file

def test_write_and_read(tmp_path):
    file_path=os.path.join(tmp_path,"hello.txt")
    w=write_text_file(file_path,"Hello i am your agent, meow meow",sandbox=tmp_path)
    assert w["ok"] is True

    r=read_text_file(file_path,sandbox=tmp_path)
    assert r["ok"] is True
    assert r["data"]=="Hello i am your agent, meow meow"

def test_read_missing_file_fails(tmp_path):
    file_path = os.path.join(tmp_path, "missing.txt")

    r = read_text_file(file_path, sandbox=tmp_path)

    assert r["ok"] is False
    assert r["data"] is None

def test_write_outside_the_sandbox_refused(tmp_path):
    box=os.path.join(tmp_path,"box")
    outside=os.path.join(tmp_path,"outside.txt")

    r = write_text_file(outside,"Hello i am your agent",sandbox=box)
    assert r["ok"] is False
    assert os.path.exists(outside) is False

def test_dotdot_escape_is_refused(tmp_path):
    box=os.path.join(tmp_path,"box")
    sneaky=os.path.join(box,"..","outside.txt")

    r = write_text_file(sneaky,"nope",sandbox=box)
    assert r["ok"] is False
    assert os.path.exists(os.path.join(tmp_path,"outside.txt")) is False