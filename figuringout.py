
import plotly.express as px
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pandas as pd

app = dash.Dash(__name__)

df2 = pd.read_csv(r"\Users\tinah\proj1\New Employee Attrition final.csv")

xlabel= df2["Age"]
ylabel= df2["DailyRate"]


app.layout = html.Div([


## Adding a title and the IBM logo with stylesheet.css

    html.Div([
        html.H2("IBM Employee Data"),
        html.Img(src="/assets/IBMLOGO.png")

    ], className="banner"),





    html.Div([

        html.Div([
            html.Label(['Choose a value to plot'],style={'font-weight': 'bold', "text-align": "left",'color': 'Blue', 'fontSize': 20}),

            dcc.Dropdown(id='my_dropdown',options=[
                        {'label': 'Age', 'value': 'Age'},
                        {'label': 'Gender', 'value': 'Gender'},
                        {'label': 'Daily Rate', 'value': 'DailyRate'},
                        {'label': 'Distance from Home', 'value': 'DistanceFromHome'},
                        {'label': 'Business Travel', 'value': 'BusinessTravel'},
                        {'label': 'Department', 'value': 'Department'},
                        {'label': 'Job Role', 'value': 'JobRole'},
                        {'label': 'Attrition', 'value': 'Attrition'},
                        {'label': 'Education', 'value': 'Education'},
                        {'label': 'EducationField', 'value': 'EducationField'},
                        {'label': 'EvironmentSatisfaction', 'value': 'EvironmentSatisfaction'},
                        {'label': 'JobInvolvement', 'value': 'JobInvolvement'},
                        {'label': 'Job Level', 'value': 'Job Level'},
                        {'label': 'JobSatisfaction', 'value': 'JobSatisfaction'},
                        {'label': 'MaritalStatus', 'value': 'MaritalStatus'},
                        {'label': 'Over18', 'value': 'Over18'},
                        {'label': 'OverTime', 'value': 'OverTime'},
                        {'label': 'PerformanceRating', 'value': 'PerformanceRating'},
                        {'label': 'RelationshipSatisfaction', 'value': 'RelationshipSatisfaction'},
                        {'label': 'WorkLifeBalance', 'value': 'WorkLifeBalance'},
                        {'label': 'Distance from Home', 'value': 'DistanceFromHome'},
                        {'label': 'Hourly Rate', 'value': 'HourlyRate'},
                        {'label': 'Monthly Income', 'value': 'MonthlyIncome'},
                        {'label': 'Number Companies Worked', 'value': 'NumCompaniesWorked'},
                        {'label': 'Percent Salary Hike', 'value': 'PercentSalaryHike'},
                        {'label': 'Stock Option Level', 'value': 'StockOptionLevel'},
                        {'label': 'Total Working Years', 'value': 'TotalWorkingYears'},
                        {'label': 'Training Times Last Year', 'value': 'TrainingTimesLastYear'},
                        {'label': 'Years At Company', 'value': 'YearsAtCompany'},
                        {'label': 'Years In Current Role', 'value': 'YearsInCurrentRole'},
                        {'label': 'Years Since Last Promotion', 'value': 'YearsSinceLastPromotion'},
                        {'label': 'Years With Current Manager', 'value': 'YearsWithCurrManager'}],
                optionHeight=35,
                value='Age',
                disabled=False,
                multi=False,
                searchable=True,
                search_value='',
                placeholder='Select a Value',
                clearable=True,
                style={'width':"100%"},
                ),
        ],className='twelve columns'),


        ]),







##barchart

    html.Div([
            dcc.Graph(id='Barchart')
        ], className='five columns'),






## PIE CHART

        html.Div([
            dcc.Graph(id='Piechart')
        ], className='five columns'),







html.Div([

                html.Label(["Pick an axis"],style={'font-weight': 'bold', "text-align": "left",'color': 'Blue', 'fontSize': 18}),

                dcc.RadioItems(id='radio',
                    options=[{'label': 'X axis', 'value': 'X'},{'label': 'Y axis', 'value': 'Y'}]
                    ),
            ],className='one columns'),










#### SCATTERPLOT

    html.Div([
        dcc.Graph(id='Scatter1')
    ], className='ten columns'),










## A drop down for our second scatter plot
    html.Div([
        html.Label(['Choose a X Value'], style={'font-weight': 'bold', "text-align": "left",'color': 'Blue', 'fontSize': 20}),

        dcc.Dropdown(id='my_dropdown2',
                     options=[
                        {'label': 'Age', 'value': 'Age'},
                        {'label': 'Daily Rate', 'value': 'DailyRate'},
                        {'label': 'Distance from Home', 'value': 'DistanceFromHome'},
                        {'label': 'Business Travel', 'value': 'BusinessTravel'},
                        {'label': 'Department', 'value': 'Department'},
                        {'label': 'Attrition', 'value': 'Attrition'},
                        {'label': 'Education', 'value': 'Education'},
                        {'label': 'EducationField', 'value': 'EducationField'},
                        {'label': 'EvironmentSatisfaction', 'value': 'EvironmentSatisfaction'},
                        {'label': 'JobInvolvement', 'value': 'JobInvolvement'},
                        {'label': 'Job Level', 'value': 'Job Level'},
                        {'label': 'JobSatisfaction', 'value': 'JobSatisfaction'},
                        {'label': 'MaritalStatus', 'value': 'MaritalStatus'},
                        {'label': 'Over18', 'value': 'Over18'},
                        {'label': 'OverTime', 'value': 'OverTime'},
                        {'label': 'PerformanceRating', 'value': 'PerformanceRating'},
                        {'label': 'RelationshipSatisfaction', 'value': 'RelationshipSatisfaction'},
                        {'label': 'WorkLifeBalance', 'value': 'WorkLifeBalance'},
                        {'label': 'Distance from Home', 'value': 'DistanceFromHome'},
                        {'label': 'Hourly Rate', 'value': 'HourlyRate'},
                        {'label': 'Monthly Income', 'value': 'MonthlyIncome'},
                        {'label': 'Number Companies Worked', 'value': 'NumCompaniesWorked'},
                        {'label': 'Percent Salary Hike', 'value': 'PercentSalaryHike'},
                        {'label': 'Stock Option Level', 'value': 'StockOptionLevel'},
                        {'label': 'Total Working Years', 'value': 'TotalWorkingYears'},
                        {'label': 'Training Times Last Year', 'value': 'TrainingTimesLastYear'},
                        {'label': 'Years At Company', 'value': 'YearsAtCompany'},
                        {'label': 'Years In Current Role', 'value': 'YearsInCurrentRole'},
                        {'label': 'Years Since Last Promotion', 'value': 'YearsSinceLastPromotion'},
                        {'label': 'Years With Current Manager', 'value': 'YearsWithCurrManager'}],
                     optionHeight=40,
                     value='DailyRate',
                     disabled=False,
                     multi=False,
                     searchable=True,
                     search_value='',
                     placeholder='Select a Value',
                     clearable=True,
                     style={'width': "100%"},
                     ),
    ], className='five columns'),
html.Div([
        html.Label(['Choose a Y Value'], style={'font-weight': 'bold', "text-align": "left",'color': 'Blue', 'fontSize': 20}),

        dcc.Dropdown(id='my_dropdown3',
                     options=[
                        {'label': 'Age', 'value': 'Age'},
                        {'label': 'Daily Rate', 'value': 'DailyRate'},
                        {'label': 'Distance from Home', 'value': 'DistanceFromHome'},
                        {'label': 'Business Travel', 'value': 'BusinessTravel'},
                        {'label': 'Department', 'value': 'Department'},
                        {'label': 'Attrition', 'value': 'Attrition'},
                        {'label': 'Education', 'value': 'Education'},
                        {'label': 'EducationField', 'value': 'EducationField'},
                        {'label': 'EvironmentSatisfaction', 'value': 'EvironmentSatisfaction'},
                        {'label': 'JobInvolvement', 'value': 'JobInvolvement'},
                        {'label': 'Job Level', 'value': 'Job Level'},
                        {'label': 'JobSatisfaction', 'value': 'JobSatisfaction'},
                        {'label': 'MaritalStatus', 'value': 'MaritalStatus'},
                        {'label': 'Over18', 'value': 'Over18'},
                        {'label': 'OverTime', 'value': 'OverTime'},
                        {'label': 'PerformanceRating', 'value': 'PerformanceRating'},
                        {'label': 'RelationshipSatisfaction', 'value': 'RelationshipSatisfaction'},
                        {'label': 'WorkLifeBalance', 'value': 'WorkLifeBalance'},
                        {'label': 'Distance from Home', 'value': 'DistanceFromHome'},
                        {'label': 'Hourly Rate', 'value': 'HourlyRate'},
                        {'label': 'Monthly Income', 'value': 'MonthlyIncome'},
                        {'label': 'Number Companies Worked', 'value': 'NumCompaniesWorked'},
                        {'label': 'Percent Salary Hike', 'value': 'PercentSalaryHike'},
                        {'label': 'Stock Option Level', 'value': 'StockOptionLevel'},
                        {'label': 'Total Working Years', 'value': 'TotalWorkingYears'},
                        {'label': 'Training Times Last Year', 'value': 'TrainingTimesLastYear'},
                        {'label': 'Years At Company', 'value': 'YearsAtCompany'},
                        {'label': 'Years In Current Role', 'value': 'YearsInCurrentRole'},
                        {'label': 'Years Since Last Promotion', 'value': 'YearsSinceLastPromotion'},
                        {'label': 'Years With Current Manager', 'value': 'YearsWithCurrManager'}],
                     optionHeight=40,
                     value='Age',
                     disabled=False,
                     multi=False,
                     searchable=True,
                     search_value='',
                     placeholder='Select a Value',
                     clearable=True,
                     style={'width': "100%"},
                     ),
    ], className='five columns'),

    html.Div([
            dcc.Graph(id='Scatter2')
        ], className= 'seven columns'),








# Creates a checklist

        html.Div([
                html.Label(children=['Select a Job Role for Scatterplot: '], style={'font-weight': 'bold','color': 'Blue', 'fontSize': 20}),
                dcc.Checklist(id='JobRole',
                              options=[{'label': str(b), 'value': b} for b in sorted(df2['JobRole'].unique())],
                              value=[b for b in sorted(df2['JobRole'].unique())])], className='four columns'),


# creates another dropdown for just one scatterplot
    html.Div([

        html.Label(['Choose a X Value'], style={'font-weight': 'bold', "text-align": "left",'color': 'Blue', 'fontSize': 20}),

        dcc.Dropdown(id='my_dropdown4',
                     options=[
                        {'label': 'Age', 'value': 'Age'},
                        {'label': 'Gender', 'value': 'Gender'},
                        {'label': 'Daily Rate', 'value': 'DailyRate'},
                        {'label': 'Distance from Home', 'value': 'DistanceFromHome'},
                        {'label': 'Business Travel', 'value': 'BusinessTravel'},
                        {'label': 'Department', 'value': 'Department'},
                        {'label': 'Job Role', 'value': 'JobRole'},
                        {'label': 'Education', 'value': 'Education'},
                        {'label': 'Education Field', 'value': 'EducationField'},
                        {'label': 'Evironment Satisfaction', 'value': 'EvironmentSatisfaction'},
                        {'label': 'Job Involvement', 'value': 'JobInvolvement'},
                        {'label': 'Job Level', 'value': 'Job Level'},
                        {'label': 'JobSatisfaction', 'value': 'JobSatisfaction'},
                        {'label': 'MaritalStatus', 'value': 'MaritalStatus'},
                        {'label': 'Over18', 'value': 'Over18'},
                        {'label': 'OverTime', 'value': 'OverTime'},
                        {'label': 'PerformanceRating', 'value': 'PerformanceRating'},
                        {'label': 'RelationshipSatisfaction', 'value': 'RelationshipSatisfaction'},
                        {'label': 'WorkLifeBalance', 'value': 'WorkLifeBalance'},
                        {'label': 'Distance from Home', 'value': 'DistanceFromHome'},
                        {'label': 'Hourly Rate', 'value': 'HourlyRate'},
                        {'label': 'Monthly Income', 'value': 'MonthlyIncome'},
                        {'label': 'Number Companies Worked', 'value': 'NumCompaniesWorked'},
                        {'label': 'Percent Salary Hike', 'value': 'PercentSalaryHike'},
                        {'label': 'Stock Option Level', 'value': 'StockOptionLevel'},
                        {'label': 'Total Working Years', 'value': 'TotalWorkingYears'},
                        {'label': 'Training Times Last Year', 'value': 'TrainingTimesLastYear'},
                        {'label': 'Years At Company', 'value': 'YearsAtCompany'},
                        {'label': 'Years In Current Role', 'value': 'YearsInCurrentRole'},
                        {'label': 'Years Since Last Promotion', 'value': 'YearsSinceLastPromotion'},
                        {'label': 'Years With Current Manager', 'value': 'YearsWithCurrManager'}],
                     optionHeight=40,
                     value='DailyRate',
                     disabled=False,
                     multi=False,
                     searchable=True,
                     search_value='',
                     placeholder='Select a Value',
                     clearable=True,
                     style={'width': "100%"},

                     ),
    ], className='five columns'),
    html.Div([

        html.Label(['Choose a Y Value'],
                   style={'font-weight': 'bold', "text-align": "left", 'color': 'Blue', 'fontSize': 20}),

        dcc.Dropdown(id='my_dropdown5',
                     options=[
                         {'label': 'Age', 'value': 'Age'},
                         {'label': 'Gender', 'value': 'Gender'},
                         {'label': 'Daily Rate', 'value': 'DailyRate'},
                         {'label': 'Distance from Home', 'value': 'DistanceFromHome'},
                         {'label': 'Business Travel', 'value': 'BusinessTravel'},
                         {'label': 'Department', 'value': 'Department'},
                         {'label': 'Job Role', 'value': 'JobRole'},
                         {'label': 'Education', 'value': 'Education'},
                         {'label': 'Education Field', 'value': 'EducationField'},
                         {'label': 'Evironment Satisfaction', 'value': 'EvironmentSatisfaction'},
                         {'label': 'Job Involvement', 'value': 'JobInvolvement'},
                         {'label': 'Job Level', 'value': 'Job Level'},
                         {'label': 'JobSatisfaction', 'value': 'JobSatisfaction'},
                         {'label': 'MaritalStatus', 'value': 'MaritalStatus'},
                         {'label': 'Over18', 'value': 'Over18'},
                         {'label': 'OverTime', 'value': 'OverTime'},
                         {'label': 'PerformanceRating', 'value': 'PerformanceRating'},
                         {'label': 'RelationshipSatisfaction', 'value': 'RelationshipSatisfaction'},
                         {'label': 'WorkLifeBalance', 'value': 'WorkLifeBalance'},
                         {'label': 'Distance from Home', 'value': 'DistanceFromHome'},
                         {'label': 'Hourly Rate', 'value': 'HourlyRate'},
                         {'label': 'Monthly Income', 'value': 'MonthlyIncome'},
                         {'label': 'Number Companies Worked', 'value': 'NumCompaniesWorked'},
                         {'label': 'Percent Salary Hike', 'value': 'PercentSalaryHike'},
                         {'label': 'Stock Option Level', 'value': 'StockOptionLevel'},
                         {'label': 'Total Working Years', 'value': 'TotalWorkingYears'},
                         {'label': 'Training Times Last Year', 'value': 'TrainingTimesLastYear'},
                         {'label': 'Years At Company', 'value': 'YearsAtCompany'},
                         {'label': 'Years In Current Role', 'value': 'YearsInCurrentRole'},
                         {'label': 'Years Since Last Promotion', 'value': 'YearsSinceLastPromotion'},
                         {'label': 'Years With Current Manager', 'value': 'YearsWithCurrManager'}],
                     optionHeight=40,
                     value='Age',
                     disabled=False,
                     multi=False,
                     searchable=True,
                     search_value='',
                     placeholder='Select a Value',
                     clearable=True,
                     style={'width': "100%"},
                     ),
    ], className='five columns'),

        html.Div([
                dcc.Graph(id='Scatter3')
            ], className= 'seven columns'),

], className="row")






####Building barchart and histogram
@app.callback(
    Output(component_id='Barchart', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def build_bar(column_chosen):
    if (is_string_dtype(df2[column_chosen])):   ## if column is a string create a barchart
        bar = px.bar(df2,y=df2[column_chosen].value_counts(), x=df2[column_chosen].value_counts().sort_index().index, opacity= 0.75, text= df2[column_chosen].value_counts(), color= df2[column_chosen].unique(), title= "Bar Chart",
                     labels={'x': column_chosen, 'y': 'count'})


    elif (is_numeric_dtype(df2[column_chosen])):  ## if column is a numeric create a histogram
        bar = px.histogram(df2,x=df2[column_chosen], nbins=7, opacity= 0.75,title= "Histogram")

    return bar






#### Building Pie chart
@app.callback(
    Output(component_id='Piechart', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def Pie_Chart(column_chosen):
    if (is_string_dtype(df2[column_chosen])):    #if the column is a string type
        if (df2[column_chosen]).name == "JobRole":   #job role is the only category with more than 6 categories
            LowerVals = pd.Series({'Other': df2[column_chosen].value_counts()[5:].sum()})  # we want to find the lowest values and sum them into a category called other
            DF = pd.concat([df2[column_chosen].value_counts()[:5], LowerVals])
            pie = px.pie(values=DF.values, names=DF.index, title= "Pie Chart")
        else:
            pie = px.pie(names=df2[column_chosen].value_counts().index,values=df2[column_chosen].value_counts().values, title= "Pie Chart")

    elif (is_numeric_dtype(df2[column_chosen])):    #if the column is a numeric type
        range = df2[column_chosen].max() - df2[column_chosen].min()
        df21= pd.cut(df2[column_chosen], bins=[df2[column_chosen].min(),                                 # Using pandas cut to create 6 bins of our numerial data
                                               df2[column_chosen].min() + range * 1 / 6,
                                               df2[column_chosen].min() + range * 2/ 6,
                                               df2[column_chosen].min() + range * 3 / 6,
                                               df2[column_chosen].min() + range * 4/ 6,
                                               df2[column_chosen].min() + range * 5/ 6,
                                               df2[column_chosen].max()], include_lowest= True)
        pie = px.pie(names=df21.value_counts().index.astype(str), values=df21.value_counts().values, title= "Pie Chart")   #plotly express piechart with
    return pie





## Building scatterplot
@app.callback(
    Output(component_id='Scatter1', component_property='figure'),    #output will be the scatterplot
    [Input(component_id='my_dropdown', component_property='value'),   #inout is the radiobuttons and the dropdown value picked
    Input(component_id='radio', component_property='value')]
)

def Scatter_graph_radio(column_chosen, radio_val):
    global xlabel     #creating global variables to help store our values
    global ylabel

    if radio_val is None:
        xlabel = column_chosen
        ylabel = column_chosen
        fig = px.scatter(df2, x=df2[xlabel], y=df2[ylabel], title="Scatterplot" )

    elif radio_val == 'X':    #when the user picks X from our radioitem we can now set the column to the picked value
        xlabel = column_chosen
        fig = px.scatter(df2, x=df2[xlabel], y=df2[ylabel], title= "Scatterplot")

    elif radio_val == 'Y':
        ylabel= column_chosen    #when the user picks Y from our radioitem we can now set the column to the picked value
        fig = px.scatter(df2, x=df2[xlabel], y=df2[ylabel], title= "Scatterplot")

    return fig



###########################################################
### Not assigned but included for personal interest

@app.callback(
    Output(component_id='Scatter2', component_property='figure'),
    [Input(component_id='my_dropdown2', component_property='value'),
    Input(component_id='my_dropdown3', component_property='value'),
     Input(component_id='JobRole', component_property='value')]
)

def Scatter_graph_withcheck(column_chosen, column_chosen2, Jobrole):
    df_sub= df2[(df2['JobRole'].isin(Jobrole))]
    scatter= px.scatter(df_sub, x=column_chosen, y= column_chosen2,color=df_sub['Gender'], title= "Scatterplot for Job Role")
    return scatter




@app.callback(
    Output(component_id='Scatter3', component_property='figure'),
    [Input(component_id='my_dropdown4', component_property='value'),
    Input(component_id='my_dropdown5', component_property='value')]
)

def Scatter_graph_withAttrition(column_chosen, column_chosen2):
    scatter3= px.scatter(df2, x=column_chosen, y= column_chosen2, color=df2["Attrition"], title= "Scatterplot showing attrition")
    return scatter3






if __name__ == '__main__':
    app.run_server(debug=True)