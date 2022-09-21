import time

from src.modules.light_proximity.LightProximity import LightProximity
from src.modules.temperature_pressure_humidity.TemperaturePressureHumidity import TemperaturePressureHumidity

file_name = "temp_readings.txt"


def main():
    tph = TemperaturePressureHumidity()
    lap = LightProximity()
    while True:
        pres_hum = tph.measure_bme280_values()
        lux_prox = lap.measure_ltr559_values()
        write_to_file(pres_hum, lux_prox)
        time.sleep(10)


def write_to_file(temp_readings, lux_prox):
    with open(file_name, "a") as temp_data:
        current_time = time.asctime()
        write_text = f"{current_time}\nRaw Temperature: {temp_readings.raw_temperature:.3f}\nCPU Temperature: {temp_readings.cpu_temperature}\n" \
                     f"Raw Humidity: {temp_readings.raw_humidity:.3f}\nRaw Pressure: {temp_readings.raw_pressure:.3f}\n" \
                     f"Current Light: {lux_prox.lux:.3f}\nCurrent Proximity: {lux_prox.proximity:.3f}\n\n"
        temp_data.write(write_text)
        temp_data.close()


if __name__ == '__main__':
    main()
