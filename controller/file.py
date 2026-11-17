
from pathlib import Path
from controller.result import success,failure
from controller.log import get_logger

logger=get_logger("file")

Sandbox=Path(__file__).resolve().parent.parent/"test_sandbox"

def check_path(path,sandbox=Sandbox):
    sandbox=Path(sandbox).resolve()
    resolved=Path(path).resolve()
    if resolved==sandbox.resolve() or sandbox.resolve() in resolved.parents:
        return resolved
    else:
        return None

def write_text_file(path, text, sandbox=Sandbox):
    safe=check_path(path, sandbox)
    if safe==None:
        logger.warning(f"Writing failed, out of sandbox: {path}")
        return failure(f"Path is outside the sandbox: {path}")
    try:
        safe.parent.mkdir(parents=True,exist_ok=True)
        safe.write_text(text,encoding="utf-8")
    except OSError as e:
        logger.error(f"Write failed: {path}, {e}")
        return failure(e)
    logger.info(f"wrote {len(text)} characters in {safe}")
    return success(text)

def read_text_file(path, sandbox=Sandbox):
    safe=check_path(path, sandbox)
    if safe==None:
        logger.warning(f"Reading failed, out of sandbox: {path}")
        return failure(f"Path is outside the sandbox: {path}")
    try:
        text=safe.read_text()
    except OSError as e:
        logger.error(f"read failed: {path}, {e}")
        return failure(e)
    logger.info(f"Read {len(text)} from {safe}")
    return success(text)


   

    
    


    


