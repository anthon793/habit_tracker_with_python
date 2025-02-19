import matplotlib.pyplot as plt

class Visualizer:
    def plot(self, data):
        data.groupby("activity").sum().plot(kind="bar")
        plt.show()