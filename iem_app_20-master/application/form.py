from random import randint
from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField, DateTimeField


class MyForm(FlaskForm):
    firstname = StringField('Fornavn', validators=[DataRequired()], render_kw={"placeholder": "Ditt fornavn"})
    lastname = StringField('Etternavn', validators=[DataRequired()], default='Hogstad')
    dato = DateField('Dato', default=date.today())


class MeasurementForm(FlaskForm):
    unit_id = IntegerField('Enhet', default=1, validators=[DataRequired()])
    registered = DateTimeField('Dato/Tid', default=datetime.now(), validators=[DataRequired()])
    bmp280_temperature = FloatField('BME280 Temperatur', validators=[DataRequired()])
    bmp280_pressure = FloatField('BME280 Trykk', validators=[DataRequired()])
    si7021_temperature = FloatField('Si7021 Temperatur', validators=[DataRequired()])
    si7021_humidity = FloatField('Si7021 Fuktighet', validators=[DataRequired()])
    ccs811_tvoc = FloatField('CCS811 TVOC', validators=[DataRequired()])
    sds011_dust = FloatField('SDS011 Støv', validators=[DataRequired()])



'''
# Hvordan få flyttall feilt til å akseptere komma
# Se eventuelt på use_locale parameter og installere Babel pakken og DecimalField
class MyFloatField(FloatField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = float(valuelist[0].replace(',', '.'))
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid float value'))
'''