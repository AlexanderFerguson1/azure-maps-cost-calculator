import streamlit as st
import pandas as pd



def calculate_cost_per_request(cost_per_1000_transactions, destinations):
    if destinations > 700:
        st.error("Origins per request cannot be greater than 700")
        return None
    return cost_per_1000_transactions * (destinations / 1000)

st.title("Azure Maps Pricing Calculator")
st.markdown('For Route Matrix, one transaction is counted for every cell in the matrix.')
st.markdown('If you provided 5 origins and 10 destinations, that would be counted as 50 Routing transactions.')
st.markdown('This example we will provide 1 origin which is fixed and 1 - 700 destinations for our matrix.')
st.divider()
cost_per_1000_transactions = st.number_input("Cost per 1000 transactions (£)", value=3.41)
st.divider()
daily_requests = st.slider("Daily Requests made to azure routing api", min_value=1, value=60, max_value=1000)
st.divider()
number_of_destinations = st.slider("Number of Destinations (transactions) per request", min_value=1, max_value=700, value=20)
st.divider()
request_cost = calculate_cost_per_request(cost_per_1000_transactions, number_of_destinations)
# Calculate costs
if request_cost is not None:
    daily_cost = request_cost * daily_requests
    weekly_cost = daily_cost * 5
    monthly_cost = weekly_cost * 4.34524
    yearly_cost = weekly_cost * 52

    # Prepare data for display
    data = {
        'Cost Type': ['Per Request', 'Per Day', 'Per Week', 'Per Month', 'Per Year'],
        'Cost (£)': [f"£{request_cost:,.2f}", f"£{daily_cost:,.2f}", f"£{weekly_cost:,.2f}", f"£{monthly_cost:,.2f}", f"£{yearly_cost:,.2f}"]
    }
    df = pd.DataFrame(data)

    # Display table
    
    st.header('Cost break down', divider='rainbow')
    st.markdown('5 day work week is used for calculation')
    st.table(df)

    # Prepare data for bar chart
    chart_data = {
        'Time Period': ['A - Daily', 'B - Weekly', 'C - Monthly', 'D - Yearly'],
        'Cost (£)': [daily_cost, weekly_cost, monthly_cost, yearly_cost]
    }
    chart_df = pd.DataFrame(chart_data)

    # Display bar chart
    st.bar_chart(chart_df.set_index('Time Period'))