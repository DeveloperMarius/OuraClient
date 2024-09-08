from dataclasses import dataclass

@dataclass
class Event:
    raw: bytes

    @staticmethod
    def from_bytes(raw: bytes) -> "Event":
        return Event(
            raw=raw
        )