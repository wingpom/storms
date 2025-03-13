
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

    return df, df_hurricane, df_tropical_storm, df_tropical_depression, df_tropical_wave

def line_plot(df_hurricane, df_tropical_storm, df_tropical_depression, df_tropical_wave):
    # Create a figure and axis
    fig, ax = plt.subplots()

    ax.plot(df_tropical_wave['year'], df_tropical_wave['n'], label='Tropical Waves', color='gold')
    ax.plot(df_tropical_depression['year'], df_tropical_depression['n'], label='Tropical Depressions', color='coral')
    ax.plot(df_tropical_storm['year'], df_tropical_storm['n'], label='Tropical Storms', color='lightgreen')
    ax.plot(df_hurricane['year'], df_hurricane['n'], label='Hurricanes', color='skyblue')

    # Add axis title and subtitle
    ax.set_title('Frequency of Different Types of Storms (2010-2022)', weight='heavy', fontsize=12, loc='left', color='#333333')
    ax.set_ylabel('Frequency', weight='bold', fontsize=10, color='#333333')

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
    fig.legend(fontsize=8, loc='lower center', frameon=False, ncol=4)

    plt.show()

def lolipop_plot(df):
    
    # Sort the data by year
    ordered_dfs = {
        'Hurricanes': df[df['status'] == 'hurricane'].sort_values(by='year'),
        'Tropical Storms': df[df['status'] == 'tropical storm'].sort_values(by='year'),
        'Tropical Depressions': df[df['status'] == 'tropical depression'].sort_values(by='year'),
        'Tropical Waves': df[df['status'] == 'tropical wave'].sort_values(by='year')
    }

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Define colors for each status
    colors = {
        'Hurricanes': 'skyblue',
        'Tropical Storms': 'lightgreen',
        'Tropical Depressions': 'coral',
        'Tropical Waves': 'gold'
    }

    # Create a stem plot with stems next to each other per year
    width = 0.2
    for i, (label, ordered_df) in enumerate(ordered_dfs.items()):
        ax.vlines(x=ordered_df['year'] + width * (i - 1.5), ymin=0, ymax=ordered_df['n'], color=colors[label], alpha=0.7, label=label)
        ax.scatter(ordered_df['year'] + width * (i - 1.5), ordered_df['n'], color=colors[label], alpha=1, marker='o')

    # Add axis title and subtitle
    ax.set_title('Frequency of Different Types of Storms (2010-2022)', weight='heavy', fontsize=12, loc='left', color='#333333')
    ax.set_ylabel('Frequency', weight='bold', fontsize=10, color='#333333')

    # Add grid with light grey color
    ax.yaxis.grid(True, color='#d7d7d7', linestyle=':', linewidth=0.5)

    # Add the legend to the plot
    fig.legend(loc='lower center', fontsize=8, frameon=False, ncol=4)

    # Set figure and axis face color
    fig.patch.set_facecolor('#f6f6f6')
    ax.set_facecolor('#f6f6f6')

    # Remove x and y ticks
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Remove left, right, and top border
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.show()

# Load the data
url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/storms/storms.csv"
df_storm = pd.read_csv(url)

# Process the data
df, df_hurricane, df_tropical_storm, df_tropical_depression, df_tropical_wave = process_data(df_storm)

# Call the function to draw line plot
line_plot(df_hurricane, df_tropical_storm, df_tropical_depression, df_tropical_wave)

# Call the function to draw lolipop plot
lolipop_plot(df)
