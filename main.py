import time

from src.modules.temp_pressure_humidity.BME280Measurements import TemperaturePressureHumidity

file_name = "temp_readings.txt"


def main():
    tmp = TemperaturePressureHumidity()
    while True:
        temp_temp = tmp.measure_temperature()
        write_to_file(temp_temp)
        time.sleep(10)


def write_to_file(temp_readings):
    with open(file_name, "a") as temp_data:
        current_time = time.asctime()
        write_text = f"{current_time} - Raw Temperature: {temp_readings.raw_temperature:.3f} & CPU Temperature: {temp_readings.cpu_temperature}\n"
        temp_data.write(write_text)
        temp_data.close()


if __name__ == '__main__':
    main()
