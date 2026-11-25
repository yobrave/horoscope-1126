import json
import os
from pathlib import Path

MAX_LEN = 200


def check(text):
    problems = []
    if not text:
        problems.append("blank")
    if len(text) > MAX_LEN:
        problems.append(f"over {MAX_LEN}")
    return problems


def ship(text):
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    out.mkdir(parents=True, exist_ok=True)
    p = out / "entry.txt"
    p.write_text(text + "\n", encoding="utf-8")
    return p


if __name__ == "__main__":
    src = Path(__file__).resolve().with_name("entry.txt")
    line = src.read_text(encoding="utf-8").strip()
    bad = check(line)
    if bad:
        raise SystemExit("; ".join(bad))
    receipt = {"source": str(src), "output": str(ship(line)), "chars": len(line), "max": MAX_LEN}
    print(json.dumps(receipt, indent=2))
