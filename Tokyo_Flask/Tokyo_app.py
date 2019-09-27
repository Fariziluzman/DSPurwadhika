from flask import Flask,render_template
from Tokyo_plots import Tokyo_type1
from Tokyo_data import data_Tokyo
app = Flask(__name__)

# ROUTE
# RENDER TEMPLATE
# RENDER TEMPLATE WITH VARIABLE

@app.route('/')
def index():
    return render_template('Tokyo_home.html')

@app.route('/data')
def data():
    data = data_Tokyo()
    return render_template('Tokyo_table_data.html' , data=data)

@app.route('/plots')
def plots():
    data = Tokyo_type1()
    # data2 = sum_type2()
    return render_template('Tokyo_plot.html' , data=data)

@app.route('/Disabled')
def Disabled():
    return render_template('Tokyo_home.html')









# @app.route('/hello')
# def hello():
#     hasil = 5 + 19
#     return 'Ini Route Hello ' + str(hasil)

# @app.route('/template')
# def sabeb():
#     return render_template('contoh.html')

# @app.route('/template-with-data')
# def template_with_data():
#     # data = {
#     #     'name' : 'fikri',
#     #     'name2' : 'seto',
#     #     'name3' : 'Andi'
#     # }
#     data = ['Fikri' , 'Seto' , 'Andi']
#     return render_template('data.html', nama = data , panjang= len(data))

if __name__ == '__main__':
    app.run(debug=True, port=1235)
