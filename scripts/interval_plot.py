#!/usr/bin/env python3
"""
interval_plot.py

"""
import re
import matplotlib.pyplot as plt

# Path to the file
file_path = "../pacificus_vs_somniosidae/intervals_somniosidae"

# Parse the data
data = []
with open(file_path, 'r') as file:
    # Skip the header line
    lines = file.readlines()[1:]
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) < 3:  # Skip lines with insufficient columns
            continue
        try:
            k_val = int(parts[0])
            s_val = int(parts[1])
            regions = re.findall(r'\((\d+), (\d+)\)', parts[2])
            intervals = [(int(start), int(end)) for start, end in regions]
            data.append(((k_val, s_val), intervals))
        except ValueError:
            # Skip lines with parsing errors
            continue
        

# Sort the data by K-val and then S-val
data.sort(key=lambda x: (x[0][0], x[0][1]))


# Prepare data for plotting
param_combinations = [f"({k}, {s})" for (k, s), _ in data]
intervals = [interval for _, interval in data]

# Plot the intervals with parameter combinations on the y-axis
fig, ax = plt.subplots(figsize=(100, 50))  # Substantially larger figure size for readability

for i, interval_list in enumerate(intervals):
    for start, end in interval_list:
        ax.plot([start, end], [i, i], color="blue", marker="|", markersize=8, linewidth=2)

# Customize the plot
ax.set_yticks(range(len(param_combinations)))
ax.set_yticklabels(param_combinations, fontsize=10)
ax.set_ylabel("Parameter Combinations (K, S)", fontsize=80)
ax.set_xlabel("Position w.r.t. reference pacificus CO1 mitochondrial gene (interval values)", fontsize=80)
ax.set_title("Interval Plot of Unique mito-CO1 Sequence Segments for Parameter Combinations K, S up to 150", fontsize=80)

ax.tick_params(axis='x', labelsize=80)

# Add extra spacing between y-axis labels
ax.set_ylim(-1, len(param_combinations) + 1)

plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.tight_layout()

# Save the plot as a high-quality PNG
plt.savefig("../pacificus_vs_somniosidae/interval_plot.png", dpi=100, bbox_inches="tight")
#plt.show()
