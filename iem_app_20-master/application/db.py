import os
import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
import mysql.connector


def get_db():
    """
    Denne funksjonen åpner databasen som den henter fra instance/config.py
    Den lager tilkoblingen i g (Globale variabler i flask) for at en ikke skal lage en ny tilkobling
    hver gang en kaller get_db()
    """
    if 'db' not in g:
        '''
        g.db = sqlite3.connect(
            os.path.join(current_app.instance_path, current_app.config['DATABASE']),
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        '''
        config = {
            'host': current_app.config['DB_HOSTNAME'],
            'user': current_app.config['DB_USER'],
            'password': current_app.config['DB_PASSWORD'],
            'database': current_app.config['DB_DATABASE'],
            'ssl_verify_cert': False,
            'port' : 3306
        }
    

        g.db = mysql.connector.connect(**config)
        print("Connection established")

    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)


def init_db():
    db = get_db()
    with current_app.open_resource('data/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def add_measurement(unit_id, registered, bmp280_temperature, bmp280_pressure, si7021_temperature, si7021_humidity, ccs811_tvoc, sds011_dust):
    '''
    Legger til en post i tabellen med målinge
    '''
    db = get_db() 
    c = db.cursor()
    c.execute('''
        INSERT INTO measurement(unit_id, registered, bmp280_temperature, bmp280_pressure, si7021_temperature, si7021_humidity, ccs811_tvoc, sds011_dust)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        ''', 
        (unit_id, registered, bmp280_temperature, bmp280_pressure, si7021_temperature, si7021_humidity, ccs811_tvoc, sds011_dust) # tuple eller liste, () eller []
        )
    db.commit()
    return c.lastrowid

def select_measurements():
    db = get_db()
    c = db.cursor(dictionary=True)
    c.execute('''
        SELECT * FROM measurement ORDER BY created DESC
        '''
        )
    return c.fetchall()

