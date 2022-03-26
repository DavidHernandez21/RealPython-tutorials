import io
import json
from typing import Any


def json_encode(obj: Any, encoding: str) -> bytes:
    return json.dumps(obj, ensure_ascii=False).encode(encoding)


def json_decode(json_bytes: bytes, encoding: str) -> Any:
    tiow = io.TextIOWrapper(
        io.BytesIO(json_bytes), encoding=encoding, newline=""
    )
    obj = json.load(tiow)
    tiow.close()
    return obj