import streamlit as st

# Set the browser-tab title, icon and page layout.
st.set_page_config(
    page_title="Football Investment Advisor",
    page_icon="⚽",
    layout="wide",
)

# Display the app name in green.
st.title("⚽ :green[Football Betting Advisor]")

# Explain the app's purpose.
st.write(
    "Explore upcoming football matches and compare both teams’ "
    "recent performance. Our planned machine learning model will "
    "estimate the chances of a home win, draw or away win and "
    "compare them with Sporttip odds to identify potential betting value."
)

# Separate the header from the league selection.
st.divider()
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
