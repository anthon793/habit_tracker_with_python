import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def plot(self, data):
        colors = sns.color_palette("husl", len(data["activity"].unique()))
        activity_data = data.groupby("activity").sum()
        
        # Plot each bar with a different color
        ax = activity_data.plot(kind="bar", legend=False)
        for i, bar in enumerate(ax.patches):
            bar.set_color(colors[i % len(colors)])
        
        plt.xlabel("Activity")
        plt.ylabel("Total Duration (hours)")
        plt.title("Time Spent on Different Activities")
        plt.show()