from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import streamlit as st


DATA_DIR = Path(__file__).parent / "data"
ASSETS_DIR = Path(__file__).parent / "assets"


def inject_global_css() -> None:
    """Inject a lightweight, modern style layer.

    Streamlit's theming controls colors and fonts via config.toml, but not
    higher-level layout polish (hero sections, cards, spacing). We keep the CSS
    small and resilient to class-name changes by styling our own HTML elements.
    """

    css = r"""
<style>
  /* Layout: keep content readable on wide screens */
  section.main > div { max-width: 1100px; }
  @media (max-width: 768px) {
    section.main > div { padding-left: 0.9rem; padding-right: 0.9rem; }
  }

  /* Brand bar */
  .eac-brand { display:flex; align-items:center; justify-content:space-between; gap: 12px; }
  .eac-brand small { opacity: 0.75; }

  /* Hero */
  .eac-hero {
    border-radius: 20px;
    padding: 22px 22px 18px 22px;
    border: 1px solid rgba(15, 23, 42, 0.10);
    background:
      radial-gradient(1200px 450px at 15% 0%, rgba(59, 130, 246, 0.20), rgba(255,255,255,0) 60%),
      radial-gradient(900px 380px at 85% 10%, rgba(245, 158, 11, 0.18), rgba(255,255,255,0) 55%),
      linear-gradient(180deg, rgba(255,255,255,0.90), rgba(248,250,252,0.92));
    box-shadow: 0 10px 30px rgba(2, 6, 23, 0.06);
  }
  .eac-hero h1 { margin: 0; font-size: 1.85rem; line-height: 1.2; }
  .eac-hero p { margin: 0.35rem 0 0 0; font-size: 1.0rem; opacity: 0.90; }
  .eac-meta { margin-top: 0.8rem; display: flex; flex-wrap: wrap; gap: 8px; }

  /* Pills */
  .eac-pill {
    display:inline-flex; align-items:center;
    padding: 4px 10px; border-radius: 999px;
    border: 1px solid rgba(15, 23, 42, 0.12);
    background: rgba(255, 255, 255, 0.75);
    font-size: 0.86rem;
  }

  /* Cards */
  .eac-card {
    border-radius: 18px;
    border: 1px solid rgba(15, 23, 42, 0.10);
    background: rgba(255,255,255,0.86);
    box-shadow: 0 8px 22px rgba(2, 6, 23, 0.05);
    padding: 14px 14px 12px 14px;
    height: 100%;
  }
  .eac-card h3 { margin: 0; font-size: 1.05rem; }
  .eac-card p { margin: 0.35rem 0 0 0; opacity: 0.92; }
  .eac-card small { opacity: 0.75; }

  /* Section headers */
  .eac-section-title { margin: 0.4rem 0 0.2rem 0; font-size: 1.25rem; }
  .eac-muted { opacity: 0.80; }

  /* Reduce visual noise */
  div[data-testid="stVerticalBlockBorderWrapper"] { border-radius: 18px; }

  /* Hide Streamlit chrome for delegates */
  #MainMenu { visibility: hidden; }
  header { visibility: hidden; }
  div[data-testid="stToolbar"] { visibility: hidden; }
  div[data-testid="stStatusWidget"] { visibility: hidden; }

  /* Hide Streamlit footer */
  footer { visibility: hidden; }
</style>
"""
    st.markdown(css, unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def load_json(filename: str) -> Any:
    path = DATA_DIR / filename
    return json.loads(path.read_text(encoding="utf-8"))


def pill(text: str) -> str:
    return f"<span class='eac-pill'>{text}</span>"


def brand_bar() -> None:
    """Brand header for all pages (EAC logo + clear app title)."""
    left, right = st.columns([1.15, 1])
    eac_logo = ASSETS_DIR / "eac_logo.png"

    with left:
        if eac_logo.exists():
            st.image(str(eac_logo), width=230)
        else:
            st.markdown("**European Airshow Council**")

    with right:
        st.markdown(
            "<div style='text-align:right;font-weight:800;font-size:1.05rem'>EAC26 Delegate Hub</div>"
            "<div style='text-align:right;opacity:0.72'>Athens, Greece</div>",
            unsafe_allow_html=True,
        )


def page_header(title: str, subtitle: Optional[str] = None) -> None:
    st.markdown(f"# {title}")
    if subtitle:
        st.caption(subtitle)


def hero(title: str, subtitle: str, meta: List[str]) -> None:
    meta_html = "".join([f"<span class='eac-pill'>{m}</span>" for m in meta])
    st.markdown(
        f"""
        <div class="eac-hero">
          <h1>{title}</h1>
          <p>{subtitle}</p>
          <div class="eac-meta">{meta_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def card(title: str, text: str, icon: str = "") -> None:
    icon_html = f"<span style='font-size:1.2rem;margin-right:8px'>{icon}</span>" if icon else ""
    st.markdown(
        f"""
        <div class="eac-card">
          <h3>{icon_html}{title}</h3>
          <p>{text}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_title(title: str, subtitle: str | None = None) -> None:
    st.markdown(f"<div class='eac-section-title'><strong>{title}</strong></div>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<div class='eac-muted'>{subtitle}</div>", unsafe_allow_html=True)


def top_nav(links: Dict[str, str]) -> None:
    """A clean top navigation bar using st.page_link.

    Designed to work with client.showSidebarNavigation=false.
    """
    # Delegate mode: minimise Streamlit chrome
    try:
        st.set_option("client.showSidebarNavigation", False)
        st.set_option("client.toolbarMode", "minimal")
    except Exception:
        pass

    brand_bar()
    st.write("")

    # Compact top nav; wraps naturally on small screens.
    c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns([1.05, 1, 1, 1, 1, 1, 1, 1, 1.2])
    with c1:
        st.page_link("app.py", label="🏠 Home")
    with c2:
        st.page_link("pages/1_Programme.py", label="📅 Programme")
    with c3:
        st.page_link("pages/4_Speakers.py", label="🎙 Speakers")
    with c4:
        st.page_link("pages/3_Hotel_Guide.py", label="🏨 Hotel")
    with c5:
        st.page_link("pages/2_Athens_Guide.py", label="🏛 Athens")
    with c6:
        st.page_link("pages/5_Partners.py", label="🤝 Partners")
    with c7:
        st.page_link("pages/7_Contacts.py", label="☎️ Contacts")
    with c8:
        st.page_link("pages/0_Apps.py", label="🧩 Tools")
    with c9:
        st.link_button("Book now", links.get("register_page", links.get("event_details", "")))


def info_card(title: str, lines: List[str]) -> None:
    with st.container(border=True):
        st.markdown(f"### {title}")
        for ln in lines:
            st.write(ln)
