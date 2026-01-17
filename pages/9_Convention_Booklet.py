import streamlit as st
from pathlib import Path

from utils import load_json, inject_global_css, top_nav, section_title


links = load_json("links.json")

inject_global_css()
top_nav(links)

section_title("Convention information & travel booklet", "Downloadable reference for delegates")

DOWNLOADS = Path(__file__).resolve().parents[1] / "downloads"
booklet_name = "EAC Convention 2026 Information V1.pdf"
booklet_path = DOWNLOADS / booklet_name

st.write("This booklet consolidates key event details, travel information, and venue guidance. Where details conflict, treat the official online booking portal as the source of truth.")

c1, c2 = st.columns([1, 1])
with c1:
    if booklet_path.exists():
        with open(booklet_path, "rb") as f:
            st.download_button(
                "Download booklet (PDF)",
                data=f,
                file_name=booklet_name,
                mime="application/pdf",
            )
    else:
        st.warning(f"Booklet file not found: {booklet_name}")

with c2:
    st.link_button("Event details & tickets (official)", links["event_details"])

st.caption("Tip: if you prefer a smaller GitHub repository, host the booklet on the EAC website and replace this download with a link.")
