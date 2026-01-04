from __future__ import annotations

from dataclasses import dataclass, field
from .base_model import BaseModel


def _require_str(field_name: str, value: str, max_len: int | None = None) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    if max_len is not None and len(value) > max_len:
        raise ValueError(f"{field_name} must be at most {max_len} characters")


def _require_number(field_name: str, value, min_val=None, max_val=None) -> None:
    if not isinstance(value, (int, float)):
        raise ValueError(f"{field_name} must be a number")
    if min_val is not None and value < min_val:
        raise ValueError(f"{field_name} must be >= {min_val}")
    if max_val is not None and value > max_val:
        raise ValueError(f"{field_name} must be <= {max_val}")


@dataclass
class Place(BaseModel):
    name: str = ""
    description: str = ""
    price: float = 0.0
    latitude: float = 0.0
    longitude: float = 0.0
    owner_id: str = ""
    amenity_ids: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        _require_str("name", self.name, 100)
        _require_str("owner_id", self.owner_id, 64)
        _require_number("price", self.price, 0)
        _require_number("latitude", self.latitude, -90, 90)
        _require_number("longitude", self.longitude, -180, 180)

        if not isinstance(self.amenity_ids, list) or not all(isinstance(x, str) for x in self.amenity_ids):
            raise ValueError("amenity_ids must be a list of strings")

    def add_amenity(self, amenity_id: str) -> None:
        _require_str("amenity_id", amenity_id, 64)
        if amenity_id not in self.amenity_ids:
            self.amenity_ids.append(amenity_id)
            self.touch()

    def remove_amenity(self, amenity_id: str) -> None:
        if amenity_id in self.amenity_ids:
            self.amenity_ids.remove(amenity_id)
            self.touch()

    def update(self, **kwargs) -> None:
        allowed = {"name", "description", "price", "latitude", "longitude", "owner_id", "amenity_ids"}
        for k in list(kwargs.keys()):
            if k not in allowed:
                kwargs.pop(k)

        if "name" in kwargs:
            _require_str("name", kwargs["name"], 100)
        if "owner_id" in kwargs:
            _require_str("owner_id", kwargs["owner_id"], 64)
        if "price" in kwargs:
            _require_number("price", kwargs["price"], 0)
        if "latitude" in kwargs:
            _require_number("latitude", kwargs["latitude"], -90, 90)
        if "longitude" in kwargs:
            _require_number("longitude", kwargs["longitude"], -180, 180)
        if "amenity_ids" in kwargs:
            if not isinstance(kwargs["amenity_ids"], list) or not all(isinstance(x, str) for x in kwargs["amenity_ids"]):
                raise ValueError("amenity_ids must be a list of strings")

        super().update(**kwargs)

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "amenity_ids": self.amenity_ids,
        })
        return d
