import streamlit as st

from utils import load_json, page_header


st.set_page_config(
    page_title="EAC Convention 2026",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

info = load_json("info.json")
links = load_json("links.json")

page_header(info["event_name"], f'{info["dates"]} • {info["city"]}')

col1, col2, col3 = st.columns([1.2, 1, 1])

with col1:
    st.subheader("At a glance")
    st.write(f'**Venue:** {info["venue"]}')
    st.write(f'**Address:** {info["venue_address"]}')
    st.write(f'**Contact:** {info["contact_email"]}')

    st.markdown("### Quick links")
    st.link_button("Convention booking portal", links["convention_booking_portal"])
    st.link_button("Hotel booking (EAC 2026 rate)", links["hotel_booking_portal"])
    st.link_button("Royal Olympic Hotel website", links["hotel_website"])

with col2:
    st.subheader("What this app contains")
    st.write("• Programme & locations (with TBC flags where needed)")
    st.write("• Athens guide (transport, attractions, practical tips)")
    st.write("• Hotel guide (venue overview, amenities, getting there)")
    st.write("• Speakers and EAC Board")
    st.write("• Sponsors / partnering overview")
    st.write("• Safety (Barker) downloads")

    st.info("Skeptical check: If any item is marked **TBC**, treat it as provisional and confirm closer to the event.")

with col3:
    st.subheader("Emergency & essentials")
    for row in info["emergency_numbers"]:
        st.write(f'**{row["service"]}:** {row["number"]}')
    st.markdown("### Local tips")
    for tip in info["local_tips"]:
        st.write(f"• {tip}")

st.markdown("## Notes for organisers")
for n in info["notes"]:
    st.write(f"• {n}")

st.markdown("---")
st.caption("This delegate hub is designed for Streamlit Community Cloud deployment (GitHub-backed).")
