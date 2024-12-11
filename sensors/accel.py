from core.base_sensor import BaseSensor
import platform

if platform.system() == "Windows":
    class SMBus:
        def __init__(self, bus):
            pass

        def write_byte_data(self, addr, reg, value):
            pass

        def read_byte_data(self, addr, reg):
            return 0

        def read_i2c_block_data(self, addr, reg, length):
            return [0] * length
else:
    from smbus2 import SMBus

from core.base_sensor import BaseSensor
import platform

if platform.system() == "Windows":
    class SMBus:
        def __init__(self, bus):
            pass

        def write_byte_data(self, addr, reg, value):
            pass

        def read_byte_data(self, addr, reg):
            return 0

        def read_i2c_block_data(self, addr, reg, length):
            return [0] * length
else:
    from smbus2 import SMBus

class GY521Sensor(BaseSensor):
    def __init__(self, name="GY-521", address=0x68):
        super().__init__(name)
        self.bus = SMBus(1)  # Use mock SMBus on Windows or real SMBus on Linux
        self.address = address

    def connect(self):
        # Example initialization logic
        self.bus.write_byte_data(self.address, 0x6B, 0)

    def read_processed(self):
        # Mock or real implementation
        return {"x": 0, "y": 0, "z": 0}
