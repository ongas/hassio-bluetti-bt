"""EP800 fields."""

from ..base_devices.ProtocolV2Device import ProtocolV2Device


class EP800(ProtocolV2Device):
    """EP800 extends EP600 - uses same Protocol V2 structure."""
    def __init__(self, address: str, sn: str):
        super().__init__(address, "EP800", sn)
        # EP800 uses same registers as EP600 family
        # Add specific fields as discovered/documented
