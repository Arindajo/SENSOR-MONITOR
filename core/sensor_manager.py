# core/sensor_manager.py
from core.base_sensor import BaseSensor

from sensors.accel import GY521Sensor
from sensors.thermistor import NTC103Sensor

class SensorManager:
    def __init__(self):
        self.sensors = []

    def register_sensor(self, sensor_type, **kwargs):
        sensor_classes = {
            "GY-521": GY521Sensor,
            "NTC103": NTC103Sensor
        }
        if sensor_type not in sensor_classes:
            raise ValueError(f"Unsupported sensor type: {sensor_type}")

        sensor = sensor_classes[sensor_type](**kwargs)
        sensor.connect()
        self.sensors.append(sensor)
        return sensor

    def poll_all(self):
        return {sensor.name: sensor.read_processed() for sensor in self.sensors}
