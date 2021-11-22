from flask import Flask, render_template
import yfinance as yf
from forms import ChartForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '64479dfecfe4778d1b7131fb577a3645'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ChartForm()
    ticker = form.ticker.data
    stock = yf.Ticker(ticker)
    hist = stock.history(period="max")
    
    # Filter Dates
    hist = hist.loc[form.start_date.data : form.end_date.data]

    # Format dates and prices to json to send to front-end
    hist['Dates'] = hist.index
    hist['Dates'] = hist['Dates'].dt.strftime('%Y-%m-%d')
    prices = hist['Close'].to_json(orient="values")
    dates = hist['Dates'].to_json(orient="values")

    ma = form.ma.data
    macd = form.macd.data
    rsi = form.rsi.data
    delta = form.delta.data

    return render_template('home.html', prices=prices, dates=dates, ticker=ticker, form=form, ma=ma, macd=macd, rsi=rsi, delta=delta)

if __name__ == '__main__':
    app.run(debug=True)
