
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from tracker.tracker import Tracker

class TestTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = Tracker()

    def test_initial_data(self):
        self.assertTrue(self.tracker.data.empty)
        self.assertEqual(self.tracker.activities, [])

    def test_add_hit(self):
        self.tracker.add_hit("Coding", 2)
        self.assertEqual(len(self.tracker.data), 1)
        self.assertEqual(self.tracker.data.iloc[0]["activity"], "Coding")
        self.assertEqual(self.tracker.data.iloc[0]["duration"], 2)

    def test_track_activity(self):
        self.tracker.track_activity("Coding")
        self.assertEqual(self.tracker.activities, ["Coding"])

if __name__ == "__main__":
    unittest.main()