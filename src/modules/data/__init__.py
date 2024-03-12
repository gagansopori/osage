
INSERT_SENSOR_DATA = """INSERT INTO sensor_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""

INSERT_BASIC_SENSOR_DATA = """INSERT INTO sensor_data (device_id, create_ts, cpu_temp, bme_temp, bme_humid, bme_pres, 
ltr_lux, ltr_prox) VALUES (?,?,?,?,?,?,?,?); """
