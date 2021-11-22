from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import datetime

class ChartForm(FlaskForm):
    ticker = StringField('Ticker', default="MSFT", validators=[DataRequired()])
    start_date = DateField('Start date', default=datetime.date.today() - datetime.timedelta(days=30), format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('End date', default=datetime.date.today(), format='%Y-%m-%d', validators=[DataRequired()])
    ma = BooleanField('Moving Average')
    delta = IntegerField('Moving Average Delta (Days)', default=5)
    macd = BooleanField('Moving Average Convergence Divergence')
    rsi = BooleanField('Relative Strength Index')
    refresh = SubmitField('Refresh')