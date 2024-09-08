from dataclasses import dataclass

@dataclass
class BatteryInfo:
    battery_level: int
    charging_progress: int
    charging_recommendation: int 

    @staticmethod
    def from_bytes(raw: bytes) -> "BatteryInfo":
        # Trailing zeros might be stripped by start_notify.
        raw = raw + bytearray([0] * (5 - len(raw)))
        return BatteryInfo(
            battery_level= raw[2],
            charging_progress=raw[3],
            charging_recommendation=raw[4], 
        )