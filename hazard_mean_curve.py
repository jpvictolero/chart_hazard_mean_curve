import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load CSV file
file_path = "sample.csv"
df = pd.read_csv(file_path)

# Transpose DataFrame with Period as index
df_transposed = df.set_index("Period").T

# Extract X values and Convert to float
x_values = df_transposed.index.astype(float)

# Extract Y values (Mean Hazard Curves) and Convert to float
pga_values = df_transposed["PGA"].astype(float)
ss_values = df_transposed["Ss"].astype(float)
s1_values = df_transposed["S1"].astype(float)

# Create plot with log-log scale.
# ax is the axis object
# fig is the figure object
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xscale("log")
ax.set_yscale("log")

# Plot hazard curves
# Use linestyle="-" solid line, color="blue" is blue color
# label is used for legend
ax.plot(x_values, pga_values,color="blue", label="PGA")
ax.plot(x_values, ss_values, color="red", label="Ss")
ax.plot(x_values, s1_values, color="green", label="S1")

# Labels and Title with fontsize
ax.set_xlabel("Label for x-axis", fontsize=12)
ax.set_ylabel("Label for y-axis", fontsize=12)
ax.set_title("Title", fontsize=14)

# Ensure only unique labels in the legend and Remove duplicates
# Handles are the lines, labels are the text
handles, labels = ax.get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))
ax.legend(unique_labels.values(), unique_labels.keys())

# Disable minor ticks
ax.xaxis.set_minor_locator(ticker.NullLocator())
ax.yaxis.set_minor_locator(ticker.NullLocator())

# Set major ticks and labels for x-axis
x_labels = [0.0001, 0.000172, 0.000296, 0.0005092, 0.0008761, 0.0015073, 
            0.0025932, 0.0044613, 0.0076754, 0.0132051, 0.0227185, 0.0390857, 
            0.0672443, 0.1156894, 0.1990359, 0.3424281, 0.5891249, 1.0135504, 
            1.7437463, 3]
ax.set_xticks(x_labels)
ax.set_xticklabels([str(x) for x in x_labels], rotation=45)

# Set major ticks and labels for y-axis
# Use scientific notation for y-axis and Replace with string
y_labels = [1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1e0]
ax.set_yticks(y_labels)
ax.set_yticklabels(["0.0000001", "0.0000010", "0.0000100", "0.0001000", 
                     "0.0010000", "0.0100000", "0.1000000", "1.000000"], rotation=45)

# Enable major grid only
# which is major grid, linestyle is dashed, linewidth is 0.5
ax.grid(True, which="major", linestyle="--", linewidth=0.5)

# Show plot
plt.show()
