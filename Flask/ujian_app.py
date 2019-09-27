from flask import Flask,render_template
from ujian_plots import ujian_type1
from ujian_plots import ujian_type2
from ujian_data import data_ujian
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('ujian_home.html')

@app.route('/data')
def data():
    data = data_ujian().head()
    return render_template('ujian_table_data.html' , data=data)

@app.route('/stats')
def stats():
    data = data_ujian()
    return render_template('ujian_stats.html' , data=data)


@app.route('/plots')
def plots():
    data = ujian_type1()
    data2 = ujian_type2()
    return render_template('ujian_plot.html' , data=data, data2=data2)

if __name__ == '__main__':
    app.run(debug=True, port=1236)
