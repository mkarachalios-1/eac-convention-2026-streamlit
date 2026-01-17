import streamlit as st

from utils import load_json, page_header


page_header("Athens guide", "Practical travel notes and curated highlights for delegates.")

st.subheader("Arrival & getting into the city")
st.write("• Athens International Airport (ATH) is ~33 km from the city centre.")
st.write("• Typical options: Metro Line 3 (direct), Express bus X95 to Syntagma (24/7), or taxi.")
st.write("• If you are arriving late, pre-booked taxi/transfer reduces uncertainty on pricing and availability.")

st.subheader("Public transport inside Athens")
st.write("• Metro is usually the fastest option for central movement; several stations include archaeological displays.")
st.write("• Walking works well in the historic centre—many streets around the Acropolis are pedestrianised.")
st.write("• Trams/buses extend coverage to coastal areas.")

st.subheader("Must-visit attractions (shortlist)")
st.write("• Acropolis (go early).")
st.write("• Acropolis Museum (directly below the hill).")
st.write("• Plaka & Anafiotika (historic neighbourhoods).")
st.write("• Ancient Agora & Temple of Hephaestus.")
st.write("• Monastiraki Square & flea market.")
st.write("• Mount Lycabettus viewpoint (sunset).")

st.subheader("Food and culture")
st.write("• Traditional dishes: moussaka, souvlaki, fresh seafood, meze-style sharing.")
st.write("• Consider a 'taverna night' for an informal group dinner outside the convention programme.")

st.subheader("Entry requirements")
st.warning("Do not rely on informal sources for visa/entry requirements. Confirm via your government travel advisory and official Greek/Schengen guidance.")

st.subheader("Practicalities")
st.write("• Currency: Euro (€).")
st.write("• Power: Type C/F plugs, 230V/50Hz.")
st.write("• English is widely spoken in tourist areas and hotels.")

st.info("If you want, add curated restaurant/cafe recommendations and walking routes (with Google Maps links).")
