import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from tracker.system_tracker import log_activity, categorize_activity, get_active_window

class TestSystemTracker(unittest.TestCase):
    @patch('tracker.system_tracker.get_active_window')
    @patch('tracker.system_tracker.categorize_activity')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_log_activity(self, mock_open, mock_categorize_activity, mock_get_active_window):
        mock_get_active_window.return_value = "Test Window"
        mock_categorize_activity.return_value = "Test Category"
        
        with patch('tracker.system_tracker.time.sleep', return_value=None):
            log_activity("test_log.txt", 1)
        
        mock_open.assert_called_once_with("test_log.txt", "a")
        mock_open().write.assert_called_with("Test Category\n")

    def test_categorize_activity(self):
        self.assertEqual(categorize_activity("Google Chrome"), "Browsing")
        self.assertEqual(categorize_activity("Microsoft Word"), "Writing")
        self.assertEqual(categorize_activity("Unknown App"), "Other")

    @patch('pygetwindow.getActiveWindow')
    def test_get_active_window(self, mock_get_active_window):
        mock_get_active_window.return_value = None
        self.assertIsNone(get_active_window())

        mock_get_active_window.return_value = unittest.mock.Mock(title="Test Window")
        self.assertEqual(get_active_window(), "Test Window")

if __name__ == "__main__":
    unittest.main()