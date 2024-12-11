import sys
import os

# Add the project root directory to sys.path
project_root = os.path.dirname(os.path.abspath(__file__)) + "/../"
sys.path.append(project_root)

# Now you can import from core and other subdirectories
#from core.sensor_manager import SensorManager

# examples/example_usage.py
from core.sensor_manager import SensorManager

manager = SensorManager()

# Register sensors
gyro = manager.register_sensor("GY-521", address=0x68)
temp = manager.register_sensor("NTC103", pin=4)

# Poll sensors
print(manager.poll_all())
