from pathlib import Path


ENTRY = "I used all my tokens planning how to meet the deadline. The plan was excellent."


def write_entry() -> None:
    primary = Path("/output")
    fallback = Path.cwd() / "output"

    try:
        primary.mkdir(parents=True, exist_ok=True)
        destination = primary / "entry.txt"
        destination.write_text(ENTRY + "\n", encoding="utf-8")
    except OSError:
        fallback.mkdir(parents=True, exist_ok=True)
        destination = fallback / "entry.txt"
        destination.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_entry()
