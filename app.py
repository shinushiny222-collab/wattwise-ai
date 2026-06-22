import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

USERS_FILE = "users.csv"

if not os.path.exists(USERS_FILE):
    pd.DataFrame(
        columns=["username", "password"]
    ).to_csv(USERS_FILE, index=False)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("⚡ WattWise AI")

    menu = st.radio(
        "Select",
        ["Login", "Register"]
    )

    if menu == "Register":

        st.subheader("Create Account")

        new_user = st.text_input(
            "Username"
        )

        new_pass = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Register"):

            users = pd.read_csv(USERS_FILE)

            if new_user in users["username"].values:
                st.error(
                    "Username already exists"
                )

            else:

                users.loc[len(users)] = [
                    new_user,
                    new_pass
                ]

                users.to_csv(
                    USERS_FILE,
                    index=False
                )

                st.success(
                    "Registration Successful"
                )

    else:

        st.subheader("Login")

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            users = pd.read_csv(
                USERS_FILE
            )

            valid = (
                (users["username"] == username)
                &
                (users["password"] == password)
            )

            if valid.any():

                st.session_state.logged_in = True
                st.session_state.user = username

                st.success(
                    "Login Successful"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid Username or Password"
                )

    st.stop()

# Page Config
st.set_page_config(
    page_title="WattWise AI",
    page_icon="⚡",
    layout="wide"
)

# Title
st.title("⚡ WattWise AI")
st.subheader("Smart Electricity Consumption Analyzer")
st.sidebar.title("⚡ WattWise AI")
st.sidebar.info("""
AI Powered Electricity Saving Assistant

SDG 7: Affordable and Clean Energy
SDG 13: Climate Action
""")
st.sidebar.write(
    f"👤 {st.session_state.user}"
)

if st.sidebar.button("Logout"):

    st.session_state.logged_in = False

    st.rerun()
GEMINI_API_KEY = "AQ.Ab8RN6KEINEUJT0smRh-lqEN5gHNjGtJi3C-gD9Bauekrhc-Cw"
# ---------------- AI Energy Agent ----------------

def energy_agent(appliance, current_units, monthly_cost):

    if current_units >= 300:
        status = "High Usage"
        action = "Recommend immediate power-saving measures."

    elif current_units >= 150:
        status = "Moderate Usage"
        action = "Suggest optimization of appliance usage."

    else:
        status = "Low Usage"
        action = "Encourage maintaining efficient energy habits."

    return status, action
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# Load appliance data
data = pd.read_csv("appliances.csv")

st.header("Appliance Energy Calculator")

# Appliance selection
appliance = st.selectbox(
    "Select an Appliance",
    data["Appliance"]
)

# Get watts
watts = data.loc[
    data["Appliance"] == appliance,
    "Watts"
].values[0]

# Hours input
hours = st.number_input(
    "Hours Used Per Day",
    min_value=1,
    max_value=24,
    value=5
)

# Calculation
daily_units = (watts * hours) / 1000
monthly_units = daily_units * 30

rate = 8  # ₹ per unit
cost = monthly_units * rate

# Results
st.success(f"Monthly Units Consumed: {monthly_units:.2f} Units")
st.success(f"Estimated Monthly Cost: ₹{cost:.2f}")

# Bill Analyzer
st.header("📊 Bill Analyzer")

previous = st.number_input(
    "Previous Month Units",
    min_value=0,
    value=200
)

current = st.number_input(
    "Current Month Units",
    min_value=0,
    value=250
)

difference = current - previous

usage_status, agent_action = energy_agent(
    appliance,
    current,
    cost
)
if difference > 0:
    st.warning(
        f"Your usage increased by {difference} units."
    )

    st.info("""
    Energy Saving Tips:
    • Use LED bulbs
    • Switch off unused appliances
    • Use AC at 24–26°C
    • Unplug chargers when not in use
    """)

elif difference < 0:
    st.success(
        f"Great! You reduced usage by {abs(difference)} units."
    )

else:
    st.info("Usage remains the same.")
# ---------------- Agentic AI Display ----------------

st.header("🤖 Agentic AI Analysis")

st.success(f"Usage Status: {usage_status}")

st.info(f"Agent Decision: {agent_action}")
score = max(0, 100 - int(current/5))

st.header("🏆 Energy Efficiency Score")

st.progress(score/100)

st.write(f"Your Energy Score: {score}/100")
# Dashboard
st.header("📈 Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Monthly Units",
        round(monthly_units, 2)
    )

with col2:
    st.metric(
        "Estimated Cost",
        f"₹{round(cost,2)}"
    )
chart_data = pd.DataFrame({
    "Month": ["Previous", "Current"],
    "Units": [previous, current]
})

st.header("📊 Usage Comparison")

st.bar_chart(
    chart_data.set_index("Month")
)
tips = pd.read_csv("energy_tips.csv")
# RAG Retrieval

filtered = tips[tips["Appliance"] == appliance]

if not filtered.empty:
    retrieved_tip = filtered["Tip"].iloc[0]
else:
    retrieved_tip = "Use energy efficiently."

st.header("🤖 WattWise AI Assistant")

if st.button("Generate AI Suggestions"):
    prompt = f"""
    You are an Energy Saving Expert.
    Knowledge Base:
    {retrieved_tip}
    User Details:
    Appliance: {appliance}
    Power: {watts} W
    Hours Used: {hours}
    Monthly Units: {monthly_units}
    Monthly Cost: ₹{cost}
    Current Bill Units: {current}

    Use the knowledge base while answering.

    Generate:
    1. Personalized Suggestions
    2. Ways to Reduce Bill
    3. Estimated Savings
    Explain how to reduce electricity bill.
    """

    response = model.generate_content(prompt)

    st.write(response.text)
st.header("📋 AI Energy Report")

if st.button("Generate AI Report"):

    prompt = f"""
    Previous Units: {previous}
    Current Units: {current}
    Monthly Units: {monthly_units}
    Monthly Cost: ₹{cost}

    Generate:
    1. Usage Summary
    2. Problem Analysis
    3. Energy Saving Suggestions
    4. Final Recommendation
    """

    response = model.generate_content(prompt)

    st.success("Report Generated")
    st.write(response.text)

# Footer
st.markdown("---")
st.caption(
    "WattWise AI | SDG 7 - Affordable and Clean Energy"
)
