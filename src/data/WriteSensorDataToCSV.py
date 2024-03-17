import csv, time
import os

csv_file = "temp.csv"


def write_to_csv(temp_readings, lux_prox, gas_poll, id):
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
    time.sleep(2)

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
