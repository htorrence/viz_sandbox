import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    html.H1('hello world'),
    html.Div([
        html.Button('Click!', id='button', n_clicks=0),
        html.Button('Reset', id='reset_button', n_clicks=0),
    ]),
    html.Br(),
    html.Br(),    
    html.Br(),
    html.Div('', id='count'),
])

@app.callback(
    Output('count', 'children'),
    [Input('button', 'n_clicks')],
)
def count_clicks(n_clicks):
    return('the button has been clicked {} times'.format(n_clicks))

@app.callback(
    Output('button', 'n_clicks'),
    [Input('reset_button', 'n_clicks')],
)
def reset_clicks(n_clicks):
    return(0)

@app.callback(
    Output('button', 'children'),
    [Input('button', 'n_clicks')],
)
def reset_click_button(n_clicks):
    if n_clicks == 0:
        return('Click!')
    else:
        return('Click again!')

if __name__ == '__main__':
    app.run_server(debug=True)










