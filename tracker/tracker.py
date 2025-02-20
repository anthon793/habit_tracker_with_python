import pandas as pd

class Tracker:
    def __init__(self):
        self.data = pd.DataFrame(columns=["activity", "duration"])

    def add_hit(self, activity, duration):
        new_hit = pd.DataFrame({"activity": [activity], "duration": [duration]})
        self.data = pd.concat([self.data, new_hit], ignore_index=True)

    def get_data(self):
        return self.data