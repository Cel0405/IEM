DROP TABLE IF EXISTS unit;
DROP TABLE IF EXISTS measurement;

CREATE TABLE unit (
  id INTEGER PRIMARY KEY,
  name VARCHAR(30) UNIQUE NOT NULL
);

INSERT INTO unit (id, name) VALUES (1, 'Stue');

CREATE TABLE measurement (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  unit_id INTEGER NOT NULL,
  registered VARCHAR(30) NOT NULL,
  bmp280_temperature FLOAT NOT NULL,
  bmp280_pressure FLOAT NOT NULL,
  si7021_temperature FLOAT NOT NULL,
  si7021_humidity FLOAT NOT NULL,
  ccs811_tvoc FLOAT NOT NULL,
  sds011_dust FLOAT NOT NULL,
  created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (unit_id) REFERENCES unit (id)
);

CREATE INDEX
  ix_measurements_unit_id_registered ON measurement (unit_id, registered);
