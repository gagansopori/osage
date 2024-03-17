import configparser
from src.data.WriteSensorDataToSqliteDB import write_to_db
from src.modules.LightProximity import LightProximity
from src.modules.TemperaturePressureHumidity import TemperaturePressureHumidity

device_info = "device_info.ini"


def main(device_id):
    ctr = 0
    while True:
        pres_hum = TemperaturePressureHumidity().populate_sensor_data()
        lux_prox = LightProximity().measure_ltr559_values()
        # if ctr == WARM_UP_TIME:
        #     gas_poll = GasPollutants().fetch_gas_ppm(True)
        #     ctr = 1
        # else:
        #     gas_poll = GasPollutants().fetch_gas_ppm(False)
        #     ctr += 1

        try:
            write_to_db(pres_hum, lux_prox, device_id)
        except Exception as e:
            print(f"Exception occurred during the process: {e}")


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(device_info)
    dev_id = config['DEVICE_INFO']['device_id']
    main(dev_id)
