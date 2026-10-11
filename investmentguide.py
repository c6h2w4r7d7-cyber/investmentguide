import streamlit as st

# Set the browser-tab title, icon and page layout.
st.set_page_config(
    page_title="Football Investment Advisor",
    page_icon="⚽",
    layout="wide",
)

# Fixed header.
st.html("""
<style>
    .fcs-header {
        position: fixed;
        top: 3.75rem;
        left: 0;
        right: 0;
        z-index: 999;
        height: 110px;
        box-sizing: border-box;
        padding: 16px 24px;
        background-color: #123D2A;
        color: #FFFFFF;
        border-bottom: 3px solid #36B878;
    }

    .fcs-header-title {
        margin: 0;
        font-size: clamp(22px, 4vw, 32px);
        font-weight: 700;
        line-height: 1.3;
    }

    .fcs-header-description {
        margin-top: 6px;
        font-size: 14px;
        color: #DDEBE2;
    }
</style>

<header class="fcs-header">
    <div class="fcs-header-title">
        ⚽ Football Betting Advisor
    </div>
    <div class="fcs-header-description">
        Team performance, match predictions and Sporttip odds
    </div>
</header>

<div style="height: 125px;"></div>
""")

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
