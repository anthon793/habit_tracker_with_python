import unittest
from tracker.visualizer import Visualizer
import pandas as pd

class TestVisualizer(unittest.TestCase):
    def test_plot(self):
        visualizer = Visualizer()
        data = pd.DataFrame({"activity": ["coding", "screen_time"], "duration": [2, 1.5]})
        visualizer.plot(data)  # This will show a plot, you might want to mock plt.show() in real tests

if __name__ == "__main__":
    unittest.main()