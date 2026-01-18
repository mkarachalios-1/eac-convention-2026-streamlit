import streamlit as st

from eac_utils import load_json, inject_global_css, top_nav, section_title, card


links = load_json("links.json")
content = load_json("content.json")

inject_global_css()
top_nav(links)

section_title("Athens guide", "Practical travel notes and curated highlights for delegates.")

st.markdown(f"<div class='eac-card'><p>{content.get('host_city','')}</p></div>", unsafe_allow_html=True)

section_title("Travel to Athens")
tcols = st.columns(2)
travel = content.get("travel_to_athens", [])
with tcols[0]:
    card("By air", "Athens International Airport (ATH) with Metro Line 3, express buses, and taxis.", icon="✈️")
with tcols[1]:
    card("By sea", "Piraeus Port offers island connections and ferry links.", icon="⛴️")

st.write("")
card("Getting around", "Modern Metro, tram, and bus network; central areas are walkable.", icon="🚇")

section_title("Arrival & getting into the city")
a1, a2 = st.columns(2)
with a1:
    card("Airport → centre", "Metro Line 3, X95 bus (Syntagma), or taxi/private transfer.", icon="🧳")
with a2:
    card("Late arrivals", "Consider pre-booked transfers to reduce pricing and availability uncertainty.", icon="🌙")

section_title("Getting around")
g1, g2 = st.columns(2)
with g1:
    card("Metro", "Fast for central movement; some stations include archaeological displays.", icon="🚇")
with g2:
    card("Walkability", "Historic centre is pedestrian-friendly; plan comfortable shoes.", icon="👟")

section_title("Must-visit shortlist")
ml, mr = st.columns(2)
with ml:
    st.markdown(
        "<div class='eac-card'><h3>🏛️ Classics</h3><p>• Acropolis (go early)<br>• Acropolis Museum<br>• Ancient Agora & Temple of Hephaestus</p></div>",
        unsafe_allow_html=True,
    )
with mr:
    st.markdown(
        "<div class='eac-card'><h3>🌆 Neighbourhoods & views</h3><p>• Plaka & Anafiotika<br>• Monastiraki & flea market<br>• Lycabettus viewpoint (sunset)</p></div>",
        unsafe_allow_html=True,
    )

section_title("Food & culture")
card("Rooftop dining", "Popular in central Athens—reserve ahead during busy periods.", icon="🍽️")

section_title("Entry requirements")
st.warning(
    "Confirm visa/entry requirements via official government sources (your country guidance and official Greek/Schengen rules)."
)

section_title("Practicalities")
p1, p2 = st.columns(2)
with p1:
    card("Currency", "Euro (€)", icon="💶")
    st.write("")
    card("Power", "Type C/F, 230V/50Hz", icon="🔌")
with p2:
    card("Language", "English widely spoken in tourist areas and hotels", icon="🗣️")
    st.write("")
    card("Delegate tip", "Plan a short walk in Plaka after sessions—Athens works well as a compact city break.", icon="🗺️")
