"""AC70P fields."""

from typing import List

from ..utils.commands import ReadHoldingRegisters
from ..base_devices.ProtocolV2Device import ProtocolV2Device


class AC70P(ProtocolV2Device):
    def __init__(self, address: str, sn: str):
        super().__init__(address, "AC70P", sn)

        # Power IO (registers 140-147)
        self.struct.add_uint_field('dc_output_power', 140)
        self.struct.add_uint_field('ac_output_power', 142)
        self.struct.add_uint_field('dc_input_power', 144)
        self.struct.add_uint_field('ac_input_power', 146)

        # DC Input Details (1200s)
        self.struct.add_decimal_field('dc_input_voltage', 1213, 1)
        self.struct.add_decimal_field('dc_input_current', 1214, 1)

        # AC Input Details (1300s)
        self.struct.add_decimal_field('ac_input_frequency', 1300, 1)
        self.struct.add_decimal_field('ac_input_voltage', 1314, 1)
        self.struct.add_decimal_field('ac_input_current', 1315, 1)

        # AC Output Details (1500s)
        self.struct.add_decimal_field('ac_output_frequency', 1500, 1)
        self.struct.add_decimal_field('ac_output_voltage', 1511, 1)

    @property
    def polling_commands(self) -> List[ReadHoldingRegisters]:
        return super().polling_commands + [
            ReadHoldingRegisters(140, 8),     # Power IO
            ReadHoldingRegisters(1213, 2),    # DC input voltage, current
            ReadHoldingRegisters(1300, 1),    # AC input frequency
            ReadHoldingRegisters(1314, 2),    # AC input voltage, current
            ReadHoldingRegisters(1500, 1),    # AC output frequency
            ReadHoldingRegisters(1511, 1),    # AC output voltage
        ]
