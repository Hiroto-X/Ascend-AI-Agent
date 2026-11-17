import logging
from pathlib import Path

# The logs folder sits next to the controller folder, at the project root.
LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_FILE = LOG_DIR / "agent.log"


def get_logger(name="controller"):
    """Return a logger that writes to the console and to logs/agent.log."""
    logger = logging.getLogger(name)

    # If this logger is already set up, reuse it.
    # Without this check, every call would add another handler
    # and each message would be printed twice, then three times...
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False  # don't pass messages up to the root logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    LOG_DIR.mkdir(exist_ok=True)

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger