import pandas as pd

# Load the Excel file into a Pandas dataframe
df = pd.read_excel('data.xlsx', index_col=0)

# Extract the data into lists
dates = list(df.columns)
critical_vuln = list(df.loc['Total Count of Critical Severity Vulnerability'])
high_vuln = list(df.loc['Total Count of High Severity Vulnerability'])
medium_vuln = list(df.loc['Total Count of Medium Severity Vulnerability'])
low_vuln = list(df.loc['Total Count of Low Severity Vulnerability'])

# Print the lists to verify the data was extracted correctly
print(dates)
print(critical_vuln)
print(high_vuln)
print(medium_vuln)
print(low_vuln)
