from tracker.tracker import Tracker
from tracker.visualizer import Visualizer
from tracker.system_tracker import log_activity, categorize_activity, get_active_window
import threading
import time

def main():
    # Initialize your tracker and visualizer
    tracker = Tracker()
    visualizer = Visualizer()

    # Start the real-time activity logging in a separate thread
    tracking_thread = threading.Thread(target=log_activity, args=("activity_log.txt", 60))
    tracking_thread.daemon = True
    tracking_thread.start()

    # Track and visualize activities
    while True:
        # Get the current active window and categorize the activity
        active_window = get_active_window()
        if active_window:
            activity_category = categorize_activity(active_window)
            tracker.track_activity(activity_category)
            print(f"Tracked activity: {activity_category}")

        # Visualize the tracked data
        visualizer.visualize_habits(tracker.activities)
        print("Visualized activities")

        # Sleep for a certain interval before tracking again
        time.sleep(120)  # Adjust the interval to 2 minutes for testing

if __name__ == "__main__":
    main()