import plotly.plotly as py
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go

url = 'https://raw.githubusercontent.com/milaroisin/plotlyDashOS/master/dataset/plotlyoperatingsystems.csv'

os_data = pd.read_csv(url)

##data: MacOSX - 9, Windows - 4, Debian - 2, Other - 0

app = dash.Dash()
app.title = 'Dash App: Operating Systems - Interns'

## css elements for grid alignment

app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

app.layout = html.Div(
html.Div([
        html.H3(children='Plot.ly: Summer 2019 Preferred Operating Systems'),

    ##Donut Chart
    dcc.Graph(
        id='piechart',
        figure={
            'data': [{'labels': ['MacOSX', 'Windows', 'Linux', 'Other'],
                      'values': [60, 26.7, 13.3, 0],
                      'sort': False,
                      'showLegend': False,
                      'text-info': 'percent-label',
                      'colors': ['#ffa15a',
                                 '#19d3f3',
                                 '#fecb52',
                                 '#ff6692'],
                      'type': 'pie',
                      'hole': 0.8,
                      }],
            'layout': {
                'title': 'Plot.ly: Summer 2019 Preferred Operating Systems',
                'xaxis': dict(
                    title='Operating Systems',
                    titlefont=dict(
                        family='Old Standard TT',
                        size=20)),
                'yaxis': dict(
                    title='# of Interns',
                    titlefont=dict(
                        family='Old Standard TT',
                        size=20))
            }
        }
    )
])
)
## return event statement

if __name__ == '__main__':
    app.run_server(debug=True)

    ##end
