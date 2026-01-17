from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import streamlit as st


DATA_DIR = Path(__file__).parent / "data"


@st.cache_data(show_spinner=False)
def load_json(filename: str) -> Any:
    path = DATA_DIR / filename
    return json.loads(path.read_text(encoding="utf-8"))


def pill(text: str) -> str:
    return f"<span style='display:inline-block;padding:2px 10px;border-radius:999px;background:#f1f5f9;border:1px solid #e2e8f0;font-size:0.85rem;margin-right:6px'>{text}</span>"


def page_header(title: str, subtitle: Optional[str] = None) -> None:
    st.markdown(f"# {title}")
    if subtitle:
        st.caption(subtitle)
    st.markdown("---")


def info_card(title: str, lines: List[str]) -> None:
    with st.container(border=True):
        st.markdown(f"### {title}")
        for ln in lines:
            st.write(ln)
