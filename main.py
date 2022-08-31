import time

from src.modules.temperature_pressure_humidity.TemperaturePressureHumidity import TemperaturePressureHumidity

file_name = "temp_readings.txt"


def main():
    tmp = TemperaturePressureHumidity()
    while True:
        temp_temp = tmp.get_bme_values()
        write_to_file(temp_temp)
        time.sleep(10)


def write_to_file(temp_readings):
    with open(file_name, "a") as temp_data:
        current_time = time.asctime()
        write_text = f"{current_time}\nRaw Temperature: {temp_readings.raw_temperature:.3f}\nCPU Temperature: {temp_readings.cpu_temperature}\n" \
                     f"Raw Humidity: {temp_readings.raw_humidity:.3f}\nRaw Pressure: {temp_readings.raw_pressure:.3f}\n\n"
        temp_data.write(write_text)
        temp_data.close()


if __name__ == '__main__':
    main()
