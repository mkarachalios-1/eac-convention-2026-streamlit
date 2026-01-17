# EAC Convention 2026 – Streamlit Delegate Hub

A GitHub-backed Streamlit web app for EAC Convention delegates: programme, Athens and hotel guide, speakers, sponsors, and safety downloads.

## Run locally (optional)

1. Install Python 3.10+  
2. In a terminal, inside this folder:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud (no Git knowledge required)

### Step 1 — Create a GitHub repository
1. Create a GitHub account.
2. Click **+** (top-right) → **New repository**
3. Name it: `eac-convention-2026-streamlit`
4. Set visibility to **Public** (required for free Streamlit hosting)
5. Click **Create repository**

### Step 2 — Upload this project to GitHub (web upload)
1. Open your new repository.
2. Click **Add file → Upload files**
3. Drag-and-drop **everything** from this folder (including `app.py`, `pages/`, `data/`, `downloads/`, `requirements.txt`)
4. Click **Commit changes**

### Step 3 — Deploy with Streamlit
1. Go to **Streamlit Community Cloud**
2. Sign in with GitHub
3. Click **New app**
4. Select your repository `eac-convention-2026-streamlit`
5. Branch: `main`
6. Main file path: `app.py`
7. Click **Deploy**

Streamlit will build and publish your app URL.

## Update content (recommended approach)
Most updates do NOT require code changes. Edit these JSON files in GitHub:

- `data/schedule.json` (programme & locations)
- `data/speakers.json` (speakers / board)
- `data/sponsors.json` (sponsor packages)
- `data/links.json` (booking links)

After you commit changes, Streamlit redeploys automatically.

## Handling large files
If you want to avoid storing files in GitHub:
- host files on an official EAC location, then
- replace download buttons in `pages/6_Safety_and_Downloads.py` with links.

## Data quality warnings
Some legacy-looking elements exist in the information pack (e.g., non-Greek currency references). This app avoids repeating those; it uses the official booking portals instead.
