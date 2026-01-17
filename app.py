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
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

info = load_json("info.json")
links = load_json("links.json")
content = load_json("content.json")
tickets = load_json("tickets.json")
speakers = load_json("speakers.json")

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
    st.page_link("pages/0_Tickets.py", label="💶 Tickets & rates", use_container_width=True)
with cta4:
    st.link_button("🏨 Hotel booking", links["hotel_booking_portal"], use_container_width=True)

st.write("")

with st.container(border=True):
    st.markdown(f"**{content.get('new_year_message','')}**")
    st.write(content.get("welcome_text", ""))


section_title("Why attend EAC26")
c1, c2 = st.columns(2)
why = content.get("why_attend", [])
if len(why) >= 4:
    with c1:
        card(why[0]["title"], why[0]["text"], icon="🛡️")
        st.write("")
        card(why[2]["title"], why[2]["text"], icon="🧠")
    with c2:
        card(why[1]["title"], why[1]["text"], icon="🤝")
        st.write("")
        card(why[3]["title"], why[3]["text"], icon="🚀")
else:
    for item in why:
        st.write(f"• **{item['title']}** — {item['text']}")

st.write("")

section_title("What to expect")
expect_cols = st.columns(2)
expect = content.get("what_to_expect", [])
left = "<br>".join([f"• {x}" for x in expect[: len(expect)//2]])
right = "<br>".join([f"• {x}" for x in expect[len(expect)//2 :]])
with expect_cols[0]:
    st.markdown(f"<div class='eac-card'><h3>✨ Experience</h3><p>{left}</p></div>", unsafe_allow_html=True)
with expect_cols[1]:
    st.markdown(f"<div class='eac-card'><h3>🏆 Recognition</h3><p>{right}</p></div>", unsafe_allow_html=True)

st.write("")
section_title("Programme at a glance", "Tap into the detailed programme for timings and locations.")
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
section_title("Tickets", "Prices and availability are controlled by the official booking portal.")
ticket_df = pd.DataFrame(tickets)
headline = ticket_df[ticket_df["ticket_type"].isin(["Full Delegate", "Delegate Guest"])].copy()

tc1, tc2, tc3 = st.columns([1, 1, 1.2])
if not headline.empty and len(headline) >= 2:
    fd = headline.iloc[0]
    dg = headline.iloc[1]
    with tc1:
        card("Full Delegate", f"€{int(fd['price_eur']):,} • {fd['includes']}", icon="🎟")
    with tc2:
        card("Delegate Guest", f"€{int(dg['price_eur']):,} • {dg['includes']}", icon="🥂")
    with tc3:
        st.markdown(
            "<div class='eac-card'><h3>✅ Book confidently</h3>"
            "<p>Use the portal for live availability, workshop rules, and add-ons. "
            "If any published numbers conflict, treat the portal as the source of truth.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
else:
    st.write("Ticket data not found. Update data/tickets.json.")

st.caption("Workshops may have eligibility rules (e.g., invitation-only) and some exhibitor options are add-ons.")

st.write("")
section_title("Speakers – first announcements", "A focused snapshot; the official list can evolve.")
speaker_df = pd.DataFrame(speakers)
sp = speaker_df[speaker_df["type"] == "Speaker"].copy()
if not sp.empty:
    top = sp.head(6)
    s_cols = st.columns(2)
    for i, row in enumerate(top.to_dict(orient="records")):
        with s_cols[i % 2]:
            card(row["name"], f"{row['role']}<br><small>{row.get('bio','')}</small>", icon="🎙")
            st.write("")
    st.page_link("pages/4_Speakers.py", label="View speakers & board →")
else:
    st.info("Speakers will appear here once populated in data/speakers.json.")

st.write("")
section_title("Athens", "History, modern energy, and a walkable centre.")
st.markdown(f"<div class='eac-card'><p>{content.get('host_city','')}</p></div>", unsafe_allow_html=True)

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

st.write("")
with st.expander("Operational notes (for organisers / reviewers)", expanded=False):
    for n in info.get("notes", []):
        st.write(f"• {n}")

st.caption("Built for Streamlit Community Cloud deployment (GitHub-backed).")
