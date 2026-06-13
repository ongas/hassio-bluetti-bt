"""AC70P fields."""

from typing import List

from ..field_enums import ChargingMode, EcoShutdown
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

        # Controls - Switch fields (2000s)
        self.struct.add_bool_field('ac_output_on_switch', 2011)
        self.struct.add_bool_field('dc_output_on_switch', 2012)
        
        # ECO mode DC
        self.struct.add_bool_field('eco_on', 2014)
        self.struct.add_enum_field('eco_shutdown', 2015, EcoShutdown)
        
        # ECO mode AC
        self.struct.add_bool_field('eco_on_ac', 2017)
        self.struct.add_enum_field('eco_shutdown_ac', 2018, EcoShutdown)
        
        # Charging mode and power lifting
        self.struct.add_enum_field('charging_mode', 2020, ChargingMode)
        self.struct.add_bool_field('power_lifting_on', 2021)

    @property
    def polling_commands(self) -> List[ReadHoldingRegisters]:
        return super().polling_commands + [
            ReadHoldingRegisters(140, 8),     # Power IO
            ReadHoldingRegisters(1213, 2),    # DC input voltage, current
            ReadHoldingRegisters(1300, 1),    # AC input frequency
            ReadHoldingRegisters(1314, 2),    # AC input voltage, current
            ReadHoldingRegisters(1500, 1),    # AC output frequency
            ReadHoldingRegisters(1511, 1),    # AC output voltage
            ReadHoldingRegisters(2011, 2),    # AC/DC output switches
            ReadHoldingRegisters(2014, 2),    # ECO DC mode
            ReadHoldingRegisters(2017, 2),    # ECO AC mode
            ReadHoldingRegisters(2020, 2),    # Charging mode, power lifting
        ]

    @property
    def writable_ranges(self) -> List[range]:
        return [
            range(2011, 2022),  # All control registers
        ]
