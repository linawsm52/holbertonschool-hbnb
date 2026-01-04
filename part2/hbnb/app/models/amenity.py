from __future__ import annotations

from dataclasses import dataclass
from .base_model import BaseModel


def _require_str(field_name: str, value: str, max_len: int | None = None) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    if max_len is not None and len(value) > max_len:
        raise ValueError(f"{field_name} must be at most {max_len} characters")


@dataclass
class Amenity(BaseModel):
    name: str = ""

    def __post_init__(self) -> None:
        _require_str("name", self.name, 50)

    def update(self, **kwargs) -> None:
        allowed = {"name"}
        for k in list(kwargs.keys()):
            if k not in allowed:
                kwargs.pop(k)

        if "name" in kwargs:
            _require_str("name", kwargs["name"], 50)

        super().update(**kwargs)

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({"name": self.name})
        return d
