from dataclasses import dataclass
from oura.models.event import Event

@dataclass
class EventSummary(Event):
    events_received: int
    sleep_analysis_progress: int
    bytes_left: int

    @staticmethod
    def from_bytes(raw: bytes) -> "EventSummary":
        packet_length = raw[1]
        return EventSummary(
            raw=raw,
            events_received=raw[2] & 0xff,
            sleep_analysis_progress=raw[3] & 0xff if packet_length >= 2 else -1,
            bytes_left=int.from_bytes(raw[4:8], 'little') if packet_length >= 6 else -1,
        )