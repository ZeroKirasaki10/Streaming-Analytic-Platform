from collections import deque
import heapq

class StreamingAnalytics:
    def __init__(self, window_size, top_n):
        self.sliding_window = deque(maxlen=window_size)
        self.window_sum = 0
        self.top_n = top_n
        self.top_n_values = []

    def process_data(self, value):
        """Process a single data point."""
        self.update_sliding_window(value)
        self.update_top_n_values(value)

    def update_sliding_window(self, value):
        """Update the sliding window and calculate sum."""
        self.sliding_window.append(value)
        self.window_sum = sum(self.sliding_window)

    def update_top_n_values(self, value):
        """Maintain top N values."""
        self.top_n_values.append(value)
        self.top_n_values.sort(reverse=True)
        if len(self.top_n_values) > self.top_n:
            self.top_n_values.pop()

    def get_metrics(self):
        """Calculate and return metrics."""
        if len(self.sliding_window) == 0:
            return {
                "sliding_window": [],
                "moving_average": 0,
                "top_n_values": []
            }
        moving_average = self.window_sum / len(self.sliding_window)
        return {
            "sliding_window": list(self.sliding_window),
            "moving_average": round(moving_average, 2),
            "top_n_values": self.top_n_values[:self.top_n]
        }