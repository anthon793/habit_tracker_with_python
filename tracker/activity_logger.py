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