import streamlit as st

from utils import load_json, page_header


links = load_json("links.json")
info = load_json("info.json")

page_header("Hotel guide", "Royal Olympic Hotel • Convention venue")

st.subheader("Venue")
st.write(f'**Hotel:** {info["venue"]}')
st.write(f'**Address:** {info["venue_address"]}')
st.write(f'**Phone:** {links["hotel_phone"]}')

c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("Hotel website", links["hotel_website"])
with c2:
    st.link_button("Hotel booking (EAC 2026 rate)", links["hotel_booking_portal"])
with c3:
    st.link_button("Convention booking portal", links["convention_booking_portal"])

st.subheader("What to expect (from the information pack)")
st.write("• Five-star, family-run property in central Athens.")
st.write("• Near Temple of Zeus, National Garden, and close to the Acropolis / Acropolis Museum.")
st.write("• Roof Garden Restaurant & Bar with Acropolis views (used for Gala Dinner).")

st.subheader("Amenities (selected)")
st.write("• Wi‑Fi (complimentary, per info pack)")
st.write("• 24-hour room service (per info pack)")
st.write("• Laundry / dry cleaning; luggage storage; currency exchange")
st.write("• Valet parking (verify availability and pricing)")
st.write("• Upon request: babysitting, transfer, indoor parking, massage")
st.caption("Treat these as indicative and confirm with the hotel if you have special requirements.")

st.subheader("Organiser checklist")
st.write("• Confirm room allocations and AV requirements for each session.")
st.write("• Confirm exhibition area layout, power availability, and safety constraints.")
st.write("• Confirm dinner seating plan, prize draw mechanics, and awards stage setup.")

st.info("If you provide the final floor plan, this page can display it as an image/PDF for delegates.")
