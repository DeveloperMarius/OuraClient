from dataclasses import dataclass
from oura.models.event_summary import EventSummary


@dataclass
class EventPacket:
    events: list[bytes]

    @staticmethod
    def from_bytes(raw: bytes) -> "EventPacket":
        events = []
        for i in range(0, len(raw), 20):
            event = raw[i:i + 20]
            if event[0] == 0x11:
                event_summary = EventSummary.from_bytes(event)
                events.append(event_summary)
            else:
                events.append(event)
        return EventPacket(
            events=events
        )
