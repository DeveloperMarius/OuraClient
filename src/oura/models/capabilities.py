from dataclasses import dataclass
from enum import Enum
# Operation: GetCapabilities

class CapabilityType(Enum):

    CAP_BACKGROUND_DFU = 0
    CAP_RESEARCH_DATA = 1
    CAP_DAYTIME_HR = 2
    CAP_EXERCISE_HR = 3
    CAP_SPO2 = 4
    CAP_BUNDLING = 5
    CAP_ENCRYPTED_API = 6
    CAP_TAP_TO_TAG = 7
    CAP_RESTING_HR = 8
    CAP_APP_AUTH = 9
    CAP_BLE_MODE = 10
    CAP_REAL_STEPS = 11
    CAP_EXPERIMENTAL = 12
    CAP_CVA_PPG_SAMPLER = 13

class Capability:
    def __init__(self, capability_type: CapabilityType, value):
        self.type = capability_type
        self.value = value

@dataclass
class Capabilities:
    capabilities: []

    @staticmethod
    def from_bytes(page: int, raw: bytes) -> "Capabilities":
        # 2f -> Response Tag
        #   12 -> Size (size-2)
        #     02 -> Has to be 2
        #       02 -> page
        # 2f12020200050102020303020401050107000800
        size = int(raw[1])
        for i in range(4, size-2+4, 2):
            cap_id = raw[i]
            cap_value = raw[i+1]
            self.capabilities.append(Capability(CapabilityType.CAP_BACKGROUND_DFU, cap_value))
        if page == 0:
            return Capabilities(
                bootloader_version=(raw[8], raw[9], raw[10]),
                firmware_version=(raw[5], raw[6], raw[7]),
                api_version=(raw[2], raw[3], raw[4]),
                bluetooth_stack_version=(raw[11], raw[12], raw[13]),
                mac_address=":".join(f"{x:02x}" for x in reversed(raw[14:20]))
            )