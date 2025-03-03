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
        self.activities.append(activity_category)
        print(f"Activity tracked: {activity_category}")