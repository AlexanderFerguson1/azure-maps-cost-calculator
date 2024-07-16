import streamlit as st
import pandas as pd

def calculate_cost_per_request(cost_per_1000_transactions, destinations):
    if destinations > 700:
        st.error("Origins per request cannot be greater than 700")
        return None
    return destinations * (cost_per_1000_transactions / 1000)

st.title("Azure Maps Pricing Calculator")

# Input fields
cost_per_1000_transactions = st.number_input("Cost per 1000 transactions", value=3.57)
daily_requests = st.slider("Daily Requests", min_value=1, value=30)
number_of_destinations = st.slider("Number of Destinations", min_value=1, max_value=700, value=100)

# Calculate costs
request_cost = calculate_cost_per_request(cost_per_1000_transactions, number_of_destinations)
if request_cost is not None:
    daily_cost = request_cost * daily_requests
    weekly_cost = daily_cost * 5
    monthly_cost = weekly_cost * 4.345
    yearly_cost = weekly_cost * 52

    # Display costs
    st.write(f"£{request_cost:,.2f} per request")
    st.write(f"£{daily_cost:,.2f} per day")
    st.write(f"£{weekly_cost:,.2f} per week")
    st.write(f"£{monthly_cost:,.2f} per month")
    st.write(f"£{yearly_cost:,.2f} per year")

    # Prepare data for bar chart
    data = {
        'Time Period': ['Daily', 'Weekly', 'Monthly', 'Yearly'],
        'Cost (£)': [daily_cost, weekly_cost, monthly_cost, yearly_cost]
    }
    df = pd.DataFrame(data)

    # Display bar chart
    st.bar_chart(df.set_index('Time Period'))
