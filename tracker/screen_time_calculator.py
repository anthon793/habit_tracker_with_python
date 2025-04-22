class ScreenTimeCalculator:
    def __init__(self, activity_logger):
        self.activity_logger = activity_logger

    def calculate_screen_time(self):
        # Retrieve logged activities
        activities = self.activity_logger.get_logged_activities()
        if not activities:
            print("No activities found for screen time calculation.")
            return 0

        # Calculate total screen time
        total_time = sum(activity['duration'] for activity in activities if 'duration' in activity)
        print(f"Activities considered for screen time: {activities}")
        print(f"Calculated screen time: {total_time} minutes")
        return total_time