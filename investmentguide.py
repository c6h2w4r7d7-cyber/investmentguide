import streamlit as st

# Set the browser-tab title, icon and page layout.
st.set_page_config(
    page_title="Football Investment Advisor",
    page_icon="⚽",
    layout="wide",
)

# Display the app name.
st.title("⚽ Football Betting Advisor")

# Explain the purpose of the app.
st.write(
  "Compare football team performance, match predictions "
  "and Sporttip betting odds."  
)

# Display the league selection section.
st.subheader("Select a football league")

# Create a dropdown and store the user's selection.
selected_league = st.selectbox(
    "League",
    options=["Swiss Super League (Switzerland)",
             "Premier League (England)",
             "La Liga (Spain)"],
    index=None,
    placeholder= "Choose a league...",
    key="league selection",
)
# Show which league the user selected.
if selected_league is not None:
    st.write(f"Selected league: **{selected_league}**")
