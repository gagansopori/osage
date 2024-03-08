# # We create a database here along with a device id.
# # If there is anything else that needs initializing, we do it here.
# import os.path
# import sqlite3
# import time
# import uuid
# from configparser import ConfigParser
# import platform
#
# device_info = "device_info.ini"
# fetch_all_tables = """SELECT name FROM sqlite_master WHERE type='table';"""
#
#
# class DeviceInfo:
#     def __init__(self):
#         if not os.path.isfile(device_info):
#             print(f"No config file found. Creating a config file now.")
#             self._init_device()
#         else:
#             print(f"Config file found. Reading and applying configurations.")
#             self._init_device(device_info)
#
#     def _init_device(self, file_name=None) -> None:
#         if not file_name:
#             config = self._add_config()
#             with open(device_info, 'w') as config_file:
#                 config.write(config_file)
#         time.sleep(5)
#
#     def _add_config(self) -> ConfigParser:
#         config = ConfigParser()
#         config['DEVICE_INFO'] = {
#             'device_id': uuid.getnode(),
#             'hostname': platform.node()
#         }
#         return config
#
#
# class DatabaseInfo:
#     def __init__(self):
#         self._init_db("osage.db")
#
#     def _init_db(self, db) -> None:
#         try:
#             connection = sqlite3.connect(db)
#             with connection:
#                 cursor = connection.cursor()
#                 result = cursor.execute(fetch_all_tables).fetchall()
#
#                 if len(result) == 0:
#                     print(f"No Table found in Osage's Database. Configuring DB now...")
#
#                 # Sensor Data
#                 cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data(
#                                     device_id TEXT,
#                                     create_ts timestamp PRIMARY KEY,
#                                     cpu_temp REAL,
#                                     bme_temp REAL,
#                                     analog_temp REAL,
#                                     bme_humid REAL,
#                                     bme_pres REAL,
#                                     ltr_lux REAL,
#                                     ltr_prox REAL,
#                                     gas_oxi REAL,
#                                     gas_red REAL,
#                                     gas_nh3 REAL,
#                                     oxi_ppm REAL,
#                                     red_ppm REAL,
#                                     nh3_ppm REAL);''')
#         except sqlite3.OperationalError as oe:
#             print(f"Operational Error occurred: {oe}")
#         except sqlite3.IntegrityError as ie:
#             print(f"Integrity Error occurred: {ie}")
#         except sqlite3.ProgrammingError as pe:
#             print(f"Programming Error occurred: {pe}")
#         finally:
#             connection.close()
#
#
# DeviceInfo()
# DatabaseInfo()