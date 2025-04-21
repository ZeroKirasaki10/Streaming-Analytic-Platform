import random

def generate_random_value():
    """Generate a random value between 50 and 100."""
    return round(random.uniform(50, 100), 2)

def generate_data_stream(count):
    """Generate a stream of random data."""
    return [generate_random_value() for _ in range(count)]