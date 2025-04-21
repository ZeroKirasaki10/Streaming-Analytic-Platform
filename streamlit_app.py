import streamlit as st
import time
from streaming_analytics import StreamingAnalytics
from data_generator import generate_random_value

# Initialize Streaming Analytics
WINDOW_SIZE = 10
TOP_N = 3
analytics = StreamingAnalytics(window_size=WINDOW_SIZE, top_n=TOP_N)

# Streamlit App Layout
st.title("Real-Time Streaming Analytics with Insights")
st.write("This app processes random values continuously and updates metrics, insights, and recommendations in real time.")

# Start/Stop Controls
start = st.button("Start Processing")
stop = st.button("Stop Processing")

# Slider to Adjust Update Speed
speed = st.slider("Update Speed (seconds)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

# Session State Initialization
if "running" not in st.session_state:
    st.session_state.running = False

if start:
    st.session_state.running = True

if stop:
    st.session_state.running = False

# Placeholders for UI Elements
chart_placeholder = st.empty()
metrics_placeholder = st.empty()
insights_placeholder = st.empty()

# Ensure the Loop is Properly Managed
while st.session_state.running:
    # Generate Random Value
    value = generate_random_value()
    analytics.process_data(value)

    # Get Updated Metrics
    metrics = analytics.get_metrics()

    # Update Chart Dynamically
    with chart_placeholder:
        if metrics["sliding_window"]:
            st.line_chart(metrics["sliding_window"])
        else:
            st.write("No data in the sliding window yet.")

    # Update Metrics
    with metrics_placeholder:
        st.subheader("Real-Time Metrics")
        st.metric(label="Moving Average", value=metrics["moving_average"])
        st.write("Sliding Window Values:", metrics["sliding_window"])
        st.write("Top N Values:", metrics["top_n_values"])

    # Provide Real-Time Insights
    with insights_placeholder:
        st.subheader("Insights and Recommendations")
        avg_price = metrics["moving_average"]
        highest_price = max(metrics["top_n_values"]) if metrics["top_n_values"] else 0

        if avg_price > 90:
            st.success("Moving average is high, signaling a potential upward trend. Consider buying!")
        elif avg_price < 60:
            st.warning("Moving average is low, indicating a possible downward trend. Consider selling or monitoring.")
        else:
            st.info("Prices are stable. Keep observing for changes.")

        st.write(f"**Highest Price Observed**: {highest_price}. This may be a resistance level for future trading decisions.")

    # Control the Update Speed
    time.sleep(speed)

# Display a Message When Processing Stops
if not st.session_state.running:
    st.write("Processing has stopped. Click 'Start Processing' to begin again.")