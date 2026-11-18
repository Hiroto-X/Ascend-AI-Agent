from pathlib import Path


def program_name_normalizer(name):
    name = name.strip().lower()

    if not name.endswith(".exe"):
        name = name + ".exe"
    return (name)