# Game Recommendation System — Streamlit Dashboard
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

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
    overflow: hidden !important;
    height: 100vh !important;
    max-height: 100vh !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #f0f2f6 !important;
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
    background-color: #ffffff !important;
    border-right: 1px solid #e8eaef !important;
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
    color: #9ca3af;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin: 0.85rem 0 0.15rem 0.1rem;
    display: block;
}
.sidebar-label .k-value {
    float: right;
    color: #2e75d1;
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
    border-bottom: 1px solid #f0f0f2;
}
.logo-box {
    width: 30px;
    height: 30px;
    background: linear-gradient(145deg, #8b7cf8, #5b52e8);
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
    color: #1a1a1a;
}

[data-testid="stSidebar"] .stSelectbox > div > div {
    background: #f8f9fb !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 8px !important;
    min-height: 34px !important;
    font-size: 11.5px !important;
    font-weight: 500 !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] > div {
    flex-direction: column !important;
    gap: 8px !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    background: #ffffff !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 10px !important;
    padding: 11px 14px !important;
    width: 100% !important;
    margin: 0 !important;
    cursor: pointer !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input[type="radio"]:checked):nth-of-type(1) {
    background: #e8f1fc !important;
    border-color: #2e75d1 !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input[type="radio"]:checked):nth-of-type(1) p {
    color: #1d5fbf !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input[type="radio"]:checked):nth-of-type(2) {
    background: #e6f9f0 !important;
    border-color: #059669 !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input[type="radio"]:checked):nth-of-type(2) p {
    color: #059669 !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] p {
    font-size: 11.5px !important;
    font-weight: 500 !important;
    color: #374151 !important;
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
    background: #2e75d1 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.62rem 1rem !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    box-shadow: 0 2px 8px rgba(46, 117, 209, 0.35) !important;
}

[data-testid="stSidebar"] div.stButton > button:hover {
    background: #2568bd !important;
    color: #ffffff !important;
    border: none !important;
}

.sidebar-stats {
    background: #f4f6f9;
    border-radius: 12px;
    padding: 14px 16px;
    margin-top: 1.5rem;
    border: 1px solid #eef0f4;
}
.stat-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2px 0;
}
.stat-name { font-size: 10.5px; color: #6b7280; }
.stat-value { font-size: 10.5px; font-weight: 700; color: #1a1a1a; }

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
    cf_results = pd.read_csv("outputs/cf_results.csv")
    cbf_results = pd.read_csv("outputs/cbf_results.csv")
    return interactions, items, players, cf_results, cbf_results


interactions, items, players, cf_results, cbf_results = load_data()

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
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background: #f0f2f6;
        color: #111827;
    }
    .wrap { width: 100%; }
    .main-header-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 12px 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        border: 1px solid #eef0f4;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
    }
    .header-title {
        font-size: 17px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 4px;
    }
    .header-subtitle { font-size: 12px; color: #9ca3af; }
    .header-badges { display: flex; gap: 8px; flex-shrink: 0; }
    .badge {
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        white-space: nowrap;
    }
    .badge-blue   { background: #e8f1fc; color: #2e75d1; }
    .badge-green  { background: #e6f9f0; color: #059669; }
    .badge-purple { background: #f3f0ff; color: #7c3aed; }
    .landing {
        min-height: auto;
        display: flex;
        flex-direction: column;
        padding-top: 0px;
    }
    .hero {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        text-align: center;
        padding: 5px 24px 20px;
    }
    .icon-box {
        width: 64px;
        height: 64px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 32px;
        margin-bottom: 20px;
    }
    .welcome-title {
        font-size: 22px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 12px;
    }
    .welcome-text {
        font-size: 14px;
        color: #6b7280;
        max-width: 500px;
        line-height: 1.65;
    }
    .welcome-text strong { color: #4b5563; font-weight: 600; }
    .feature-cards {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
        width: 100%;
        margin-top: 56px;
    }
    .f-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 22px 18px;
        border: 1px solid #eef0f4;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05);
        text-align: center;
    }
    .f-icon { font-size: 22px; margin-bottom: 12px; display: block; }
    .f-title { font-size: 13px; font-weight: 700; color: #111827; margin-bottom: 8px; }
    .f-desc { font-size: 11.5px; color: #9ca3af; line-height: 1.55; }
    .results-wrap { padding-top: 20px; }
    .results-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 16px;
    }
    .results-title { font-size: 18px; font-weight: 700; }
    .results-subtitle { font-size: 13px; color: #6b7280; margin-top: 3px; }
    .model-pill {
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }
    .pill-cf  { background: #e8f1fc; color: #2e75d1; }
    .pill-cbf { background: #e6f9f0; color: #059669; }
    .rec-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
    }
    .rec-card {
        background: #fff;
        border-radius: 12px;
        padding: 14px;
        border: 1px solid #eef0f4;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05);
        display: flex;
        gap: 12px;
        align-items: flex-start;
    }
    .rec-rank {
        width: 28px; height: 28px;
        background: #2e75d1; color: #fff;
        border-radius: 8px;
        display: flex; align-items: center; justify-content: center;
        font-size: 12px; font-weight: 700; flex-shrink: 0;
    }
    .rec-body { flex: 1; }
    .rec-name { font-size: 14px; font-weight: 600; margin-bottom: 4px; }
    .rec-meta { font-size: 11px; color: #9ca3af; }
    .rec-score { font-size: 13px; font-weight: 700; color: #2e75d1; }
    .cat-weapon { color: #dc2626; }
    .cat-skin { color: #7c3aed; }
    .cat-mission { color: #d97706; }
    """


def header_html() -> str:
    return """
    <div class="main-header-card">
        <div>
            <div class="header-title">In-Game Recommendation System</div>
            <div class="header-subtitle">Battle Royale Edition · Weapons · Skins · Missions</div>
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
    <div class="wrap">
        {header_html()}
        <div class="landing">
            <div class="hero">
                <div class="icon-box">🎮</div>
                <div class="welcome-title">Battle Royale Item Recommender</div>
                <p class="welcome-text">
                    Select a player and a recommendation model from the sidebar,
                    then click <strong>Get Recommendations</strong> to see personalised item suggestions.
                </p>
            </div>
            <div class="feature-cards">
                <div class="f-card">
                    <span class="f-icon">⚡</span>
                    <div class="f-title">Collaborative Filtering</div>
                    <div class="f-desc">Finds players similar to you and recommends what they liked using SVD matrix decomposition.</div>
                </div>
                <div class="f-card">
                    <span class="f-icon">🔍</span>
                    <div class="f-title">Content-Based Filtering</div>
                    <div class="f-desc">Recommends items with similar features to what you already rated 4 or 5 stars using cosine similarity.</div>
                </div>
                <div class="f-card">
                    <span class="f-icon">📊</span>
                    <div class="f-title">Full Evaluation</div>
                    <div class="f-desc">Both models evaluated using Precision@5, Recall@5, RMSE, and MAE with comparison charts.</div>
                </div>
            </div>
        </div>
    </div>
    </body></html>
    """


def get_recommendations(player_id: int, use_cbf: bool, k: int) -> pd.DataFrame:
    if use_cbf:
        recs = cbf_results[cbf_results["player_id"] == player_id].copy()
        recs = recs[recs["rank"] <= k]
        recs = recs.merge(
            items[["item_name", "category", "rarity"]], on="item_name", how="left"
        )
        recs["score"] = recs["similarity_score"]
    else:
        recs = cf_results[cf_results["player_id"] == player_id].copy()
        recs = recs[recs["rank"] <= k]
        recs = recs.merge(
            items[["item_id", "category", "rarity"]], on="item_id", how="left"
        )
        recs["score"] = recs["predicted_score"]
    return recs.sort_values("rank")


def category_class(cat: str) -> str:
    c = str(cat).lower()
    if c == "weapon":
        return "cat-weapon"
    if c == "skin":
        return "cat-skin"
    return "cat-mission"


def results_html(player_label: str, use_cbf: bool, k: int, player_id: int) -> str:
    recs = get_recommendations(player_id, use_cbf, k)
    model_name = "Content-Based Filtering" if use_cbf else "Collaborative Filtering"
    pill_class = "pill-cbf" if use_cbf else "pill-cf"

    cards = ""
    for _, row in recs.iterrows():
        cat = row.get("category", "Item")
        cat_cls = category_class(cat)
        rarity = row.get("rarity", "")
        rarity_txt = (
            f" · {rarity}"
            if pd.notna(rarity) and str(rarity) not in ("", "nan")
            else ""
        )
        cards += f"""
        <div class="rec-card">
            <div class="rec-rank">{int(row['rank'])}</div>
            <div class="rec-body">
                <div class="rec-name">{row['item_name']}</div>
                <div class="rec-meta"><span class="{cat_cls}">{cat}</span>{rarity_txt}</div>
            </div>
            <div class="rec-score">{row['score']:.4f}</div>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html><head><meta charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>{page_css()}</style>
    </head><body>
    <div class="wrap">
        {header_html()}
        <div class="results-wrap">
            <div class="results-header">
                <div>
                    <div class="results-title">Recommendations</div>
                    <div class="results-subtitle">{player_label} · Top {k} items</div>
                </div>
                <span class="model-pill {pill_class}">{model_name}</span>
            </div>
            <div class="rec-grid">{cards}</div>
        </div>
    </div>
    </body></html>
    """


# ── Main content ─────────────────────────────────────────────────────────────
if get_recs:
    components.html(
        results_html(selected_label, is_cbf, top_k, selected_player_id),
        height=520,
        scrolling=False,
    )
else:
    components.html(landing_html(), height=580, scrolling=False)
