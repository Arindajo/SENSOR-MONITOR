from core.base_sensor import BaseSensor

class NTC103Sensor(BaseSensor):
    def __init__(self, name="NTC103", pin=None):
        super().__init__(name)
        self.pin = pin  # Save the pin argument for use in other methods

    def connect(self):
        # Example initialization logic for thermistor
        if self.pin is None:
            raise ValueError("Pin must be specified for NTC103Sensor.")
        print(f"Thermistor connected to pin {self.pin}")

    def read_processed(self):
        # Mock or real implementation
        return {"temperature": 25.0}  # Example mock value
