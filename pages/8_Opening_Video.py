import streamlit as st

from eac_utils import load_json, inject_global_css, top_nav, section_title, card


content = load_json("content.json")
links = load_json("links.json")

inject_global_css()
top_nav(links)

section_title(content["opening_video_heading"], "PlanesTV • clip submissions")

st.markdown(f"<div class='eac-card'><p>{content['opening_video_text']}</p></div>", unsafe_allow_html=True)

section_title("How to submit clips")

guidelines = links.get("opening_video_guidelines_url")
upload = links.get("opening_video_upload_url")

g1, g2 = st.columns(2)
with g1:
    if guidelines:
        st.link_button("Submission guidelines", guidelines, use_container_width=True)
    else:
        card("Submission guidelines", "Link: TBC (add it in data/links.json)", icon="📄")
with g2:
    if upload:
        st.link_button("Upload clips (Dropbox)", upload, use_container_width=True)
    else:
        card("Dropbox upload", "Link: TBC (add it in data/links.json)", icon="☁️")

st.warning(
    "Do not publish upload links publicly unless you are confident about access control and moderation. "
    "A controlled submission process reduces spam and IP risks."
)
