import streamlit as st

# Set the browser-tab title, icon and page layout.
st.set_page_config(
    page_title="Football Investment Advisor",
    page_icon="⚽",
    layout="wide",
)

# Set the header background to dark green and its text to white.
st.html("""
<style>
.st-key-app_header {
    background: #123D2A;
    padding: 20px;
    border-radius: 10px;
    color: white;
}
.st-key-app_header h1 { color: white; }
.st-key-app_header button {
    color: #E5E7EB;
    background: transparent;
}
</style>
""")

# Group the title and information button in one header.
with st.container(key="app_header"):

    # Place the title on the left and the information button on the right.
    title, info = st.columns([10, 2])

    with title:
        # Use a monochrome football icon.
        st.title("Football Betting Advisor", icon=":material/sports_soccer:")

    with info:
        # Show the explanation only when the information button is clicked.
        with st.popover("Info", icon=":material/info:"):
            st.write(
                "Choose a league and match to compare recent team performance. "
                "Our planned model will predict home-win, draw and away-win "
                "probabilities and compare them with Sporttip odds to assess "
                "potential betting value."
            )
            st.caption("Predictions cannot guarantee wins or profits.")

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
