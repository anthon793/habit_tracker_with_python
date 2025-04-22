from tracker.tracker import Tracker
from tracker.visualizer import Visualizer
from tracker.visualizer import Visualizer
from tracker.system_tracker import log_activity, categorize_activity, get_active_window, ActivityLogger, calculate_screen_time
import threading
import time

def main():
    # Initialize the activity logger and visualizer
    activity_logger = ActivityLogger()
    visualizer = Visualizer()

    # Create a stop event for the logging thread
    stop_event = threading.Event()

    # Start the real-time activity logging in a separate thread
    tracking_thread = threading.Thread(target=log_activity, args=("activity_log.txt", 60, stop_event))
    tracking_thread.daemon = True
    tracking_thread.start()

    # Track and visualize activities
    visualizer_open = True
    while visualizer_open:
        # Get the current active window and categorize the activity
        active_window = get_active_window()
        print(f"Active window: {active_window}")
        if active_window:
            activity_category = categorize_activity(active_window)
            print(f"Categorized activity: {activity_category}")
            # Log the activity with a fixed duration (e.g., 10 minutes for testing)
            activity_logger.log_activity(activity_category, 10)
            print(f"Tracked activity: {{'activity': {activity_category}, 'duration': 10}}")

        # Visualize the tracked data
        visualizer.visualize_habits(activity_logger.get_logged_activities())
        print("Visualized activities")

        # Check if the visualizer tab is closed
        visualizer_open = visualizer.is_open()
        print(f"Visualizer is_open called, returning {visualizer_open}")

        # Sleep for a certain interval before tracking again
        time.sleep(10)  # Adjust the interval to 10 seconds for testing

    # Calculate and print the screen time when the visualizer tab is closed
    screen_time = calculate_screen_time(activity_logger)
    print(f"Total screen time: {screen_time} minutes")

    # Stop the logging thread and end the program
    print("Stopping the tracker and ending the program.")
    stop_event.set()
    tracking_thread.join()

if __name__ == "__main__":
    main()