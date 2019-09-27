import plotly
import plotly.graph_objects  as go
from ujian_data import data_ujian
import json

def ujian_type1():
    df1 = data_ujian()
    df1_group= df1['mpg'].value_counts()
    
    fig = go.Figure([
        go.Bar(x=df1_group.index , y= df1_group.values)
    ])
    fig.update_layout(title_text='Distribusi Data Kolom MPG ')
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
    # fig.show()

def ujian_type2():
    df2 = data_ujian()
    df2_group= df2['horsepower'].value_counts()
    
    fig2 = go.Figure([
        go.Bar(x=df2_group.index , y= df2_group.values)
    ])
    fig2.update_layout(title_text='Distribusi Data Kolom Horsepower')
    fig2_json = json.dumps(fig2 , cls=plotly.utils.PlotlyJSONEncoder)
    return fig2_json

