import plotly.plotly as py
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd


##data: MacOSX - 9, Windows - 4, Debian - 2, Other - 0

url = 'https://raw.githubusercontent.com/milaroisin/plotlyDashOS/master/dataset/plotlyoperatingsystems.csv'

os_data = pd.read_csv(url)

app = dash.Dash()
app.title = 'Dash App: Operating Systems - Interns'

## css elements with bootstrap
app.css.append_css({'external_url': 'https://bootswatch.com/4/lux/bootstrap.css'})

app.layout = html.Div(
    html.Div([
        dcc.Graph(
            id='barchart',
            figure={
                'data': [
                    {'x': ['MacOSX', 'Windows', 'Linux', 'Other'],
                     'y': [9, 4, 2, 0], 'type': 'bar'}],
                'layout': {
                    'title': 'Plot.ly: Summer 2019 Preferred Operating Systems',
                    'xaxis': dict(
                        title='Operating Systems',
                        titlefont=dict(
                        family='Old Standard TT',
                        size=20,
                        color='#7f7f7f'
                    )),
                    'yaxis' : dict(
                        title='# of Interns',
                        titlefont=dict(
                        family='Old Standard TT',
                        size=20,
                    ))
                }
            }
        ),

        dcc.Graph(
            id='example-graph-2',
            figure={
                'data': [
                    {'x': ['MacOSX', 'Windows', 'Linux', 'Other'],
                     'y': [9, 4, 2, 0], 'type': 'line'}],
                'layout': {
                    'title': 'Plot.ly: Summer 2019 Preferred Operating Systems',
                    'xaxis': dict(
                        title='Operating Systems',
                        titlefont=dict(
                        family='Old Standard TT',
                        size=20
                        )),
                    'yaxis': dict(
                    title='# of Interns',
                    titlefont=dict(
                    family='Old Standard TT',
                        size=20
                    ))
                }
            }
        )

    ])
)


# piechart with hole


## return event statement

if __name__ == '__main__':
    app.run_server(debug=True)

    ##end
