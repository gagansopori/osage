import sqlite3
import time

from src.modules.data import INSERT_SENSOR_DATA


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