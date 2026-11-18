import psutil 
from controller.log import get_logger
from controller.file import success, failure
from controller.helper_functions import program_name_normalizer

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

def find_pids(name):
    result = list_processes()

    if result["ok"] is False:
        return None
    
def is_running(name):
    if not isinstance(name,str):
        logger.warning(f"Name must be text, got: {type(name)}")
        return failure(f"Name must be text, got: {type(name)}")

    result=list_processes()
    if result["ok"]==False:
        return result
    name = program_name_normalizer(name)
    pids = []
    for n in result["data"]:
        if (n["name"] or " ").lower() == name:
            pids.append(n["pid"])
    if not pids:        
        logger.info(f"{name} is currently not running ")
        return success({"is_running": False, "name": name})
    
    logger.info(f"{name}: Running")
    return success({"is_running": True, "name": name, "pids": pids})

