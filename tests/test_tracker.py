import unittest
from tracker.tracker import Tracker

class TestTracker(unittest.TestCase):
    def test_add_hit(self):
        tracker = Tracker()
        tracker.add_hit("coding", 2)
        self.assertEqual(len(tracker.get_data()), 1)

if __name__ == "__main__":
    unittest.main()