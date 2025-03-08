import pandas as pd

class Tracker:
    def __init__(self):
        self.data = pd.DataFrame(columns=["activity", "duration"])
        self.activities = []

    def add_hit(self, activity, duration):
        new_hit = pd.DataFrame({"activity": [activity], "duration": [duration]})
        self.data = pd.concat([self.data, new_hit], ignore_index=True)

    def get_data(self):
        return self.data

    def track_activity(self, activity_category):
        # Assuming activity_category is a dictionary with 'activity' and 'duration' keys
        self.activities.append(activity_category)
        print(f"Activity tracked: {activity_category}")

    def calculate_screen_time(self):
        # Logic to calculate the total screen time
        screen_time = sum(activity['duration'] for activity in self.activities if activity['activity'] == 'Browsing')
        print(f"Calculated screen time: {screen_time}")
        return screen_time