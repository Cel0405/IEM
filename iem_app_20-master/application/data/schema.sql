DROP TABLE IF EXISTS unit;
DROP TABLE IF EXISTS measurement;

CREATE TABLE unit (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

INSERT INTO unit (name) VALUES ('Stue');

CREATE TABLE measurement (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  unit_id INTEGER NOT NULL,
  registered TEXT NOT NULL, 
  bmp280_temperature NUMBER NOT NULL,
  bmp280_pressure NUMBER NOT NULL, 
  si7021_temperature NUMBER NOT NULL, 
  si7021_humidity NUMBER NOT NULL, 
  ccs811_tvoc NUMBER NOT NULL,
  sds011_dust NUMBER NOT NULL,
  created TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (unit_id) REFERENCES unit (id)
);

CREATE INDEX IF NOT EXISTS 
  ix_measurements_unit_id_registered ON measurement (unit_id, registered);