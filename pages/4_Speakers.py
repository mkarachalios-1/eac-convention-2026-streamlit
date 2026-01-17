import streamlit as st
import pandas as pd

from utils import load_json, inject_global_css, top_nav, section_title, card


links = load_json("links.json")
people = load_json("speakers.json")

inject_global_css()
top_nav(links)

df = pd.DataFrame(people)

section_title(
    "Speakers & EAC Board",
    "Speaker lists evolve as confirmations are published. Use the official EAC site for the latest updates.",
)

q = st.text_input("Search names / topics", value="", placeholder="Type a name, role, or keyword…")

tabs = st.tabs(["🎙 Speakers", "🧭 EAC Board"])


def matches(row: pd.Series) -> bool:
    if not q.strip():
        return True
    hay = f"{row.get('name','')} {row.get('role','')} {row.get('bio','')}".lower()
    return q.strip().lower() in hay


def render_cards(sub: pd.DataFrame, empty_msg: str) -> None:
    if sub.empty:
        st.info(empty_msg)
        return
    cols = st.columns(2)
    for i, row in enumerate(sub.to_dict(orient="records")):
        with cols[i % 2]:
            bio = (row.get("bio") or "").strip()
            bio_html = f"<br><small>{bio}</small>" if bio else ""
            card(row.get("name", ""), f"{row.get('role','')}{bio_html}", icon="👤")
            st.write("")

    with st.expander("Show as table (reference)", expanded=False):
        show = sub[["name", "role", "bio"]].rename(
            columns={"name": "Name", "role": "Role", "bio": "Focus / notes"}
        )
        st.dataframe(show, use_container_width=True, hide_index=True)


with tabs[0]:
    section_title("Speakers – first announcements")
    speakers = df[df["type"] == "Speaker"].copy()
    speakers = speakers[speakers.apply(matches, axis=1)]
    render_cards(speakers, "No speakers match your search. If the list is empty, update data/speakers.json.")
    st.link_button("View speaker list (official EAC site)", links["speakers_page"])

with tabs[1]:
    section_title("EAC Board")
    board = df[df["type"] == "Board"].copy()
    if q.strip():
        board = board[board.apply(matches, axis=1)]
    render_cards(board, "No board members match your search.")

st.caption("To update speakers or board members without changing code: edit data/speakers.json.")
