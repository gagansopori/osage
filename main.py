import configparser

from src.modules import WARM_UP_TIME
from src.modules.data.WriteSensorDataToSqliteDB import write_to_db
from src.modules.sensors.gas_pollution.GasPollutants import GasPollutants
from src.modules.sensors.light_proximity.LightProximity import LightProximity
from src.modules.sensors.temperature_pressure_humidity.TemperaturePressureHumidity import TemperaturePressureHumidity


device_info = "device_info.ini"

def main(id):
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
            write_to_db(pres_hum, lux_prox, gas_poll, id)
        except Exception as e:
            print(f"Exception occurred during the process: {e}")


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(device_info)
    dev_id = config['DEVICE_INFO']['device_id']
    main(dev_id)
