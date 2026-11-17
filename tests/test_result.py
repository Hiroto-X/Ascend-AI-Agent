from controller.result import success,failure

def test_success_test():
    r=success("Pass")
    assert r=={"ok":True,"data":"Pass","error":None}

def test_failure_success():
    r=failure("something broke")
    assert r=={"ok":False,"data":None,"error":"something broke"}

def test_failure_turns_exception_into_text():
    r=failure(ValueError("bad value"))
    assert r["error"]=="bad value"