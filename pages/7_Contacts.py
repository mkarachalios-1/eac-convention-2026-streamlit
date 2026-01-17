import streamlit as st

from utils import load_json, page_header


info = load_json("info.json")
links = load_json("links.json")

page_header("Contacts", "Keep escalation paths clear and short for delegates.")

st.subheader("EAC Convention")
st.write(f"**General enquiries:** {info['contact_email']}")

st.subheader("Venue")
st.write(f"**Hotel:** {info['venue']}")
st.write(f"**Address:** {info['venue_address']}")
st.write(f"**Phone:** {links['hotel_phone']}")
st.link_button("Hotel website", links["hotel_website"])

st.subheader("Emergency")
for row in info["emergency_numbers"]:
    st.write(f"**{row['service']}:** {row['number']}")

st.warning("If you publish this app publicly, avoid posting personal mobile numbers without consent. Prefer role-based emails and venue reception numbers.")
