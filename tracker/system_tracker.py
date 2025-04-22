import psutil
import pygetwindow as gw
import time
from threading import Event

class ActivityLogger:
    def __init__(self):
        self.logged_activities = []

    def log_activity(self, activity, duration):
        # Log the activity with its duration
        self.logged_activities.append({'activity': activity, 'duration': duration})
        print(f"Logged activity: {activity} with duration: {duration}")

    def get_logged_activities(self):
        # Retrieve all logged activities
        return self.logged_activities

def get_running_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        processes.append(proc.info)
    return processes

def get_active_window():
    active_window = gw.getActiveWindow()
    if active_window:
        return active_window.title
    return None

def categorize_activity(window_title):
    print(f"Categorizing activity for window title: {window_title}")
    if "WhatsApp" in window_title:
        print("Detected social media activity")
        return "Social Media"
    elif "Visual Studio Code" in window_title or "VSCode" in window_title:
        print("Detected coding activity")
        return "Coding"
    elif "VLC" in window_title:
        print("Detected movie activity")
        return "Movies"
    elif any(browser in window_title for browser in ["Chrome", "Firefox", "Edge", "Safari", "Opera"]):
        print("Detected browsing activity")
        return "Browsing"
    else:
        print("Detected other activity")
        return "Other"

def log_activity(log_file_path="activity_log.txt", interval=60, stop_event=None):
    activity_logger = ActivityLogger()
    start_time = time.time()

    with open(log_file_path, "a") as log_file:
        while not stop_event.is_set():
            active_window = get_active_window()
            activity_category = categorize_activity(active_window) if active_window else "Unknown"
            running_processes = get_running_processes()

            # Log activity to file
            log_file.write(f"Active window: {active_window}\n")
            log_file.write(f"Activity category: {activity_category}\n")
            log_file.write("Running processes:\n")
            for process in running_processes:
                log_file.write(f"{process}\n")
            log_file.write("\n")
            log_file.flush()
            print(f"Logged activity: {activity_category}")

            # Log activity to ActivityLogger
            elapsed_time = time.time() - start_time
            activity_logger.log_activity(activity_category, int(elapsed_time // 60))
            start_time = time.time()

            time.sleep(interval)  # Log every 'interval' seconds

    # Print all logged activities for debugging
    print("Final logged activities:", activity_logger.get_logged_activities())

def calculate_screen_time(activity_logger):
    activities = activity_logger.get_logged_activities()
    if not activities:
        print("No activities found for screen time calculation.")
        return 0

    total_time = sum(activity['duration'] for activity in activities if 'duration' in activity)
    print(f"Activities considered for screen time: {activities}")
    print(f"Calculated screen time: {total_time} minutes")
    return total_time