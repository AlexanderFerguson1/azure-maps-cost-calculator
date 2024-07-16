import streamlit as st

cost_per_1000_transactions = 3.57

def calculate_cost_per_request(destinations):
    if destinations > 700:
        st.error("Advisers per request cannot be greater than 700")
        return None
    return destinations * (cost_per_1000_transactions / 1000)

st.title("Azure Maps Pricing Calculator")

daily_lead_allocations = st.number_input("Daily Lead Allocations", min_value=1, value=30)
number_of_advisers = st.number_input("Number of Advisers", min_value=1, max_value=700, value=100)

request_cost = calculate_cost_per_request(number_of_advisers)
if request_cost is not None:
    daily_cost = request_cost * daily_lead_allocations
    weekly_cost = daily_cost * 5
    monthly_cost = weekly_cost * 4.345
    yearly_cost = weekly_cost * 52

    st.write(f"£{request_cost:,.2f} per request")
    st.write(f"£{daily_cost:,.2f} per day")
    st.write(f"£{weekly_cost:,.2f} per week")
    st.write(f"£{monthly_cost:,.2f} per month")
    st.write(f"£{yearly_cost:,.2f} per year")