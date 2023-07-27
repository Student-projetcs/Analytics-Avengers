#Librairies importation
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dcc

#Dataset importation 1
adult_mortality="https://raw.githubusercontent.com/Student-projetcs/Analytics-Avengers/main/datasets/Adult_Morality.csv"
df_adult_raw = pd.read_csv(adult_mortality)

class DataCleaningPipeline:
    def __init__(self,df):
        self.df_raw = df

    def drop_na_columns(self):
        df_adult_raw_c1 = self.df_raw.dropna(axis=1)
        df_new =  df_adult_raw_c1.dropna(axis=0)
        return df_new
    
    def select_range_by_years(self):
        if ('Dim1' in self.drop_na_columns()) is True:
            df_new_c1 = self.drop_na_columns().rename(columns={'Dim1':'Gender','Dim1ValueCode':'GenderCode','FactValueNumeric':'NumericValue'})
            df_cleaned = df_new_c1[(df_new_c1['Period']<2017) & (df_new_c1['Period']>1999)][['Indicator','ParentLocationCode','ParentLocation',
                                        'SpatialDimValueCode','Location','Period','GenderCode','Gender','NumericValue']]
        else:
            df_new_c1 = self.drop_na_columns().rename(columns={'FactValueNumeric':'NumericValue'})
            df_cleaned = df_new_c1[(df_new_c1['Period']<2017) & (df_new_c1['Period']>1999)][['Indicator','ParentLocationCode','ParentLocation',
                                        'SpatialDimValueCode','Location','Period','NumericValue']]
        return df_cleaned

adult = DataCleaningPipeline(df_adult_raw)
df_adult = adult.select_range_by_years()


#Dataset importation 2

#Dataset importation 3

#Figure1
df_geo_2000 = df_adult[df_adult['Period']==2000].groupby('SpatialDimValueCode')['NumericValue'].sum()
fig1 = px.scatter_geo(df_adult, locations=df_geo_2000.index, 
                     color=df_geo_2000.values,
                     size=df_geo_2000.values,labels = True,
                     color_continuous_scale='bluered'
                    )
fig1.update_layout(title = 'Geographic Analysis on Adult Morality(2000)')

#figure 2

#figure 3


# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Dashboard title", className="Dasboard-title"),
    html.Div([
        html.H1("Figure 1"),
        dcc.Graph(figure=fig1)
        ],className="section1"),
    html.Div([
        html.H1("Figure 3"),
        dcc.Graph(),
        ], className="section2"),
     html.Div([
        html.H1("Figure 4"),
        dcc.Graph()
        ], className="section4"),
     html.Div([
        html.H1("Figure 5"),
        dcc.Graph()
        ], className="section5"),
    ], className="mainSection")


# Run the app
if __name__ == '__main__':
    app.run(port= 8000, debug=True)
