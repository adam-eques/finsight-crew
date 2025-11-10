"""A very small on-disk cache so repeat tool calls are cheap."""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Optional


class DiskCache:
    def __init__(self, root: str = "data/cache", ttl: float = 86400):
        self.root = Path(root)
        self.ttl = ttl
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, key: str) -> Path:
        return self.root / f"{key}.json"

    def get(self, key: str) -> Optional[Any]:
        path = self._path(key)
        if not path.exists():
            return None
        payload = json.loads(path.read_text(encoding="utf-8"))
        if time.time() - payload["stored_at"] > self.ttl:
            return None
        return payload["value"]

    def set(self, key: str, value: Any, now: Optional[float] = None) -> None:
        payload = {"stored_at": now if now is not None else time.time(),
                   "value": value}
        self._path(key).write_text(json.dumps(payload), encoding="utf-8")


def cache_key(*parts) -> str:
    import hashlib

    raw = "|".join(str(p) for p in parts)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]
