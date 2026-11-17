import pyperclip
from controller.log import get_logger
from controller.result import success,failure

logger=get_logger("clipboard")

def set_clipboard(text):
    if not isinstance(text,str):
        logger.warning(f"set refused, not text: {type(text).__name__}")
        return failure(f"clipbaord only accepts text, got: {type(text).__name__}")

    try:
        pyperclip.copy(text)
        check=pyperclip.paste()
    except pyperclip.PyperclipException as e:
        logger.error(f"set failed: {e}")
        return failure(e)

    if check!=text:
        logger.error("Clipbaord doesn't match what we wrote!")
        return failure("Clipboard doesn't match after writing")
    logger.info(f"set clipboard: {len(text) } characters")
    return success(len(text))
def get_clipboard():
    try:
        read=pyperclip.paste()
    except pyperclip.PyperclipException as e:
        logger.error(f"get failed: {e}")
        return failure(e)
    logger.info(f"get complete: {len(read)} characters")
    return success(read)