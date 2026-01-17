import streamlit as st
import pandas as pd

from utils import load_json, page_header


page_header("Speakers & EAC Board", "Board list is taken from the information pack. Add session speakers as they are confirmed.")

speakers = load_json("speakers.json")

df = pd.DataFrame(speakers)

st.subheader("EAC Board")
board = df[df["type"] == "Board"][["name", "role", "bio"]].copy()
board.rename(columns={"name":"Name", "role":"Role", "bio":"Notes"}, inplace=True)
st.dataframe(board, use_container_width=True, hide_index=True)

st.subheader("Session speakers (to be confirmed)")
st.warning("Populate session speakers once confirmed (name, role, organisation, session). This avoids publishing unverified details.")
st.write("Suggested fields: name • role • organisation • session • biography • contact/links (optional).")

st.info("Edit data/speakers.json to update this page without changing any code.")
