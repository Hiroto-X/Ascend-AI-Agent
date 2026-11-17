import psutil 
from controller.log import get_logger
from controller.file import success, failure

logger=get_logger("processes")

def list_processes():
    try:
        found=[]
        for p in psutil.process_iter(["pid","name"]):
            found.append({"pid": p.info["pid"], "name": p.info["name"]})
    except psutil.Error as e:
        logger.error(f"List failed: {e}")
        return failure(e)

    logger.info(f"Listed {len(found) } Processes")
    return success(found)

    
def is_running(name):
    if not isinstance(name,str):
        logger.warning(f"Name must be text, got: {type(name)}")
        return failure(f"Name must be text, got: {type(name)}")

    result=list_processes()
    if result["ok"]==False:
        return result
    
    for n in result["data"]:
        if (n["name"] or " ").lower() == name:
            logger.info(f"{name}: Running")
            return success(True)
    
    logger.info(f"{name} is currently not running ")
    return success(False)

