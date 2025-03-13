
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

def process_data(df_storm):
    # Drop rows with missing values
    df_storm = df_storm.dropna()

    # Group by year and status
    df = df_storm.groupby(['year', 'status'])['n'].sum().reset_index()

    # Filter the dataframe by different statuses
    df_hurricane = df[df['status'] == 'hurricane']
    df_tropical_storm = df[df['status'] == 'tropical storm']
    df_tropical_depression = df[df['status'] == 'tropical depression']
    df_tropical_wave = df[df['status'] == 'tropical wave']

    return df_hurricane, df_tropical_storm, df_tropical_depression, df_tropical_wave

# Load the data
url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/storms/storms.csv"
df_storm = pd.read_csv(url)

# Process the data
df_hurricane, df_tropical_storm, df_tropical_depression, df_tropical_wave = process_data(df_storm)

# Create a figure and axis
fig, ax = plt.subplots()

ax.plot(df_tropical_wave['year'], df_tropical_wave['n'], label='Tropical Waves', color='#C2B8B2')
ax.plot(df_tropical_depression['year'], df_tropical_depression['n'], label='Tropical Depressions', color='#eee29a')
ax.plot(df_tropical_storm['year'], df_tropical_storm['n'], label='Tropical Storms', color='#f5a623')
ax.plot(df_hurricane['year'], df_hurricane['n'], label='Hurricanes', color='#db372d')

# Add axis title and subtitle
ax.set_title('Frequency of Different Types of Storms (2010-2022)', weight='heavy', fontsize=20, loc='left', color='#333333')
ax.set_ylabel('Frequency', weight='bold', color='#333333')

# Add grid with light grey color
ax.yaxis.grid(True, color='#d7d7d7', linestyle=':', linewidth=0.5)

# Set figure and axis face color
fig.patch.set_facecolor('#f6f6f6')
ax.set_facecolor('#f6f6f6')

# Remove x and y ticks
ax.tick_params(axis='y', which='both', left=False, right=False)

# Remove left, right, and top border
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Add the legend to the plot
ax.legend(labels=ax.get_legend_handles_labels()[1], loc='upper left', frameon=False, ncol=4)

plt.show()
