import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    def __init__(self):
        self.open = True

    def plot(self, data):
        colors = sns.color_palette("husl", len(data["activity"].unique()))
        activity_data = data.groupby("activity").sum()
        
        # Plot each bar with a different color
        fig, ax = plt.subplots()
        activity_data.plot(kind="bar", legend=False, ax=ax)
        for i, bar in enumerate(ax.patches):
            bar.set_color(colors[i % len(colors)])
        
        plt.xlabel("Activity")
        plt.ylabel("Total Duration (hours)")
        plt.title("Time Spent on Different Activities")

        # Connect the close event to the handler
        fig.canvas.mpl_connect('close_event', self.on_close)
        
        plt.show()

    def visualize_habits(self, activities):
        # Convert activities list to a DataFrame
        activity_counts = pd.DataFrame(activities, columns=["activity"])
        activity_counts["count"] = 1
        activity_data = activity_counts.groupby("activity").count().reset_index()
        activity_data.columns = ["activity", "duration"]

        # Plot the data
        self.plot(activity_data)

    def is_open(self):
        # Logic to check if the visualizer tab is still open
        print(f"Visualizer is_open called, returning {self.open}")
        return self.open

    def close(self):
        # Logic to close the visualizer tab
        self.open = False
        print("Visualizer tab closed")

    def on_close(self, event):
        # Event handler for the window close event
        self.close()