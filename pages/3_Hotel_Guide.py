import streamlit as st
from streamlit.components.v1 import iframe

from utils import load_json, inject_global_css, top_nav, section_title, card


links = load_json("links.json")
info = load_json("info.json")
content = load_json("content.json")

inject_global_css()
top_nav(links)

section_title("Hotel guide", "Royal Olympic Hotel • Convention venue")

left, right = st.columns([1.1, 1])

with left:
    st.markdown(
        f"<div class='eac-card'><h3>🏨 {info['venue']}</h3>"
        f"<p><strong>Address:</strong> {info['venue_address']}<br>"
        f"<strong>Phone:</strong> {links['hotel_phone']}</p></div>",
        unsafe_allow_html=True,
    )

with right:
    # OpenStreetMap embed (no API key). Marker centred on Royal Olympic Hotel.
    lat, lon = 37.9731, 23.7337
    bbox = f"{lon-0.01}%2C{lat-0.006}%2C{lon+0.01}%2C{lat+0.006}"
    url = f"https://www.openstreetmap.org/export/embed.html?bbox={bbox}&layer=mapnik&marker={lat}%2C{lon}"
    iframe(url, height=260)

st.write("")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.link_button("Hotel website", links["hotel_website"])
with c2:
    st.link_button("Hotel booking (EAC 2026 rate)", links["hotel_booking_portal"])
with c3:
    st.link_button("Convention booking portal", links["convention_booking_portal"])
with c4:
    st.link_button("Roof Garden Restaurant", links.get("hotel_roof_restaurant", links["hotel_website"]))

st.subheader("Overview")
st.write(content.get("hotel_blurb", ""))

section_title("Amenities (selected)")
a1, a2 = st.columns(2)
with a1:
    card("Connectivity", "Wi‑Fi is offered; confirm any access limits for group bookings.", icon="📶")
    st.write("")
    card("Services", "24‑hour reception; room service; luggage storage.", icon="🛎️")
with a2:
    card("Practical", "Laundry / dry cleaning; currency exchange; concierge support.", icon="🧺")
    st.write("")
    card("Transport", "Parking and transfers may be available—verify pricing and availability.", icon="🚗")

st.caption("Treat amenities as indicative and confirm with the hotel for special requirements.")

section_title("Organiser checklist")
st.write("• Confirm room allocations and AV requirements for each session.")
st.write("• Confirm exhibition area layout, power availability, and safety constraints.")
st.write("• Confirm dinner seating plan, prize draw mechanics, and awards stage setup.")

st.info("If you provide the final floor plan, this page can display it as an image/PDF for delegates.")
