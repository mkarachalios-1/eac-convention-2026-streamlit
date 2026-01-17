import streamlit as st

from eac_utils import load_json, inject_global_css, top_nav, section_title


links = load_json("links.json")

inject_global_css()
top_nav(links)

section_title("Tools & companion apps", "Optional utilities. Open in a new tab; content may evolve during the season.")

st.markdown(
    "<div class='eac-card'><p>These companion applications provide specialised views that some delegates and organisers may find useful. "
    "Treat outputs as advisory unless explicitly validated for your operational context.</p></div>",
    unsafe_allow_html=True,
)

safety_url = links.get("external_safety_app", "https://airshow-safety-app-test.streamlit.app/")
traj_url = links.get("external_trajectory_app", "https://airshow-trajectory-app.streamlit.app/")

c1, c2 = st.columns(2)
with c1:
    st.markdown(
        "<div class='eac-card'>"
        "<h3>🛡️ Airshow Safety App</h3>"
        "<p>Safety indicators, reference views, and quick checks (beta).</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.link_button("Open safety app", safety_url, use_container_width=True)

with c2:
    st.markdown(
        "<div class='eac-card'>"
        "<h3>📈 Airshow Trajectory App</h3>"
        "<p>Trajectory visualisation and analysis utilities (beta).</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.link_button("Open trajectory app", traj_url, use_container_width=True)

st.caption("If you need these links restricted (e.g., members-only), do not publish them on a public app.")
