import psutil
import pygetwindow as gw
import time

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
    if "WhatsApp" in window_title:
        return "Social Media"
    elif "Visual Studio Code" in window_title or "VSCode" in window_title:
        return "Coding"
    elif "VLC" in window_title:
        return "Movies"
    elif any(browser in window_title for browser in ["Chrome", "Firefox", "Edge", "Safari", "Opera"]):
        return "Browsing"
    else:
        return "Other"

def log_activity(log_file_path="activity_log.txt", interval=60):
    with open(log_file_path, "a") as log_file:
        while True:
            active_window = get_active_window()
            activity_category = categorize_activity(active_window) if active_window else "Unknown"
            running_processes = get_running_processes()
            log_file.write(f"Active window: {active_window}\n")
            log_file.write(f"Activity category: {activity_category}\n")
            log_file.write("Running processes:\n")
            for process in running_processes:
                log_file.write(f"{process}\n")
            log_file.write("\n")
            log_file.flush()
            print(f"Logged activity: {activity_category}")
            time.sleep(interval)  # Log every 'interval' seconds