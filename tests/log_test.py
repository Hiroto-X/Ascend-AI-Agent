from controller.log import get_logger, LOG_FILE


def test_get_logger_does_not_duplicate_handlers():
    a = get_logger("test_dup")
    count = len(a.handlers)
    b = get_logger("test_dup")
    assert a is b
    assert len(b.handlers) == count


def test_logger_writes_to_file():
    logger = get_logger("test_file")
    logger.info("unique-marker-12345")
    text = LOG_FILE.read_text(encoding="utf-8")
    assert "unique-marker-12345" in text
