"""AC60 fields."""

from typing import List

from ..utils.commands import ReadHoldingRegisters
from ..base_devices.ProtocolV2Device import ProtocolV2Device


class AC60(ProtocolV2Device):
    def __init__(self, address: str, sn: str):
        super().__init__(address, "AC60", sn)

        # Power IO (registers 140-147)
        self.struct.add_uint_field('dc_output_power', 140)
        self.struct.add_uint_field('ac_output_power', 142)
        self.struct.add_uint_field('dc_input_power', 144)
        self.struct.add_uint_field('ac_input_power', 146)

        # AC Input voltage
        self.struct.add_decimal_field('ac_input_voltage', 1314, 1)

        # Controls - Switch fields (2000s)
        self.struct.add_bool_field('ac_output_on_switch', 2011)
        self.struct.add_bool_field('dc_output_on_switch', 2012)
        self.struct.add_bool_field('power_lifting_on', 2021)

    @property
    def polling_commands(self) -> List[ReadHoldingRegisters]:
        return super().polling_commands + [
            ReadHoldingRegisters(140, 8),     # Power IO
            ReadHoldingRegisters(1314, 1),    # AC input voltage
            ReadHoldingRegisters(2011, 2),    # AC/DC output switches
            ReadHoldingRegisters(2021, 1),    # Power lifting
        ]

    @property
    def writable_ranges(self) -> List[range]:
        return [
            range(2011, 2013),  # AC/DC output switches
            range(2021, 2022),  # Power lifting
        ]
