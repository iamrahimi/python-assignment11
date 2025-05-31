import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load the dataset
df = pldata.wind(return_type='pandas')

# Print first and last 10 lines
print("First 10 rows:")
print(df.head(10))

print("\nLast 10 rows:")
print(df.tail(10))

# Remove non-numeric characters (e.g., 'calm-', '<', '+') and convert to float
df['strength_clean'] = df['strength'].str.extract(r'(\d+\.?\d*)')  # extract numeric part
df['strength_clean'] = df['strength_clean'].astype(float)

# Create an interactive scatter plot
fig = px.scatter(
    df,
    x='frequency',
    y='strength_clean',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={'strength_clean': 'Wind Strength', 'frequency': 'Frequency'}
)


# Save the plot as an HTML file
fig.write_html("assignment11/wind.html")

# Optionally, show plot in a browser
fig.show()