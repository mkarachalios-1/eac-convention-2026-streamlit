import streamlit as st

from eac_utils import load_json, inject_global_css, top_nav, section_title, card


info = load_json("info.json")
links = load_json("links.json")

inject_global_css()
top_nav(links)

section_title("Contacts", "Keep escalation paths clear and short for delegates.")

c1, c2 = st.columns(2)
with c1:
    card("EAC Convention", f"General enquiries: <strong>{info['contact_email']}</strong>", icon="📨")
with c2:
    card("Venue", f"{info['venue']}<br><small>{info['venue_address']}</small>", icon="🏨")

st.write("")
card("Hotel phone", links["hotel_phone"], icon="📞")
st.link_button("Hotel website", links["hotel_website"])

st.write("")
section_title("Emergency")

e1, e2 = st.columns(2)
nums = info.get("emergency_numbers", [])
for i, row in enumerate(nums):
    with (e1 if i % 2 == 0 else e2):
        card(row.get("service", ""), row.get("number", ""), icon="🆘")
        st.write("")

st.warning(
    "If this app is public, avoid publishing personal mobile numbers without consent. "
    "Prefer role-based inboxes and venue reception numbers."
)
