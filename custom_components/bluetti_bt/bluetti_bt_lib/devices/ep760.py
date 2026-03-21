"""EP760 fields."""

from typing import List

from ..utils.commands import ReadHoldingRegisters
from ..base_devices.ProtocolV2Device import ProtocolV2Device


class EP760(ProtocolV2Device):
    def __init__(self, address: str, sn: str):
        super().__init__(address, "EP760", sn)

        # PV Solar inputs
        self.struct.add_uint_field('pv_input_power1', 1212)
        self.struct.add_decimal_field('pv_input_voltage1', 1213, 1)
        self.struct.add_decimal_field('pv_input_current1', 1214, 1)
        self.struct.add_uint_field('pv_input_power2', 1220)
        self.struct.add_decimal_field('pv_input_voltage2', 1221, 1)
        self.struct.add_decimal_field('pv_input_current2', 1222, 1)

        # Smart Meter Phase 1
        self.struct.add_uint_field('adl400_ac_input_power_phase1', 1228)
        self.struct.add_decimal_field('adl400_ac_input_voltage_phase1', 1229, 1)
        self.struct.add_uint_field('adl400_ac_input_current_phase1', 1230)

        # Grid Input
        self.struct.add_decimal_field('grid_frequency', 1300, 1)
        self.struct.add_uint_field('grid_power_phase1', 1313)
        self.struct.add_decimal_field('grid_voltage_phase1', 1314, 1)
        self.struct.add_decimal_field('grid_current_phase1', 1315, 1)

        # AC Output
        self.struct.add_decimal_field('ac_output_frequency', 1500, 1)
        self.struct.add_int_field('ac_output_power_phase1', 1510)
        self.struct.add_decimal_field('ac_output_voltage_phase1', 1511, 1)
        self.struct.add_decimal_field('ac_output_current_phase1', 1512, 1)

    @property
    def polling_commands(self) -> List[ReadHoldingRegisters]:
        return super().polling_commands + [
            ReadHoldingRegisters(1212, 3),    # PV1
            ReadHoldingRegisters(1220, 3),    # PV2
            ReadHoldingRegisters(1228, 3),    # Smart Meter P1
            ReadHoldingRegisters(1300, 1),    # Grid frequency
            ReadHoldingRegisters(1313, 3),    # Grid P1
            ReadHoldingRegisters(1500, 1),    # AC output frequency
            ReadHoldingRegisters(1510, 3),    # AC output P1
        ]
