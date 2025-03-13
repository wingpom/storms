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
    fig.legend(labels=ax.get_legend_handles_labels()[1], loc='lower center', frameon=False, ncol=4)

    plt.show()

def lolipop_plot(df, df_hurricane, df_tropical_storm, df_tropical_depression, df_tropical_wave):

    # Sort the data by year
    ordered_df_hurricane=df_hurricane.sort_values(by='year')
    ordered_df_tropical_storm=df_tropical_storm.sort_values(by='year')
    ordered_df_tropical_depression=df_tropical_depression.sort_values(by='year')
    ordered_df_tropical_wave=df_tropical_wave.sort_values(by='year')
   
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Create a stem plot with stems next to each other per year
    width = 0.2
    ax.vlines(x=ordered_df_hurricane['year'] - width*1.5, ymin=0, ymax=ordered_df_hurricane['n'], color='skyblue', alpha=0.7, label='Hurricanes')
    ax.vlines(x=ordered_df_tropical_storm['year'] - width*0.5, ymin=0, ymax=ordered_df_tropical_storm['n'], color='lightgreen', alpha=0.7, label='Tropical Storms')
    ax.vlines(x=ordered_df_tropical_depression['year'] + width*0.5, ymin=0, ymax=ordered_df_tropical_depression['n'], color='coral', alpha=0.7, label='Tropical Depressions')
    ax.vlines(x=ordered_df_tropical_wave['year'] + width*1.5, ymin=0, ymax=ordered_df_tropical_wave['n'], color='gold', alpha=0.7, label='Tropical Waves')

    ax.scatter(ordered_df_hurricane['year'] - width*1.5, ordered_df_hurricane['n'], color='skyblue', alpha=1)
    ax.scatter(ordered_df_tropical_storm['year'] - width*0.5, ordered_df_tropical_storm['n'], color='lightgreen', alpha=1)
    ax.scatter(ordered_df_tropical_depression['year'] + width*0.5, ordered_df_tropical_depression['n'], color='coral', alpha=1)
    ax.scatter(ordered_df_tropical_wave['year'] + width*1.5, ordered_df_tropical_wave['n'], color='gold', alpha=1)

    # Add axis title and subtitle
    ax.set_title('Frequency of Different Types of Storms (2010-2022)', weight='heavy', fontsize=20, loc='left', color='#333333')
    ax.set_ylabel('Frequency', weight='bold', color='#333333')

    # Add grid with light grey color
    ax.yaxis.grid(True, color='#d7d7d7', linestyle=':', linewidth=0.5)

    # Add the legend to the plot
    fig.legend(labels=ax.get_legend_handles_labels()[1], loc='lower center', frameon=False, ncol=4)

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
lolipop_plot(df, df_hurricane, df_tropical_storm, df_tropical_depression, df_tropical_wave)
