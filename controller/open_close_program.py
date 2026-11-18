import subprocess
from controller.result import success, failure
from controller.log import get_logger
from controller.processes import is_running
from controller.processes import list_processes
from controller.helper_functions import program_name_normalizer

logger = get_logger("open_close_program")

PROGRAMS = ("powershell.exe", "cmd.exe")


def open_program(name, allow_multiple = False):

    name = program_name_normalizer(name)
    if name in PROGRAMS:
        logger.warning(f"launch failed: program not allowed {name}")
        return failure(f"launch failed: program not allowed {name}")
        
    r = is_running(name)
    before = r["data"]["pids"]
    if not allow_multiple and before:
        return success({"started": False, "already_running": True, "pid": sorted(before), "name":name})
    try:
           
        p = subprocess.Popen([name])
        logger.info(f"Successfully opened program: {name} with pid {p.pid}")
        return success({"started": True, "pid": p.pid, "name": name})

    

    except OSError as e:
        logger.error(e)
        return failure(f"launch failed: {type(e).__name__}: {e}")    

    

 


