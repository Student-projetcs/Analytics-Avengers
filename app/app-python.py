#Librairies importation
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dcc

#Dataset importation 1
#Importing Child Mortality file
df = pd. read_csv('C:/Users/SonyY/Documents/Portfolio Project/Infant Mortality Rate.csv')


#Dataset importation 2

#Dataset importation 3

#Figure1
fig_map = px.choropleth(df_latest_btsx, locations='CountryCode', color='MortalityRate', hover_name='Country',
                    projection='natural earth',
                    title='Child Mortality Rate by Country (Both Sex, Latest Year)',
                    labels={'MortalityRate': 'Mortality Rate',
                            'Sex' : 'Sex'
                        })


#figure 2
fig_years_region = px.line(
    df_years_sex_region, x='Year', y='MortalityRate',
    color='Region', line_group='Sex',  
    line_dash='Sex',  
    markers=True,  
    title='Child Mortality Rate (Under 5) by Region and Sex',
    labels={'Year': 'Year', 'MortalityRate': 'Mortality Rate'},
#figure 3
fig_avg_mortality = px.bar(
                    df_avg_mortality, x = 'Average_Percentage_Change', y = 'Region', color = 'Sex', orientation='h',
                    barmode = 'group', title = 'Avg. Child Mortality Rate Change (2002-2021) by Region'
                    
)

fig_avg_mortality.update_xaxes(title_text="Average Mortality Rate Percentage Change (%)")

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div([
        html.H1("Figure 1"),
        dcc.Graph()
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
