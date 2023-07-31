import streamlit as st
import plotly.graph_objs as go
import pandas as pd

# Load the Excel file into a Pandas dataframe
df = pd.read_excel('data.xlsx', index_col=0)

# Define the data as lists
# dates = ['Jan-23', 'Feb-23', 'Mar-23']
# critical_vuln = [6, 8, 3]
# high_vuln = [82, 84, 64]
# medium_vuln = [86, 97, 160]
# low_vuln = [13, 14, 15]

dates = list(df.columns)
critical_vuln = list(df.loc['Total Count of Critical Severity Vulnerability'])
high_vuln = list(df.loc['Total Count of High Severity Vulnerability'])
medium_vuln = list(df.loc['Total Count of Medium Severity Vulnerability'])
low_vuln = list(df.loc['Total Count of Low Severity Vulnerability'])

# Create traces for each severity level
trace1 = go.Scatter(x=dates, y=critical_vuln, mode='lines+markers', name='Critical')
trace2 = go.Scatter(x=dates, y=high_vuln, mode='lines+markers', name='High')
trace3 = go.Scatter(x=dates, y=medium_vuln, mode='lines+markers', name='Medium')
trace4 = go.Scatter(x=dates, y=low_vuln, mode='lines+markers', name='Low')

# Create the layout for the graph
layout = go.Layout(title='Vulnerabilities Over Time', xaxis=dict(title='Date'), yaxis=dict(title='Number of Vulnerabilities'))

# Create the figure with the traces and layout
fig = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)

# Show the figure
fig.show()
