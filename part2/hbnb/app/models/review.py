from __future__ import annotations

from dataclasses import dataclass
from .base_model import BaseModel


def _require_str(field_name: str, value: str, max_len: int | None = None) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    if max_len is not None and len(value) > max_len:
        raise ValueError(f"{field_name} must be at most {max_len} characters")


@dataclass
class Review(BaseModel):
    text: str = ""
    user_id: str = ""
    place_id: str = ""

    def __post_init__(self) -> None:
        _require_str("text", self.text, 500)
        _require_str("user_id", self.user_id, 64)
        _require_str("place_id", self.place_id, 64)

    def update(self, **kwargs) -> None:
        allowed = {"text"}
        for k in list(kwargs.keys()):
            if k not in allowed:
                kwargs.pop(k)

        if "text" in kwargs:
            _require_str("text", kwargs["text"], 500)

        super().update(**kwargs)

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "text": self.text,
            "user_id": self.user_id,
            "place_id": self.place_id,
        })
        return d
