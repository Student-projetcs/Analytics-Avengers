#Librairies importation
import numpy as np
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dcc

#Dataset importation 1
# Qintong Li: Adult Morality
df_adult = pd.read_csv('https://github.com/Student-projetcs/Analytics-Avengers/blob/main/datasets/Adult_Morality.csv')
df_geo_2000 = df_adult[(df_adult['Period']==2000)&(df_adult['Gender']=='Both sexes')]
df_geo_2016 = df_adult[(df_adult['Period']==2016)&(df_adult['Gender']=='Both sexes')]

#Dataset importation 2

#Dataset importation 3

#Figure1
# Qintong Li: Adult Morality

rows = 1
cols = 2
fig_geo = make_subplots(
    rows=rows, cols=cols,
    specs = [[{'type': 'choropleth'} for c in np.arange(cols)] for r in np.arange(rows)],
                        )


fig_geo.add_trace(go.Choropleth(
    locations=df_geo_2000['Location'],     
    locationmode='country names', 
    z=df_geo_2000['NumericValue'],             
    zmin=df_geo_2000['NumericValue'].min(),
    zmax=df_geo_2016['NumericValue'].max(),
    colorscale='bluered',         
    text=df_geo_2000['Location'],              
    colorbar_title='Adult Morality',
    
    hoverinfo='location+z',
    
),row = 1,col = 1    )



fig_geo.add_trace(go.Choropleth(
    locations=df_geo_2016['Location'],    
    locationmode='country names', 
    z=df_geo_2016['NumericValue'],            
    zmin=df_geo_2000['NumericValue'].min(),
    zmax=df_geo_2016['NumericValue'].max(),
    colorscale='bluered',         
    text=df_geo_2016['Location'],              
    colorbar_title='Adult Morality',
    hoverinfo='location+z',
),row = 1,col = 2)



fig_geo.update_geos(fitbounds="locations",
                visible=False,
                )

fig_geo.update_layout(
    title='Fig.2. Geographic Analysis on World Adult Morality 2000 vs 2016',
    title_x=0.5
#     geo=dict(
#         projection_type='natural earth',   # Choose the map projection
#     )
)

#figure 2

#figure 3


# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div([
        html.H1("Figure 1"),
        dcc.Graph(figure = fig_geo)
        ]),
    html.Div([
        html.H1("Figure 3"),
        dcc.Graph()
        ]),
     html.Div([
        html.H1("Figure 4"),
        dcc.Graph()
        ]),
     html.Div([
        html.H1("Figure 5"),
        dcc.Graph()
        ])
])


# Run the app
if __name__ == '__main__':
    app.run(port= 8000, debug=True)
