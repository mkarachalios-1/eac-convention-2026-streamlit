import streamlit as st
import pandas as pd

from eac_utils import (
    load_json,
    inject_global_css,
    top_nav,
    hero,
    section_title,
    card,
    pill,
)


st.set_page_config(
    page_title="EAC Convention 2026",
    page_icon="assets/eac_logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

info = load_json("info.json")
links = load_json("links.json")
content = load_json("content.json")
people = load_json("speakers.json")

inject_global_css()
top_nav(links)

hero(
    info["event_name"],
    f"{content['announcement_title']} — {content['announcement_subtitle']}",
    [info["dates"], info["city"], info["venue"], links.get("eac_hashtag", "#EAC26")],
)

st.write("")

cta1, cta2, cta3, cta4 = st.columns([1, 1, 1, 1])
with cta1:
    st.link_button("🎟 Book / register", links["register_page"], use_container_width=True)
with cta2:
    st.page_link("pages/1_Programme.py", label="📅 Programme", use_container_width=True)
with cta3:
    st.page_link("pages/3_Hotel_Guide.py", label="🏨 Hotel guide", use_container_width=True)
with cta4:
    st.page_link("pages/0_Apps.py", label="🧩 Tools", use_container_width=True)

st.write("")

with st.container(border=True):
    st.markdown(f"**{content.get('welcome_message','')}**")
    st.write(content.get("welcome_text", ""))


section_title("What is EAC26")
cols = st.columns(2)
items = content.get("what_is_eac26", [])
for i, it in enumerate(items):
    with cols[i % 2]:
        card(it.get("title", ""), it.get("text", ""), icon=it.get("icon", "✈️"))
        st.write("")

st.write("")
section_title("Programme at a glance", "Use the Programme page for timings and locations.")
pg = content.get("programme_glance", {})
cols = st.columns(3)
for i, (day, items) in enumerate(pg.items()):
    bullets = "<br>".join([f"• {x}" for x in items])
    with cols[i % 3]:
        st.markdown(
            f"<div class='eac-card'><h3>📍 {day}</h3><p>{bullets}</p></div>",
            unsafe_allow_html=True,
        )

st.write("")
section_title("Speakers")
df = pd.DataFrame(people)
sp = df[df["type"] == "Speaker"].copy()
if not sp.empty:
    top = sp.head(6)
    s_cols = st.columns(2)
    for i, row in enumerate(top.to_dict(orient="records")):
        with s_cols[i % 2]:
            bio = (row.get("bio") or "").strip()
            bio_html = f"<br><small>{bio}</small>" if bio else ""
            card(row["name"], f"{row['role']}{bio_html}", icon="🎙")
            st.write("")
    st.page_link("pages/4_Speakers.py", label="View all speakers & board →")
else:
    st.info("Speakers will appear here as the programme is finalised.")

st.write("")
section_title("Tools")
t1, t2 = st.columns(2)
with t1:
    st.markdown(
        "<div class='eac-card'><h3>🛡️ Airshow Safety & Excellence Dashboard</h3>"
        "<p>Safety indicators and reference views.</p></div>",
        unsafe_allow_html=True,
    )
    st.link_button(
        "Open dashboard",
        links.get("external_safety_app", "https://airshow-safety-app-test.streamlit.app/"),
        use_container_width=True,
    )
with t2:
    st.markdown(
        "<div class='eac-card'><h3>📈 Airshow Trajectory App</h3>"
        "<p>Trajectory visualisation and analysis utilities.</p></div>",
        unsafe_allow_html=True,
    )
    st.link_button(
        "Open trajectory app",
        links.get("external_trajectory_app", "https://airshow-trajectory-app.streamlit.app/"),
        use_container_width=True,
    )

st.write("")
section_title("Athens")
st.markdown(
    f"<div class='eac-card'><p>{content.get('host_city','')}</p></div>",
    unsafe_allow_html=True,
)

st.write("")
section_title("Venue & essentials")
v1, v2 = st.columns([1.2, 1])
with v1:
    st.markdown(
        f"<div class='eac-card'><h3>🏨 {info['venue']}</h3>"
        f"<p><strong>Address:</strong> {info['venue_address']}<br>"
        f"<strong>Enquiries:</strong> {info['contact_email']}</p></div>",
        unsafe_allow_html=True,
    )
    st.write("")
    q1, q2, q3, q4 = st.columns(4)
    with q1:
        st.link_button("Event details", links["event_details"], use_container_width=True)
    with q2:
        st.link_button("Hotel site", links["hotel_website"], use_container_width=True)
    with q3:
        st.link_button("Speakers", links["speakers_page"], use_container_width=True)
    with q4:
        st.link_button("Partners", links["partners_page"], use_container_width=True)

with v2:
    st.markdown("<div class='eac-card'><h3>🆘 Emergency</h3>", unsafe_allow_html=True)
    for row in info.get("emergency_numbers", []):
        st.write(f"**{row['service']}:** {row['number']}")
    st.markdown("</div>", unsafe_allow_html=True)
