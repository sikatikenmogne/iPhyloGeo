from dash import html

layout = html.Div([
    html.Div(
        html.Div([
            html.Div([
                html.Div([
                    html.Img(src='../../assets/icons/close.svg', className="icon", id="close_popup"),
                ], className="close"),
                html.Div('Please don\'t close your browser window until we finish generating your file', className="title"),
                html.A([
                    html.Img(src='../../assets/img/coffee-cup.gif', className="icon"),
                ], href="https://www.flaticon.com/authors/freepik", target="_blank", className="link"),
                html.Div('This may take a few minutes', className="description"),
            ], className='content'),
        ], className="popup hidden", id="popup")
    ),
])