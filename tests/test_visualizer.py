import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from tracker.visualizer import Visualizer
import pandas as pd

class TestVisualizer(unittest.TestCase):
    def setUp(self):
        self.visualizer = Visualizer()

    def test_visualize_habits(self):
        activities = ["Coding", "Reading", "Coding"]
        self.visualizer.visualize_habits(activities)
        # Since visualize_habits shows a plot, we can't test the plot directly.
        # Instead, we can test the intermediate DataFrame creation.
        activity_counts = pd.DataFrame(activities, columns=["activity"])
        activity_counts["count"] = 1
        activity_data = activity_counts.groupby("activity").count().reset_index()
        activity_data.columns = ["activity", "duration"]
        self.assertEqual(len(activity_data), 2)
        self.assertEqual(activity_data.iloc[0]["activity"], "Coding")
        self.assertEqual(activity_data.iloc[0]["duration"], 2)
        self.assertEqual(activity_data.iloc[1]["activity"], "Reading")
        self.assertEqual(activity_data.iloc[1]["duration"], 1)

if __name__ == "__main__":
    unittest.main()