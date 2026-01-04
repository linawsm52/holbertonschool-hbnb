from __future__ import annotations

from dataclasses import dataclass
from .base_model import BaseModel


def _require_str(field_name: str, value: str, max_len: int | None = None) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    if max_len is not None and len(value) > max_len:
        raise ValueError(f"{field_name} must be at most {max_len} characters")


@dataclass
class User(BaseModel):
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    password: str = ""

    def __post_init__(self) -> None:
        _require_str("email", self.email, 128)

    def update(self, **kwargs) -> None:
        allowed = {"first_name", "last_name", "email", "password"}
        for k in list(kwargs.keys()):
            if k not in allowed:
                kwargs.pop(k)

        if "email" in kwargs:
            _require_str("email", kwargs["email"], 128)

        super().update(**kwargs)

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        })
        return d
