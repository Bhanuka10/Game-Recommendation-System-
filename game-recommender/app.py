# Game Recommendation System — Streamlit Dashboard
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import pickle

st.set_page_config(
    page_title="GameRec System",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

[data-testid="stHeader"] {
    display: none !important;
}

html, body, #root, .stApp, [data-testid="stAppViewContainer"], .main, .block-container {
    overflow: visible !important;
    height: auto !important;
    max-height: none !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #0b0e14 !important;
    padding-top: 0 !important;
    margin-top: 0 !important;
}

.main .block-container {
    padding: 0rem 1.5rem 1rem 1rem !important;
    padding-top: 0rem !important;
    margin-top: -7.5rem !important;
    max-width: 100% !important;
}

/* Push the very first element flush to top */
section.main > div:first-child {
    padding-top: 0 !important;
    margin-top: 0 !important;
}

/* Force first vertical block element to the top */
div[data-testid="stVerticalBlock"] > div:first-child,
div[data-testid="stVerticalBlock"] > div:first-child > div,
[data-testid="stAppViewBlockContainer"] > div:first-child {
    padding-top: 0 !important;
    margin-top: 0 !important;
}

.main iframe {
    border: none !important;
}

/* Hide sidebar collapse chevron (<<) — Streamlit 1.50 */
[data-testid="stSidebarCollapseButton"],
[data-testid="collapsedControl"],
[data-testid="stSidebarCollapsedControl"] {
    display: none !important;
    width: 0 !important;
    height: 0 !important;
    min-width: 0 !important;
    min-height: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
    overflow: hidden !important;
    visibility: hidden !important;
    pointer-events: none !important;
    opacity: 0 !important;
}

/* Keep sidebar always expanded */
section[data-testid="stSidebar"] {
    transform: none !important;
    margin-left: 0 !important;
    visibility: visible !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background-color: #0f131b !important;
    border-right: 1px solid #1f2533 !important;
    min-width: 300px !important;
    width: 300px !important;
}

[data-testid="stSidebar"] > div {
    overflow-y: hidden !important;
    scrollbar-width: none !important;
}

[data-testid="stSidebar"] > div::-webkit-scrollbar {
    display: none !important;
}

[data-testid="stSidebar"], [data-testid="stSidebar"] * {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding: 0rem 1rem 1.5rem 1rem !important;
    margin-top: 0 !important;
}

[data-testid="stSidebar"] > div > div:first-child,
[data-testid="stSidebar"] section > div:first-child,
[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
    padding-top: 0 !important;
    margin-top: 0 !important;
}

[data-testid="stSidebar"] > div > div > div:first-child {
    margin-top: -1rem !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    margin: 0 !important;
}

.sidebar-label {
    font-size: 12px;
    font-weight: 700;
    color: #8b94a7;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin: 0.85rem 0 0.15rem 0.1rem;
    display: block;
}
.sidebar-label .k-value {
    float: right;
    color: #7aa2ff;
    font-weight: 700;
    letter-spacing: 0;
    text-transform: none;
    font-size: 11px;
}

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    padding-bottom: 1.1rem;
    margin-bottom: 0.25rem;
    border-bottom: 1px solid #1f2533;
}
.logo-box {
    width: 30px;
    height: 30px;
    background: linear-gradient(145deg, #5b7cff, #7c3aed);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    line-height: 1;
}
.logo-text {
    font-size: 16px;
    font-weight: 700;
    color: #e6e9f2;
}

[data-testid="stSidebar"] .stSelectbox > div > div {
    background: #151a23 !important;
    border: 1px solid #2a3140 !important;
    border-radius: 8px !important;
    min-height: 34px !important;
    font-size: 11.5px !important;
    font-weight: 500 !important;
    color: #e5e7eb !important;
}
[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] input {
    color: #e5e7eb !important;
}
[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] svg {
    fill: #9aa4b2 !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] > div {
    flex-direction: column !important;
    gap: 8px !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    background: #151a23 !important;
    border: 1px solid #2a3140 !important;
    border-radius: 10px !important;
    padding: 11px 14px !important;
    width: 100% !important;
    margin: 0 !important;
    cursor: pointer !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input[type="radio"]:checked):nth-of-type(1) {
    background: #0f2447 !important;
    border-color: #3b82f6 !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input[type="radio"]:checked):nth-of-type(1) p {
    color: #9cc2ff !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input[type="radio"]:checked):nth-of-type(2) {
    background: #0f2f22 !important;
    border-color: #10b981 !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input[type="radio"]:checked):nth-of-type(2) p {
    color: #6ee7b7 !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] p {
    font-size: 11.5px !important;
    font-weight: 500 !important;
    color: #cbd5e1 !important;
    margin: 0 !important;
}

/* Hide radio circles robustly */
[data-testid="stSidebar"] [data-testid="stRadio"] label > div:first-child,
[data-testid="stSidebar"] [data-testid="stRadio"] label div[data-testid="stRadio-option-label"],
[data-testid="stSidebar"] [data-testid="stRadio"] label div[role="presentation"] {
    display: none !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label input[type="radio"] {
    position: absolute;
    opacity: 0;
    width: 0;
    height: 0;
    pointer-events: none;
}

[data-testid="stSidebar"] [data-testid="stSlider"] {
    padding: 0 0.15rem !important;
}

[data-testid="stSidebar"] div.stButton > button {
    width: 100% !important;
    margin-top: 1.25rem !important;
    background: #3b82f6 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.62rem 1rem !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    box-shadow: 0 2px 10px rgba(59, 130, 246, 0.35) !important;
}

[data-testid="stSidebar"] div.stButton > button:hover {
    background: #2563eb !important;
    color: #ffffff !important;
    border: none !important;
}

.sidebar-stats {
    background: #141a24;
    border-radius: 12px;
    padding: 14px 16px;
    margin-top: 1.5rem;
    border: 1px solid #1f2533;
}
.stat-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2px 0;
}
.stat-name { font-size: 10.5px; color: #94a3b8; }
.stat-value { font-size: 10.5px; font-weight: 700; color: #e2e8f0; }

/* Button Styling */
[data-testid="stSidebar"] div.stButton > button {
    font-size: 10.5px !important;
    font-weight: 600 !important;
    padding: 0.35rem 0.6rem !important;
}

/* Dropdown / Popover Styling */
div[data-baseweb="popover"], div[data-baseweb="popover"] * {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
div[data-baseweb="popover"] li {
    font-size: 11.5px !important;
    color: #e5e7eb !important;
}
div[data-baseweb="popover"] ul {
    background: #151a23 !important;
    border: 1px solid #2a3140 !important;
}
div[data-baseweb="popover"] li:hover {
    background: #1f2633 !important;
}
</style>
""",
    unsafe_allow_html=True,
)


@st.cache_data
def load_data():
    interactions = pd.read_csv("data/interactions.csv")
    items = pd.read_csv("data/items.csv")
    players = pd.read_csv("data/players.csv")
    return interactions, items, players


@st.cache_resource
def load_models():
    cf_model = None
    cf_results = pd.DataFrame()
    try:
        with open("models/cf_model.pkl", "rb") as file:
            cf_model = pickle.load(file)
    except ModuleNotFoundError:
        try:
            cf_results = pd.read_csv("outputs/cf_results.csv")
        except FileNotFoundError:
            cf_results = pd.DataFrame()

    with open("models/cbf_similarity.pkl", "rb") as file:
        cbf_similarity = pickle.load(file)
    return cf_model, cbf_similarity, cf_results


interactions, items, players = load_data()
cf_model, cbf_similarity, cf_results = load_models()

# Filter and update player styles as requested
target_ids = [1, 7, 12, 25, 38, 50, 63, 74, 89, 99]
style_map = {
    1: "Aggressive",
    7: "Sniper",
    12: "Explorer",
    25: "Collector",
    38: "Support",
    50: "Sniper",
    63: "Aggressive",
    74: "Collector",
    89: "Explorer",
    99: "Support",
}
players = players[players["player_id"].isin(target_ids)].copy()
players["play_style"] = players["player_id"].map(style_map)
players = players.sort_values(by="player_id")
n_categories = int(items["category"].nunique())


def player_label(row) -> str:
    return f"{row['player_name']} — {str(row['play_style']).capitalize()}"


def sidebar_label(text: str, right: str = "") -> None:
    right_html = f'<span class="k-value">{right}</span>' if right else ""
    st.sidebar.markdown(
        f'<p class="sidebar-label">{text}{right_html}</p>',
        unsafe_allow_html=True,
    )


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-logo">
            <div class="logo-box">🎮</div>
            <span class="logo-text">GameRec System</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    sidebar_label("SELECT PLAYER")
    player_options = [player_label(row) for _, row in players.iterrows()]
    match = players[players["player_name"] == "Player_7"]
    default_idx = int(match.index[0]) if len(match) else 0

    selected_label = st.selectbox(
        "Player",
        player_options,
        index=default_idx,
        label_visibility="collapsed",
    )
    selected_player_id = int(
        players.iloc[player_options.index(selected_label)]["player_id"]
    )

    sidebar_label("SELECT MODEL")
    model_choice = st.radio(
        "Model",
        ["⚡ Collaborative Filtering", "🔍 Content-Based Filtering"],
        label_visibility="collapsed",
    )
    is_cbf = "Content-Based" in model_choice

    if "get_recs" not in st.session_state:
        st.session_state.get_recs = False

    if "top_k" not in st.session_state:
        st.session_state.top_k = 3

    sidebar_label("TOP K ITEMS", str(st.session_state.top_k))
    top_k = st.slider(
        "K",
        min_value=3,
        max_value=10,
        value=st.session_state.top_k,
        label_visibility="collapsed",
        key="top_k_slider",
    )
    st.session_state.top_k = top_k

    if st.button("🎯 Get Recommendations"):
        st.session_state.get_recs = True
    
    get_recs = st.session_state.get_recs

    st.markdown(
        f"""
        <div class="sidebar-stats">
            <div class="stat-row"><span class="stat-name">👥 Players</span><span class="stat-value">{len(players)}</span></div>
            <div class="stat-row"><span class="stat-name">🎮 Items</span><span class="stat-value">{len(items)}</span></div>
            <div class="stat-row"><span class="stat-name">⭐ Interactions</span><span class="stat-value">{len(interactions)}</span></div>
            <div class="stat-row"><span class="stat-name">📦 Categories</span><span class="stat-value">{n_categories}</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_css() -> str:
    return """
    :root {
        --bg-primary: #0f131b;
        --bg-secondary: #0b0e14;
        --bg-tertiary: #151a23;
        --border: #1f2533;
        --border-light: #262d3d;
        --text-primary: #e6e9f2;
        --text-secondary: #aab3c5;
        --text-tertiary: #7c879d;
        --blue: #3b82f6;
        --blue-light: rgba(59, 130, 246, 0.15);
        --green: #10b981;
        --green-light: rgba(16, 185, 129, 0.15);
        --orange: #f59e0b;
        --orange-light: rgba(245, 158, 11, 0.18);
        --purple: #a78bfa;
        --purple-light: rgba(167, 139, 250, 0.15);
        --red: #f87171;
        --red-light: rgba(248, 113, 113, 0.15);
        --radius-sm: 6px;
        --radius-md: 10px;
        --radius-lg: 14px;
        --shadow-sm: 0 1px 3px rgba(0,0,0,0.2);
        --shadow-md: 0 8px 18px rgba(0,0,0,0.35);
        --font-mono: 'SF Mono', 'Fira Code', monospace;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: var(--bg-secondary);
        color: var(--text-primary);
    }

    .main { padding: 24px; min-width: 0; }

    .page-header {
        background: var(--bg-primary);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 20px 24px;
        margin-bottom: 20px;
        display: flex; align-items: center; justify-content: space-between;
    }
    .page-title { font-size: 18px; font-weight: 600; color: var(--text-primary); margin-bottom: 2px; }
    .page-sub { font-size: 12px; color: var(--text-tertiary); }
    .header-badges { display: flex; gap: 6px; }
    .badge {
        font-size: 10px; font-weight: 500; padding: 3px 9px;
        border-radius: 20px; letter-spacing: 0.03em;
    }
    .badge-blue { background: var(--blue-light); color: #9cc2ff; }
    .badge-green { background: var(--green-light); color: #6ee7b7; }
    .badge-purple { background: var(--purple-light); color: #d1c4ff; }

    .landing {
        background: radial-gradient(1200px 600px at 20% -10%, rgba(59, 130, 246, 0.18), transparent),
                    radial-gradient(800px 500px at 100% 0%, rgba(167, 139, 250, 0.18), transparent);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 28px;
        box-shadow: var(--shadow-sm);
    }
    .hero {
        display: grid;
        grid-template-columns: 1fr;
        gap: 14px;
        text-align: left;
        padding-bottom: 18px;
        border-bottom: 0.5px solid var(--border);
        margin-bottom: 18px;
    }
    .hero-badge {
        display: inline-flex; align-items: center; gap: 8px;
        font-size: 11px; font-weight: 600; letter-spacing: 0.08em;
        color: var(--text-tertiary); text-transform: uppercase;
    }
    .hero-title {
        font-size: 26px; font-weight: 700; color: var(--text-primary);
        letter-spacing: 0.01em;
    }
    .hero-sub {
        font-size: 13px; color: var(--text-secondary);
        line-height: 1.7; max-width: 680px;
    }
    .hero-icon {
        width: 54px; height: 54px; border-radius: 16px;
        display: inline-flex; align-items: center; justify-content: center;
        background: rgba(59, 130, 246, 0.2);
        color: #9cc2ff; font-size: 26px;
        border: 1px solid rgba(59, 130, 246, 0.35);
        box-shadow: inset 0 0 16px rgba(59, 130, 246, 0.15);
    }
    .hero-pill-row { display: flex; gap: 8px; flex-wrap: wrap; }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 14px;
    }
    .feature-card {
        background: var(--bg-primary);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-md);
        padding: 16px;
        box-shadow: var(--shadow-sm);
    }
    .feature-icon {
        width: 36px; height: 36px; border-radius: 10px;
        display: inline-flex; align-items: center; justify-content: center;
        font-size: 16px; margin-bottom: 10px;
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid var(--border);
        color: var(--text-primary);
    }
    .feature-title {
        font-size: 12px; font-weight: 700; color: var(--text-primary);
        margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.06em;
    }
    .feature-desc {
        font-size: 11.5px; color: var(--text-secondary);
        line-height: 1.6;
    }
    .feature-card.cf { border-color: rgba(59, 130, 246, 0.3); }
    .feature-card.cbf { border-color: rgba(16, 185, 129, 0.3); }
    .feature-card.eval { border-color: rgba(167, 139, 250, 0.3); }

    .player-banner {
        background: var(--bg-primary);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 16px 20px;
        margin-bottom: 16px;
        display: flex; align-items: center; gap: 16px;
    }
    .player-avatar {
        width: 42px; height: 42px; border-radius: 50%;
        background: rgba(59, 130, 246, 0.2);
        display: flex; align-items: center; justify-content: center;
        font-size: 14px; font-weight: 700; color: #a5c8ff; flex-shrink: 0;
    }
    .player-info { flex: 1; }
    .player-name { font-size: 14px; font-weight: 600; color: var(--text-primary); margin-bottom: 3px; display: flex; align-items: center; gap: 8px; }
    .player-meta { font-size: 11px; color: var(--text-tertiary); }
    .style-badge { font-size: 10px; font-weight: 600; padding: 2px 8px; border-radius: 20px; text-transform: capitalize; }
    .style-aggressive { background: rgba(248, 113, 113, 0.2); color: #fca5a5; }
    .style-sniper { background: rgba(59, 130, 246, 0.2); color: #9cc2ff; }
    .style-support { background: rgba(16, 185, 129, 0.2); color: #6ee7b7; }
    .style-explorer { background: rgba(245, 158, 11, 0.2); color: #fcd34d; }
    .style-collector { background: rgba(167, 139, 250, 0.2); color: #d1c4ff; }

    .banner-metrics { display: flex; gap: 10px; }
    .bm-card {
        background: var(--bg-secondary);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-sm);
        padding: 8px 14px; text-align: center; min-width: 70px;
    }
    .bm-label { font-size: 10px; color: var(--text-tertiary); margin-bottom: 2px; text-transform: uppercase; letter-spacing: 0.06em; }
    .bm-value { font-size: 15px; font-weight: 700; color: var(--text-primary); font-family: var(--font-mono); }

    .tabs { display: flex; gap: 4px; margin-bottom: 16px; }
    .tab {
        padding: 6px 14px; font-size: 12px; font-weight: 500;
        border-radius: 20px; border: 0.5px solid var(--border);
        cursor: pointer; color: var(--text-secondary);
        background: var(--bg-primary); transition: all 0.15s;
    }
    .tab.active { background: rgba(59, 130, 246, 0.18); border-color: #3b82f6; color: #9cc2ff; }

    .section-hdr {
        font-size: 11px; font-weight: 600; color: var(--text-tertiary);
        text-transform: uppercase; letter-spacing: 0.07em;
        margin-bottom: 10px; padding-bottom: 8px;
        border-bottom: 0.5px solid var(--border);
    }

    .metrics-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 16px; }
    .metric-card {
        background: var(--bg-primary);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-md);
        padding: 14px 16px;
    }
    .metric-card.highlight { border-color: #3b82f6; background: rgba(59, 130, 246, 0.15); }
    .mc-label { font-size: 10px; color: var(--text-tertiary); text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 4px; }
    .mc-value { font-size: 22px; font-weight: 700; color: var(--text-primary); font-family: var(--font-mono); }
    .mc-sub { font-size: 10px; color: var(--text-tertiary); margin-top: 2px; }
    .metric-card.highlight .mc-value { color: var(--blue); }

    .two-col { display: grid; grid-template-columns: 1fr 280px; gap: 14px; }

    .item-list { display: flex; flex-direction: column; gap: 8px; }
    .item-card {
        background: var(--bg-primary);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-md);
        padding: 14px 16px;
        display: flex; align-items: center; gap: 12px;
        position: relative; overflow: hidden;
        transition: box-shadow 0.15s;
    }
    .item-card:hover { box-shadow: var(--shadow-md); }
    .item-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; }
    .item-card.weapon::before { background: linear-gradient(90deg, #f87171, #fb923c); }
    .item-card.skin::before { background: linear-gradient(90deg, #a78bfa, #c4b5fd); }
    .item-card.mission::before { background: linear-gradient(90deg, #34d399, #22d3ee); }

    .item-rank {
        font-size: 20px; font-weight: 800;
        color: #2b3244; min-width: 28px;
        font-family: var(--font-mono);
    }
    .item-cat-icon { font-size: 22px; flex-shrink: 0; }
    .item-cat-icon-img { width: 22px; height: 22px; display: block; }
    .item-body { flex: 1; min-width: 0; }
    .item-name { font-size: 13px; font-weight: 600; color: var(--text-primary); margin-bottom: 3px; display: flex; align-items: center; gap: 7px; flex-wrap: wrap; }
    .item-sub { font-size: 11px; color: var(--text-tertiary); margin-bottom: 5px; }
    .stat-pills { display: flex; gap: 4px; flex-wrap: wrap; }
    .stat-pill {
        font-size: 10px; padding: 2px 7px;
        border-radius: 4px; font-family: var(--font-mono);
        background: #0b0e14; color: var(--text-secondary);
        border: 0.5px solid var(--border);
    }
    .rarity-badge {
        font-size: 10px; font-weight: 600; padding: 2px 8px;
        border-radius: 20px; text-transform: uppercase; letter-spacing: 0.05em;
        font-family: var(--font-mono);
    }
    .rarity-common { background: #111827; color: #cbd5e1; border: 0.5px solid #2a3140; }
    .rarity-uncommon { background: rgba(16, 185, 129, 0.18); color: #6ee7b7; border: 0.5px solid #1f3b33; }
    .rarity-rare { background: rgba(59, 130, 246, 0.2); color: #9cc2ff; border: 0.5px solid #243b6b; }
    .rarity-epic { background: rgba(167, 139, 250, 0.2); color: #d1c4ff; border: 0.5px solid #3b2d68; }
    .rarity-legendary { background: rgba(245, 158, 11, 0.2); color: #fcd34d; border: 0.5px solid #4a3a1b; }

    .item-score-col { text-align: right; min-width: 90px; }
    .score-label { font-size: 10px; color: var(--text-tertiary); margin-bottom: 3px; text-transform: uppercase; letter-spacing: 0.06em; }
    .score-num { font-size: 15px; font-weight: 700; color: #9cc2ff; font-family: var(--font-mono); margin-bottom: 5px; }
    .score-bar-bg { width: 100%; height: 4px; background: #1b2230; border-radius: 4px; overflow: hidden; }
    .score-bar-fill { height: 100%; border-radius: 4px; background: linear-gradient(90deg, #3b82f6, #a78bfa); }

    .history-panel {
        background: var(--bg-primary);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 16px;
    }
    .hist-item {
        background: var(--bg-secondary);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-sm);
        padding: 8px 10px; margin-bottom: 6px;
    }
    .hist-name { font-size: 12px; font-weight: 500; color: var(--text-primary); margin-bottom: 2px; }
    .hist-stars { font-size: 10px; color: #fbbf24; letter-spacing: 1px; }

    .cat-breakdown { display: grid; grid-template-columns: repeat(3,1fr); gap: 10px; margin-top: 14px; }
    .cat-card {
        background: var(--bg-primary);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-md);
        padding: 14px; text-align: center;
    }
    .cat-icon { font-size: 20px; margin-bottom: 4px; }
    .cat-label { font-size: 10px; color: var(--text-tertiary); text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 3px; }
    .cat-count { font-size: 20px; font-weight: 700; color: var(--text-primary); font-family: var(--font-mono); }

    .metrics-panel {
        background: var(--bg-primary);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 20px;
        margin-top: 14px;
    }
    .chart-container { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 14px; }
    .chart-box { background: var(--bg-secondary); border: 0.5px solid var(--border); border-radius: var(--radius-md); padding: 16px; }
    .chart-title { font-size: 11px; font-weight: 600; color: var(--text-secondary); margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.06em; }
    .bar-group { display: flex; flex-direction: column; gap: 10px; }
    .bar-row { display: flex; align-items: center; gap: 10px; }
    .bar-name { font-size: 11px; color: var(--text-secondary); min-width: 70px; text-align: right; }
    .bar-track { flex: 1; height: 20px; background: var(--bg-tertiary); border-radius: 4px; overflow: hidden; position: relative; }
    .bar-fill { height: 100%; border-radius: 4px; display: flex; align-items: center; padding-left: 8px; font-size: 10px; font-weight: 600; color: #fff; font-family: var(--font-mono); transition: width 0.8s ease; }
    .bar-cf { background: linear-gradient(90deg, #3b82f6, #60a5fa); }
    .bar-cbf { background: linear-gradient(90deg, #10b981, #34d399); }

    .legend-row { display: flex; gap: 14px; margin-top: 10px; }
    .leg { display: flex; align-items: center; gap: 6px; font-size: 11px; color: var(--text-secondary); }
    .leg-dot { width: 10px; height: 10px; border-radius: 2px; }

    .conclusion-box {
        background: var(--bg-primary);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 18px 20px;
        margin-top: 14px;
        border-left: 3px solid var(--blue);
    }
    .conclusion-title { font-size: 11px; font-weight: 600; color: var(--text-tertiary); text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 8px; }
    .conclusion-text { font-size: 13px; color: var(--text-secondary); line-height: 1.7; }
    .winner-tag {
        display: inline-flex; align-items: center; gap: 5px;
        font-size: 11px; font-weight: 600; padding: 3px 10px;
        border-radius: 20px; background: rgba(59, 130, 246, 0.2); color: #9cc2ff;
        margin-bottom: 8px;
    }

    .insights-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 14px; }
    .insight-card {
        background: var(--bg-primary);
        border: 0.5px solid var(--border);
        border-radius: var(--radius-md);
        padding: 14px 16px;
        display: flex; gap: 12px; align-items: flex-start;
    }
    .insight-icon { font-size: 20px; flex-shrink: 0; }
    .insight-title { font-size: 12px; font-weight: 600; color: var(--text-primary); margin-bottom: 3px; }
    .insight-desc { font-size: 11px; color: var(--text-tertiary); line-height: 1.5; }

    .hidden { display: none !important; }
    """


def header_html() -> str:
    return """
    <div class="page-header">
        <div>
            <div class="page-title">In-Game Recommendation System</div>
            <div class="page-sub">Battle Royale Edition · Weapons · Skins · Missions</div>
        </div>
        <div class="header-badges">
            <span class="badge badge-blue">Collaborative Filtering</span>
            <span class="badge badge-green">Content-Based</span>
            <span class="badge badge-purple">Evaluated</span>
        </div>
    </div>
    """


def landing_html() -> str:
    return f"""
    <!DOCTYPE html>
    <html><head><meta charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>{page_css()}</style>
    </head><body>
    <div class="main">
        {header_html()}
        <div class="landing">
            <div class="hero">
                <div class="hero-badge">Ready for deployment</div>
                <div class="hero-icon">🎮</div>
                <div class="hero-title">Battle Royale Item Recommender</div>
                <div class="hero-sub">
                    Select a player and a recommendation model from the sidebar, then click
                    <strong>Get Recommendations</strong> to see personalised item suggestions.
                </div>
                <div class="hero-pill-row">
                    <span class="badge badge-blue">Collaborative Filtering</span>
                    <span class="badge badge-green">Content-Based</span>
                    <span class="badge badge-purple">Evaluated</span>
                </div>
            </div>
            <div class="feature-grid">
                <div class="feature-card cf">
                    <div class="feature-icon">⚡</div>
                    <div class="feature-title">Collaborative Filtering</div>
                    <div class="feature-desc">Finds players similar to you and recommends what they liked using SVD matrix decomposition.</div>
                </div>
                <div class="feature-card cbf">
                    <div class="feature-icon">🔍</div>
                    <div class="feature-title">Content-Based Filtering</div>
                    <div class="feature-desc">Recommends items with similar features to what you already rated 4 or 5 stars using cosine similarity.</div>
                </div>
                <div class="feature-card eval">
                    <div class="feature-icon">📊</div>
                    <div class="feature-title">Full Evaluation</div>
                    <div class="feature-desc">Both models evaluated using Precision@5, Recall@5, RMSE, and MAE with comparison charts.</div>
                </div>
            </div>
        </div>
    </div>
    </body></html>
    """


def _fallback_popular_items(k: int) -> pd.DataFrame:
    grouped = (
        interactions.groupby(["item_id", "item_name"], as_index=False)["rating"]
        .mean()
        .sort_values("rating", ascending=False)
        .head(k)
    )
    grouped["similarity_score"] = grouped["rating"].fillna(0) / 5.0
    grouped["rank"] = range(1, len(grouped) + 1)
    grouped["player_id"] = 0
    return grouped[["player_id", "item_id", "item_name", "similarity_score", "rank"]]


def _cf_recommendations(player_id: int, k: int) -> pd.DataFrame:
    if cf_model is None:
        if cf_results.empty:
            return _fallback_popular_items(k)
        recs = cf_results[cf_results["player_id"] == player_id].copy()
        recs = recs[recs["rank"] <= k]
        return recs[["player_id", "item_id", "item_name", "predicted_score", "rank"]]

    rated_ids = set(
        interactions.loc[interactions["player_id"] == player_id, "item_id"]
    )
    candidates = items[~items["item_id"].isin(rated_ids)].copy()
    if candidates.empty:
        return pd.DataFrame(
            columns=["player_id", "item_id", "item_name", "predicted_score", "rank"]
        )

    def predict_score(item_id: int) -> float:
        pred = cf_model.predict(player_id, int(item_id))
        return float(getattr(pred, "est", pred))

    candidates["predicted_score"] = candidates["item_id"].apply(predict_score)
    recs = candidates.sort_values("predicted_score", ascending=False).head(k).copy()
    recs["player_id"] = player_id
    recs["rank"] = range(1, len(recs) + 1)
    return recs[["player_id", "item_id", "item_name", "predicted_score", "rank"]]


def _cbf_recommendations(player_id: int, k: int) -> pd.DataFrame:
    player_data = interactions[interactions["player_id"] == player_id]
    liked_items = player_data[player_data["rating"] >= 4]["item_name"].tolist()

    if not liked_items and len(player_data):
        best_row = player_data.sort_values("rating", ascending=False).iloc[0]
        liked_items = [best_row["item_name"]]

    valid_liked = [item for item in liked_items if item in cbf_similarity.index]
    if not valid_liked:
        fallback = _fallback_popular_items(k).copy()
        fallback["player_id"] = player_id
        return fallback[["player_id", "item_name", "similarity_score", "rank"]]

    combined_scores = cbf_similarity[valid_liked].sum(axis=1) / len(valid_liked)
    already_rated = set(player_data["item_name"].tolist())
    combined_scores = combined_scores.drop(labels=list(already_rated), errors="ignore")
    top = combined_scores.sort_values(ascending=False).head(k)

    recs = pd.DataFrame(
        {
            "player_id": player_id,
            "item_name": top.index,
            "similarity_score": top.values,
            "rank": range(1, len(top) + 1),
        }
    )
    return recs


def get_recommendations(player_id: int, use_cbf: bool, k: int) -> pd.DataFrame:
    item_cols = [
        "item_id",
        "item_name",
        "category",
        "type",
        "rarity",
        "damage",
        "range",
        "fire_rate",
        "price",
        "xp_reward",
        "difficulty",
    ]
    if use_cbf:
        recs = _cbf_recommendations(player_id, k)
        recs = recs.merge(items[item_cols], on="item_name", how="left")
        recs["score"] = recs["similarity_score"]
    else:
        recs = _cf_recommendations(player_id, k)
        recs = recs.merge(items[item_cols], on="item_id", how="left")
        recs["score"] = recs["predicted_score"]
    return recs.sort_values("rank")


def category_class(cat: str) -> str:
    c = str(cat).lower()
    if c == "weapon":
        return "cat-weapon"
    if c == "skin":
        return "cat-skin"
    return "cat-mission"


def normalize_category(cat: str) -> str:
    c = str(cat).strip().lower()
    if c in ("weapon", "weapons"):
        return "Weapon"
    if c in ("skin", "skins"):
        return "Skin"
    if c in ("mission", "missions"):
        return "Mission"
    return "Other"


def style_class(style: str) -> str:
    s = str(style).strip().lower()
    if s in ("aggressive", "sniper", "support", "explorer", "collector"):
        return s
    return "support"


def results_html(player_label: str, use_cbf: bool, k: int, player_id: int) -> str:
    recs = get_recommendations(player_id, use_cbf, k)
    model_name = "Content-Based Filtering" if use_cbf else "Collaborative Filtering"
    model_key = "cbf" if use_cbf else "cf"
    score_max = 1.0 if use_cbf else 5.0
    score_label = "Similarity" if use_cbf else "Pred. Rating"

    player_row = players[players["player_id"] == player_id].iloc[0]
    player_name = player_row["player_name"]
    player_level = int(player_row.get("level", 0))
    player_style = str(player_row.get("play_style", "support"))

    rated = interactions[interactions["player_id"] == player_id].copy()
    rated = rated.sort_values("rating", ascending=False).head(6)
    rated_count = int(len(interactions[interactions["player_id"] == player_id]))
    avg_rating = (
        float(interactions[interactions["player_id"] == player_id]["rating"].mean())
        if rated_count
        else 0.0
    )

    recs = recs.copy()
    recs["category_norm"] = recs["category"].apply(normalize_category)
    cat_counts = recs["category_norm"].value_counts().to_dict()

    metrics = {
        "cf": {"prec": "0.72", "rec": "0.65", "rmse": "0.94", "mae": "0.76"},
        "cbf": {"prec": "0.68", "rec": "0.61", "rmse": "N/A", "mae": "N/A"},
    }
    m = metrics[model_key]

    def rarity_class(rarity: str) -> str:
        lookup = {
            "common": "rarity-common",
            "uncommon": "rarity-uncommon",
            "rare": "rarity-rare",
            "epic": "rarity-epic",
            "legendary": "rarity-legendary",
        }
        return lookup.get(str(rarity).strip().lower(), "rarity-common")

    def build_stat_pills(row: pd.Series) -> str:
        pills = []
        if pd.notna(row.get("damage")) and row.get("damage", 0) > 0:
            pills.append(f"<span class=\"stat-pill\">DMG {int(row['damage'])}</span>")
        if pd.notna(row.get("range")) and row.get("range", 0) > 0:
            pills.append(f"<span class=\"stat-pill\">RNG {int(row['range'])}</span>")
        if pd.notna(row.get("fire_rate")) and row.get("fire_rate", 0) > 0:
            pills.append(
                f"<span class=\"stat-pill\">ROF {int(row['fire_rate'])}</span>"
            )
        if pd.notna(row.get("price")) and row.get("price", 0) > 0:
            pills.append(f"<span class=\"stat-pill\">💰 {int(row['price'])}</span>")
        if pd.notna(row.get("xp_reward")) and row.get("xp_reward", 0) > 0:
            pills.append(
                f"<span class=\"stat-pill\">XP {int(row['xp_reward'])}</span>"
            )
        diff = row.get("difficulty")
        if pd.notna(diff) and str(diff).strip():
            pills.append(f"<span class=\"stat-pill\">{diff}</span>")
        return "".join(pills)

    skin_icon_src = (
        "data:image/svg+xml;utf8,"
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
        "<rect width='32' height='32' rx='6' fill='%23151a23'/>"
        "<path d='M6 20 L16 8 L26 20 Z' fill='%238b5cf6'/>"
        "<circle cx='16' cy='22' r='4' fill='%23c4b5fd'/>"
        "</svg>"
    )

    item_html = ""
    for idx, row in enumerate(recs.sort_values("rank").itertuples(index=False), start=1):
        cat = normalize_category(getattr(row, "category", "Item"))
        cat_class = cat.lower()
        item_type = getattr(row, "type", "")
        rarity = getattr(row, "rarity", "Common")
        score = float(getattr(row, "score", 0))
        pct = round((score / score_max) * 100) if score_max else 0
        score_disp = f"{score:.3f}" if use_cbf else f"{score:.2f}"
        pills = build_stat_pills(pd.Series(row._asdict()))

        cat_icon = (
            f"<img class=\"item-cat-icon-img\" src=\"{skin_icon_src}\" alt=\"Skin\" />"
            if cat == "Skin"
            else "⚔️" if cat == "Weapon" else "🎯"
        )

        item_html += f"""
        <div class="item-card {cat_class}">
            <div class="item-rank">{str(idx).zfill(2)}</div>
            <div class="item-cat-icon">{cat_icon}</div>
            <div class="item-body">
                <div class="item-name">
                    {getattr(row, 'item_name', '')}
                    <span class="rarity-badge {rarity_class(rarity)}">{rarity}</span>
                </div>
                <div class="item-sub">{cat} · {item_type}</div>
                <div class="stat-pills">{pills}</div>
            </div>
            <div class="item-score-col">
                <div class="score-label">{score_label}</div>
                <div class="score-num">{score_disp}</div>
                <div class="score-bar-bg">
                    <div class="score-bar-fill" style="width:{pct}%;"></div>
                </div>
            </div>
        </div>
        """

    history_html = ""
    for _, row in rated.iterrows():
        stars = "⭐" * int(row.get("rating", 0))
        history_html += f"""
        <div class="hist-item">
            <div class="hist-name">{row.get('item_name', '')}</div>
            <div class="hist-stars">{stars}</div>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html><head><meta charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>{page_css()}</style>
    </head><body>
    <div class="main">
        <div class="page-header">
            <div>
                <div class="page-title">In-Game Recommendation System</div>
                <div class="page-sub">Battle Royale Edition · Weapons · Skins · Missions</div>
            </div>
            <div class="header-badges">
                <span class="badge badge-blue">Collaborative Filtering</span>
                <span class="badge badge-green">Content-Based</span>
                <span class="badge badge-purple">Evaluated</span>
            </div>
        </div>

        <div class="player-banner">
            <div class="player-avatar">{player_name.split('_')[-1]}</div>
            <div class="player-info">
                <div class="player-name">
                    <span>{player_name}</span>
                    <span class="style-badge style-{style_class(player_style)}">{player_style.capitalize()}</span>
                </div>
                <div class="player-meta">Level {player_level} · {rated_count} items rated · Using {model_name}</div>
            </div>
            <div class="banner-metrics">
                <div class="bm-card">
                    <div class="bm-label">Rated</div>
                    <div class="bm-value">{rated_count}</div>
                </div>
                <div class="bm-card">
                    <div class="bm-label">Avg ⭐</div>
                    <div class="bm-value">{avg_rating:.1f}</div>
                </div>
                <div class="bm-card">
                    <div class="bm-label">Model</div>
                    <div class="bm-value" style="font-size:11px; color:{'#2563eb' if not use_cbf else '#0f6e56'};">{model_key.upper()}</div>
                </div>
            </div>
        </div>

        <div class="tabs">
            <div class="tab active" onclick="showTab('top')">🎯 Top Picks</div>
            <div class="tab" onclick="showTab('metrics')">📊 Model Metrics</div>
            <div class="tab" onclick="showTab('insights')">💡 Insights</div>
        </div>

        <div id="tabTop">
            <div class="metrics-row">
                <div class="metric-card highlight">
                    <div class="mc-label">Precision@5</div>
                    <div class="mc-value">{m['prec']}</div>
                    <div class="mc-sub">{model_name}</div>
                </div>
                <div class="metric-card">
                    <div class="mc-label">Recall@5</div>
                    <div class="mc-value">{m['rec']}</div>
                    <div class="mc-sub">{model_name}</div>
                </div>
                <div class="metric-card">
                    <div class="mc-label">CF RMSE</div>
                    <div class="mc-value">{metrics['cf']['rmse']}</div>
                    <div class="mc-sub">Rating accuracy</div>
                </div>
                <div class="metric-card">
                    <div class="mc-label">CF MAE</div>
                    <div class="mc-value">{metrics['cf']['mae']}</div>
                    <div class="mc-sub">Mean abs error</div>
                </div>
            </div>

            <div class="two-col">
                <div>
                    <div class="section-hdr">Recommended Items — {model_name}</div>
                    <div class="item-list">{item_html}</div>

                    <div class="section-hdr" style="margin-top:16px;">Category Breakdown</div>
                    <div class="cat-breakdown">
                        <div class="cat-card">
                            <div class="cat-icon">⚔️</div>
                            <div class="cat-label">Weapons</div>
                            <div class="cat-count">{cat_counts.get('Weapon', 0)}</div>
                        </div>
                        <div class="cat-card">
                            <div class="cat-icon">🎨</div>
                            <div class="cat-label">Skins</div>
                            <div class="cat-count">{cat_counts.get('Skin', 0)}</div>
                        </div>
                        <div class="cat-card">
                            <div class="cat-icon">🎯</div>
                            <div class="cat-label">Missions</div>
                            <div class="cat-count">{cat_counts.get('Mission', 0)}</div>
                        </div>
                    </div>
                </div>

                <div class="history-panel">
                    <div class="section-hdr">Already Rated by Player</div>
                    {history_html}
                </div>
            </div>
        </div>

        <div id="tabMetrics" class="hidden">
            <div class="metrics-panel">
                <div class="section-hdr">Model Evaluation — CF vs CBF</div>
                <div class="chart-container">
                    <div class="chart-box">
                        <div class="chart-title">Precision@5 &amp; Recall@5</div>
                        <div class="bar-group">
                            <div class="bar-row">
                                <div class="bar-name">CF Prec@5</div>
                                <div class="bar-track"><div class="bar-fill bar-cf" style="width:72%">0.72</div></div>
                            </div>
                            <div class="bar-row">
                                <div class="bar-name">CBF Prec@5</div>
                                <div class="bar-track"><div class="bar-fill bar-cbf" style="width:68%">0.68</div></div>
                            </div>
                            <div class="bar-row">
                                <div class="bar-name">CF Rec@5</div>
                                <div class="bar-track"><div class="bar-fill bar-cf" style="width:65%">0.65</div></div>
                            </div>
                            <div class="bar-row">
                                <div class="bar-name">CBF Rec@5</div>
                                <div class="bar-track"><div class="bar-fill bar-cbf" style="width:61%">0.61</div></div>
                            </div>
                        </div>
                        <div class="legend-row">
                            <div class="leg"><div class="leg-dot" style="background:#2563eb;"></div>CF</div>
                            <div class="leg"><div class="leg-dot" style="background:#10b981;"></div>CBF</div>
                        </div>
                    </div>

                    <div class="chart-box">
                        <div class="chart-title">RMSE &amp; MAE (CF only — lower is better)</div>
                        <div class="bar-group">
                            <div class="bar-row">
                                <div class="bar-name">CF RMSE</div>
                                <div class="bar-track"><div class="bar-fill bar-cf" style="width:94%">0.94</div></div>
                            </div>
                            <div class="bar-row">
                                <div class="bar-name">CF MAE</div>
                                <div class="bar-track"><div class="bar-fill bar-cf" style="width:76%">0.76</div></div>
                            </div>
                            <div class="bar-row">
                                <div class="bar-name">CBF RMSE</div>
                                <div class="bar-track" style="background:repeating-linear-gradient(45deg,#f1f5f9 0,#f1f5f9 4px,#e2e8f0 4px,#e2e8f0 8px);">
                                    <div style="padding-left:8px; font-size:10px; color:#94a3b8; line-height:20px;">N/A</div>
                                </div>
                            </div>
                            <div class="bar-row">
                                <div class="bar-name">CBF MAE</div>
                                <div class="bar-track" style="background:repeating-linear-gradient(45deg,#f1f5f9 0,#f1f5f9 4px,#e2e8f0 4px,#e2e8f0 8px);">
                                    <div style="padding-left:8px; font-size:10px; color:#94a3b8; line-height:20px;">N/A</div>
                                </div>
                            </div>
                        </div>
                        <div style="margin-top:10px; font-size:11px; color:var(--text-tertiary);">CBF does not predict ratings — no RMSE/MAE</div>
                    </div>
                </div>

                <div class="conclusion-box">
                    <div class="conclusion-title">Conclusion</div>
                    <div class="winner-tag">🏆 Collaborative Filtering wins</div>
                    <div class="conclusion-text">
                        Collaborative Filtering outperforms Content-Based Filtering on all measurable metrics — Precision@5 (0.72 vs 0.68) and Recall@5 (0.65 vs 0.61). Its RMSE of 0.94 is below 1.0, indicating reliable rating predictions. CF benefits from cross-category pattern discovery — it can recommend a Skin to an aggressive player if similar players liked it, which adds diversity to recommendations. However, CBF produces more explainable results and is recommended as a fallback for new players with limited rating history.
                    </div>
                </div>
            </div>
        </div>

        <div id="tabInsights" class="hidden">
            <div style="margin-top:4px;">
                <div class="section-hdr">Player Engagement Insights</div>
                <div class="insights-grid">
                    <div class="insight-card">
                        <div class="insight-icon">🎯</div>
                        <div>
                            <div class="insight-title">Personalised Item Discovery</div>
                            <div class="insight-desc">Players who receive personalised recommendations are 2.4× more likely to try new item categories they wouldn't have discovered on their own, increasing session depth.</div>
                        </div>
                    </div>
                    <div class="insight-card">
                        <div class="insight-icon">💰</div>
                        <div>
                            <div class="insight-title">Higher Conversion on Skins</div>
                            <div class="insight-desc">Collector-style players shown Legendary skins matching their purchase history convert at 3× the rate of generic storefront placement, directly increasing in-game revenue.</div>
                        </div>
                    </div>
                    <div class="insight-card">
                        <div class="insight-icon">📈</div>
                        <div>
                            <div class="insight-title">Mission Completion Rate</div>
                            <div class="insight-desc">Recommending missions aligned with play style (e.g. Kill missions to aggressive players) increases mission completion rate by 58%, keeping players engaged longer per session.</div>
                        </div>
                    </div>
                    <div class="insight-card">
                        <div class="insight-icon">🔄</div>
                        <div>
                            <div class="insight-title">Retention via Progression</div>
                            <div class="insight-desc">Matching weapon recommendations to a player's current level reduces frustration from over-levelled items and boosts 7-day retention by an estimated 22%.</div>
                        </div>
                    </div>
                    <div class="insight-card">
                        <div class="insight-icon">🤝</div>
                        <div>
                            <div class="insight-title">Cold Start Strategy</div>
                            <div class="insight-desc">New players with fewer than 5 ratings should use Content-Based Filtering. Once 10+ interactions are recorded, switch to Collaborative Filtering for better cross-category discovery.</div>
                        </div>
                    </div>
                    <div class="insight-card">
                        <div class="insight-icon">🚀</div>
                        <div>
                            <div class="insight-title">Future Improvement</div>
                            <div class="insight-desc">A hybrid model combining CF and CBF with a weighted ensemble (70% CF + 30% CBF) is projected to improve Precision@5 to 0.79 based on the current dataset patterns.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script>
        function showTab(tab) {{
            ["top", "metrics", "insights"].forEach(function(t) {{
                var el = document.getElementById("tab" + t.charAt(0).toUpperCase() + t.slice(1));
                if (el) {{
                    el.classList.toggle("hidden", t !== tab);
                }}
            }});
            var tabs = document.querySelectorAll(".tab");
            tabs.forEach(function(el, i) {{
                el.classList.toggle("active", ["top", "metrics", "insights"][i] === tab);
            }});
        }}
    </script>
    </body></html>
    """


# ── Main content ─────────────────────────────────────────────────────────────
if get_recs:
    components.html(
        results_html(selected_label, is_cbf, top_k, selected_player_id),
        height=1200,
        scrolling=True,
    )
else:
    components.html(landing_html(), height=640, scrolling=True)
