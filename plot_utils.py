# ## Plotting function for snow2school...
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_data(x, y, xmin=None, xmax=None):
    """
    Plots x and y data with optional x-axis limits.

    Args:
        x (list or array-like): X-axis data.
        y (list or array-like): Y-axis data.
        xmin (float, optional): Minimum x-axis value. Defaults to None (min of x).
        xmax (float, optional): Maximum x-axis value. Defaults to None (max of x).
    """
    
    # Create a figure and an axes object
    fig, ax = plt.subplots(figsize=(14, 7))

    # Check for xmin and xmax values
    if xmin is not None or xmax is not None:
        if xmin is None:
            xmin = min(x)
        if xmax is None:
            xmax = max(x)
        ax.xlim(xmin, xmax)

    # Plot the temperature data against the date
    ax.plot(x, y, marker='o', linestyle='-', color='skyblue', linewidth=1.5, markersize=5, label='Temperature [°C]')

    # Set the title of the plot with a larger font size
    ax.set_title('Daily Temperature in Uummannaq', fontsize=18)

    # Set more descriptive and styled labels for the x and y axes
    ax.set_xlabel('Date', fontsize=14, fontweight='bold')
    ax.set_ylabel('Temperature [°C]', fontsize=14, fontweight='bold')

    # Add a legend with a larger font size
    ax.legend(fontsize=12)

    # Format the x-axis to display dates nicely
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    date_format = mdates.DateFormatter('%d-%m-%Y')
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

    # Customize the grid lines
    ax.grid(True, linestyle='--', alpha=0.7)

    # Improve tick parameters
    ax.tick_params(axis='both', which='major', labelsize=12)

    # Add horizontal line at 0 degrees Celsius for reference
    ax.axhline(0, color='red', linestyle='--', linewidth=0.8, label='Freezing Point')
    ax.legend(fontsize=12) # Ensure the freezing point legend is also displayed

    # Add a text annotation...
    if not x.empty:
        min_temp = x.min()
        max_temp = x.max()
        ax.text(0.05, 0.95, f'Min Temp: {min_temp}°C\nMax Temp: {max_temp}°C',
                transform=ax.transAxes, fontsize=10, verticalalignment='top',
                bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))

    # Remove top and right spines for a cleaner look (optional)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Display the plot with tight layout
    plt.tight_layout()
    plt.show()