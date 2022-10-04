import os.path
import time, csv

from src.modules.gas_pollution.GasPollutants import GasPollutants
from src.modules.light_proximity.LightProximity import LightProximity
from src.modules.temperature_pressure_humidity.TemperaturePressureHumidity import TemperaturePressureHumidity

file_name = "temp_readings.txt"
csv_file = "temp.csv"


def main():
    if not os.path.isfile(csv_file):
        headers = [f"TimeStamp", f"BME Temp", f"CPU Temp",
                   f"TMP Temp", f"BME Humidity", f"BME Pressure",
                   f"LTR Lux", f"LTR Prox", f"Oxidizing", f"Reducing", f"Ammonia"]

        with open(csv_file, 'w') as init_csv:
            writer = csv.writer(init_csv)
            writer.writerow(headers)
            init_csv.close()

    tph = TemperaturePressureHumidity()
    lap = LightProximity()
    gpl = GasPollutants()
    while True:
        pres_hum = tph.populate_sensor_data()
        lux_prox = lap.measure_ltr559_values()
        gas_poll = gpl.measure_ads1015_values()
        # write_to_file(pres_hum, lux_prox)
        write_to_csv(pres_hum, lux_prox, gas_poll)
        time.sleep(10)


def write_to_file(temp_readings, lux_prox):
    with open(file_name, "a") as temp_data:
        current_time = time.asctime()
        write_text = f"{current_time}\nRaw Temperature: {temp_readings.raw_temperature:.3f}\n" \
                     f"CPU Temperature: {temp_readings.cpu_temperature}\nTMP36 Temperature: {temp_readings.calibrated_temperature:.3f}\n" \
                     f"Raw Humidity: {temp_readings.raw_humidity:.3f}\nRaw Pressure: {temp_readings.raw_pressure:.3f}\n" \
                     f"Current Light: {lux_prox.lux:.3f}\nCurrent Proximity: {lux_prox.proximity:.3f}\n\n"
        temp_data.write(write_text)
        temp_data.close()


def write_to_csv(temp_readings, lux_prox, gas_poll):
    current_time = time.asctime()
    row_data = [f"{current_time}", f"{temp_readings.bme_temperature:.3f}", f"{temp_readings.cpu_temperature}",
                f"{temp_readings.tmp_temperature:.3f}", f"{temp_readings.raw_humidity:.3f}",
                f"{temp_readings.raw_pressure:.3f}", f"{lux_prox.lux:.3f}", f"{lux_prox.proximity:.3f}",
                f"{gas_poll.ads_oxidizing:.3f}", f"{gas_poll.ads_reducing:.3f}", f"{gas_poll.ads_nh3ammonia:.3f}"]
    with open(csv_file, 'a') as env_data:
        writer = csv.writer(env_data)
        writer.writerow(row_data)
        env_data.close()


if __name__ == '__main__':
    main()
