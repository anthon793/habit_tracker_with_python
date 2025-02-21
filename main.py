from tracker.tracker import Tracker
from tracker.visualizer import Visualizer

def main():
    tracker = Tracker()
    visualizer = Visualizer()

    # Example usage
    tracker.add_hit("coding", 2)
    tracker.add_hit("screen_time", 1.5)
    tracker.add_hit("reading", 0.5)
    tracker.add_hit("sleep", 8)
    tracker.add_hit("browsing", 3)
    tracker.add_hit("gaming", 2)
    tracker.add_hit("video_calls", 1)
    tracker.add_hit("social_media", 2.5)
    
    
    data = tracker.get_data()
    visualizer.plot(data)

if __name__ == "__main__":
    main()