from dataclasses import dataclass

# Operation: GetFirmwareVersion

@dataclass
class VersionInfo:
    bootloader_version: tuple[int, int, int] # (8, 9, 10)
    firmware_version: tuple[int, int, int] # (5, 6, 7)
    api_version: tuple[int, int, int] # (2, 3, 4)
    bluetooth_stack_version: tuple[int, int, int] # (11, 12, 13)
    mac_address: str

    @staticmethod
    def from_bytes(raw: bytes) -> "VersionInfo":
        return VersionInfo(
            bootloader_version=(raw[8], raw[9], raw[10]),
            firmware_version=(raw[5], raw[6], raw[7]),
            api_version=(raw[2], raw[3], raw[4]),
            bluetooth_stack_version=(raw[11], raw[12], raw[13]),
            mac_address=":".join(f"{x:02x}" for x in reversed(raw[14:20]))
        )