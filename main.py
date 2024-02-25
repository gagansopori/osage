import configparser
import os.path
import sqlite3
import time, csv

from src import device_info
from src.modules import WARM_UP_TIME
from src.modules.data import INSERT_SENSOR_DATA
from src.modules.gas_pollution.GasPollutants import GasPollutants
from src.modules.gas_pollution.GasPollutionModel import GasPollutionModel
from src.modules.light_proximity.LightProximity import LightProximity
from src.modules.temperature_pressure_humidity.TemperaturePressureHumidity import TemperaturePressureHumidity

file_name = "temp_readings.txt"
csv_file = "temp.csv"


def main(id):
    if not os.path.isfile(csv_file):
        headers = [f"TimeStamp", f"BME Temp", f"CPU Temp",
                   f"TMP Temp", f"BME Humidity", f"BME Pressure",
                   f"LTR Lux", f"LTR Prox",
                   f"Oxidizing", f"Reducing", f"Ammonia",
                   f"Oxidizing (ppm)", f"Reducing (ppm)", f"Ammonia (ppm)"
                   ]

        with open(csv_file, 'w') as init_csv:
            writer = csv.writer(init_csv)
            writer.writerow(headers)
            init_csv.close()

    tph = TemperaturePressureHumidity()
    lap = LightProximity()
    gpl = GasPollutants()
    ctr = 0
    while True:
        pres_hum = tph.populate_sensor_data()
        lux_prox = lap.measure_ltr559_values()
        if ctr == WARM_UP_TIME:
            gas_poll = gpl.fetch_gas_ppm(True)
            ctr = 1
        else:
            gas_poll = gpl.fetch_gas_ppm(False)
            ctr += 1
        # write_to_csv(pres_hum, lux_prox, gas_poll)
        write_to_db(pres_hum, lux_prox, gas_poll, id)


def write_to_db(temp_readings, lux_prox, gas_poll, id):
    current_time = time.asctime()
    row_data = (f"{id}",
                f"{current_time}",
                f"{temp_readings.cpu_temperature}",
                f"{temp_readings.bme_temperature:.3f}",
                f"{temp_readings.tmp_temperature:.3f}",
                f"{temp_readings.raw_humidity:.3f}",
                f"{temp_readings.raw_pressure:.3f}",
                f"{lux_prox.lux:.3f}",
                f"{lux_prox.proximity:.3f}",
                f"{gas_poll.ads_oxidizing:.3f}",
                f"{gas_poll.ads_reducing:.3f}",
                f"{gas_poll.ads_nh3ammonia:.3f}",
                f"{gas_poll.oxidizing_ppm:.3f}",
                f"{gas_poll.reducing_ppm:.3f}",
                f"{gas_poll.nh3ammonia_ppm:.3f}"
                )
    try:
        connection = sqlite3.connect("osage.db")
        with connection:
            cursor = connection.cursor()
            cursor.execute(INSERT_SENSOR_DATA, row_data)
    except sqlite3.Error as e:
        print(f"Error occurred inserting data into table sensor: {e}")
    finally:
        connection.close()

    time.sleep(2)


def write_to_csv(temp_readings, lux_prox, gas_poll, id):
    current_time = time.asctime()
    row_data = (f"{id}",
                f"{current_time}",
                f"{temp_readings.cpu_temperature}",
                f"{temp_readings.bme_temperature:.3f}",
                f"{temp_readings.tmp_temperature:.3f}",
                f"{temp_readings.raw_humidity:.3f}",
                f"{temp_readings.raw_pressure:.3f}",
                f"{lux_prox.lux:.3f}",
                f"{lux_prox.proximity:.3f}",
                f"{gas_poll.ads_oxidizing:.3f}",
                f"{gas_poll.ads_reducing:.3f}",
                f"{gas_poll.ads_nh3ammonia:.3f}",
                f"{gas_poll.oxidizing_ppm:.3f}",
                f"{gas_poll.reducing_ppm:.3f}",
                f"{gas_poll.nh3ammonia_ppm:.3f}"
                )
    with open(csv_file, 'a') as env_data:
        writer = csv.writer(env_data)
        writer.writerow(row_data)
        env_data.close()


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(device_info)
    dev_id = config['DEVICE_INFO']['device_id']
    main(dev_id)
