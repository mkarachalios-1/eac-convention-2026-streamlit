import streamlit as st
import pandas as pd

from eac_utils import load_json, inject_global_css, top_nav, section_title, card


links = load_json("links.json")
people = load_json("speakers.json")

inject_global_css()
top_nav(links)

df = pd.DataFrame(people)

section_title("Speakers & EAC Board")

q = st.text_input("Search", value="", placeholder="Type a name, role, or keyword...")

tabs = st.tabs(["🎙 Speakers", "🧭 EAC Board"])


def matches(row: pd.Series) -> bool:
    if not q.strip():
        return True
    hay = f"{row.get('name','')} {row.get('role','')} {row.get('bio','')}".lower()
    return q.strip().lower() in hay


def render_cards(sub: pd.DataFrame, empty_msg: str, show_bio: bool = True) -> None:
    if sub.empty:
        st.info(empty_msg)
        return

    cols = st.columns(2)
    for i, row in enumerate(sub.to_dict(orient="records")):
        with cols[i % 2]:
            bio = (row.get("bio") or "").strip() if show_bio else ""
            bio_html = f"<br><small>{bio}</small>" if bio else ""
            card(row.get("name", ""), f"{row.get('role','')}{bio_html}", icon="👤")
            st.write("")

    with st.expander("Show as table (reference)", expanded=False):
        if show_bio:
            show = sub[["name", "role", "bio"]].rename(
                columns={"name": "Name", "role": "Role", "bio": "Bio"}
            )
        else:
            show = sub[["name", "role"]].rename(columns={"name": "Name", "role": "Role"})
        st.dataframe(show, use_container_width=True, hide_index=True)


with tabs[0]:
    speakers = df[df["type"] == "Speaker"].copy()
    speakers = speakers[speakers.apply(matches, axis=1)]
    render_cards(speakers, "Speaker profiles will appear here as confirmations are published.", show_bio=True)
    st.link_button("Official speaker page", links["speakers_page"])

with tabs[1]:
    board = df[df["type"] == "Board"].copy()
    if q.strip():
        board = board[board.apply(matches, axis=1)]
    render_cards(board, "No board members match your search.", show_bio=False)
    st.link_button(
        "Official EAC Board page",
        links.get("boardmembers_page", "https://www.europeanairshow.org/boardmembers"),
    )
