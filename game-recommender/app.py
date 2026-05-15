import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# ── Page config — MUST be first Streamlit command ─────────────────────────────
st.set_page_config(
    page_title="GameRec – Item Recommender",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS (matches mockup design) ────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: #F7F7F8 !important;
    border-right: 0.5px solid #E4E4E7 !important;
}
[data-testid="stSidebar"] > div:first-child { padding-top: 1.5rem; }
[data-testid="stSidebar"] .stButton button {
    width: 100%; background: #378ADD !important; color: white !important;
    border: none !important; border-radius: 8px !important;
    font-size: 13px !important; font-weight: 500 !important;
    padding: 0.55rem 0 !important; margin-top: 0.5rem;
}
[data-testid="stSidebar"] .stButton button:hover { opacity: 0.88 !important; }
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stRadio label,
[data-testid="stSidebar"] .stSlider label {
    font-size: 10.5px !important; font-weight: 500 !important;
    color: #A1A1AA !important; text-transform: uppercase; letter-spacing: 0.06em;
}

/* Main */
.block-container { padding: 1.75rem 2rem 2rem !important; max-width: 100% !important; }

/* Page title */
.page-title { font-size: 20px; font-weight: 600; color: #18181B; margin: 0 0 2px; }
.page-sub   { font-size: 13px; color: #71717A; margin: 0 0 1.25rem; }

/* Player banner */
.player-banner {
    background: #F7F7F8; border: 0.5px solid #E4E4E7; border-radius: 12px;
    padding: 0.85rem 1.1rem; display: flex; align-items: center;
    gap: 13px; margin-bottom: 1.25rem;
}
.avatar {
    width: 40px; height: 40px; border-radius: 50%; background: #E6F1FB;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; font-weight: 600; color: #185FA5; flex-shrink: 0;
}
.player-name  { font-size: 14px; font-weight: 600; color: #18181B; }
.player-meta  { font-size: 12px; color: #71717A; margin-top: 2px; }
.badge        { display: inline-block; padding: 2px 9px; border-radius: 20px; font-size: 11px; font-weight: 500; margin-left: 6px; }
.badge-aggressive { background: #FAEEDA; color: #854F0B; }
.badge-explorer   { background: #E6F1FB; color: #185FA5; }
.badge-support    { background: #E1F5EE; color: #085041; }
.badge-collector  { background: #EEEDFE; color: #3C3489; }
.badge-sniper     { background: #F1EFE8; color: #444441; }
.model-badge-label { font-size: 11px; color: #A1A1AA; }
.model-badge       { font-size: 12px; font-weight: 500; color: #185FA5; }

/* Metric cards */
.metric-card { background: #F7F7F8; border: 0.5px solid #E4E4E7; border-radius: 10px; padding: 0.7rem 0.95rem; }
.metric-label { font-size: 11px; color: #A1A1AA; margin-bottom: 2px; }
.metric-val   { font-size: 22px; font-weight: 600; color: #18181B; }

/* Section title */
.section-title {
    font-size: 12px; font-weight: 500; color: #71717A;
    text-transform: uppercase; letter-spacing: 0.05em; margin: 0.5rem 0 0.65rem;
}

/* Item cards */
.item-card {
    background: #FFFFFF; border: 0.5px solid #E4E4E7; border-radius: 12px;
    padding: 0.75rem 1rem; display: flex; align-items: center;
    gap: 13px; margin-bottom: 7px;
}
.rank      { font-size: 13px; font-weight: 500; color: #A1A1AA; min-width: 20px; }
.item-icon {
    width: 34px; height: 34px; border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    font-size: 17px; flex-shrink: 0;
}
.item-name { font-size: 13px; font-weight: 600; color: #18181B; }
.item-type { font-size: 11px; color: #A1A1AA; }
.stat-row  { display: flex; gap: 6px; margin-top: 4px; flex-wrap: wrap; }
.stat      { font-size: 11px; color: #52525B; background: #F4F4F5; padding: 2px 7px; border-radius: 5px; }

/* Rarity */
.rarity           { font-size: 11px; font-weight: 500; padding: 3px 10px; border-radius: 20px; white-space: nowrap; }
.rarity-Common    { background: #F1EFE8; color: #444441; }
.rarity-Uncommon  { background: #E1F5EE; color: #085041; }
.rarity-Rare      { background: #E6F1FB; color: #0C447C; }
.rarity-Epic      { background: #EEEDFE; color: #3C3489; }
.rarity-Legendary { background: #FAEEDA; color: #633806; }

/* Score bar */
.score-wrap   { display: flex; align-items: center; gap: 7px; min-width: 90px; }
.score-bar-bg { flex: 1; height: 5px; background: #F0F0F0; border-radius: 10px; overflow: hidden; }
.score-bar    { height: 100%; border-radius: 10px; background: #378ADD; }
.score-val    { font-size: 12px; font-weight: 500; color: #52525B; min-width: 32px; text-align: right; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { gap: 6px; background: transparent !important; border-bottom: 0.5px solid #E4E4E7 !important; }
.stTabs [data-baseweb="tab"] {
    border-radius: 20px 20px 0 0 !important; font-size: 12px !important;
    font-weight: 500 !important; padding: 6px 14px !important;
    border: 0.5px solid transparent !important;
    background: transparent !important; color: #71717A !important;
}
.stTabs [aria-selected="true"] { background: #E6F1FB !important; border-color: #378ADD !important; color: #185FA5 !important; }
.stTabs [data-baseweb="tab-panel"] { padding-top: 1rem !important; }

/* Stats bar */
.stats-bar { font-size: 11px; color: #A1A1AA; border-top: 0.5px solid #E4E4E7; padding-top: 0.75rem; margin-top: 0.5rem; }

/* Sidebar logo */
.sidebar-logo { display: flex; align-items: center; gap: 10px; font-size: 16px; font-weight: 600; color: #18181B; margin-bottom: 1.75rem; padding: 0 0.25rem; }
.logo-box { width: 26px; height: 26px; background: #378ADD; border-radius: 7px; display: inline-block; }
</style>
""", unsafe_allow_html=True)


# ── Metric values — 04_evaluation.ipynb 
CF_RMSE       = 1.1673  
CF_MAE        = 1.0330  
CF_PRECISION  = 0.0357  
CF_RECALL     = 0.1696   
CBF_PRECISION = 0.0000   
CBF_RECALL    = 0.0000   
# ────────────────────────────────────────
@st.cache_data
def load_data():
    interactions = pd.read_csv('data/interactions.csv')
    items        = pd.read_csv('data/items.csv')
    players      = pd.read_csv('data/players.csv')
    cf_results   = pd.read_csv('outputs/cf_results.csv')
    cbf_results  = pd.read_csv('outputs/cbf_results.csv')
    return interactions, items, players, cf_results, cbf_results

@st.cache_resource
def load_models():
    with open('models/cf_model.pkl', 'rb') as f:
        cf_model = pickle.load(f)
    with open('models/cbf_similarity.pkl', 'rb') as f:
        cbf_similarity = pickle.load(f)
    return cf_model, cbf_similarity

interactions, items, players, cf_results, cbf_results = load_data()
cf_model, cbf_similarity = load_models()


# ── Recommendation functions ──────────────────────────────────────────────────
def get_cf_recommendations(player_id, n=5):
    """cf_results.csv ගෙන් top-N recommendations"""
    recs = cf_results[cf_results['player_id'] == player_id].copy()
    recs = recs.sort_values('rank').head(n)
    return list(zip(recs['item_name'], recs['predicted_score'].round(2)))

def get_cbf_recommendations(player_id, n=5):
    """cbf_results.csv ගෙන් top-N recommendations"""
    recs = cbf_results[cbf_results['player_id'] == player_id].copy()
    recs = recs.sort_values('rank').head(n)
    return list(zip(recs['item_name'], recs['similarity_score'].round(4)))


# ── Helper maps ───────────────────────────────────────────────────────────────
RARITY_BG = {
    'Legendary': '#FAEEDA', 'Epic': '#EEEDFE',
    'Rare': '#E6F1FB', 'Uncommon': '#E1F5EE', 'Common': '#F4F4F5',
}
CATEGORY_ICON = {
    'Weapon': '⚔️', 'Outfit': '👘', 'Emote': '💃',
    'Vehicle': '🚗', 'Mission': '🎯',
}
STYLE_BADGE = {
    'aggressive': 'badge-aggressive', 'explorer': 'badge-explorer',
    'support': 'badge-support', 'collector': 'badge-collector', 'sniper': 'badge-sniper',
}

def get_item_info(item_name):
    row = items[items['item_name'] == item_name]
    return row.iloc[0] if not row.empty else None


# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        '<div class="sidebar-logo"><div class="logo-box"></div>GameRec</div>',
        unsafe_allow_html=True
    )

    st.markdown('<p style="font-size:10.5px;font-weight:500;color:#A1A1AA;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:4px;">Select Player</p>', unsafe_allow_html=True)
    player_options = [
        f"{row['player_name']} ({row['play_style']})"
        for _, row in players.iterrows()
    ]
    selected_label     = st.selectbox("Select Player", player_options, label_visibility="collapsed")
    selected_name      = selected_label.split(" (")[0]
    selected_player    = players[players['player_name'] == selected_name].iloc[0]
    selected_player_id = int(selected_player['player_id'])

    st.markdown('<p style="font-size:10.5px;font-weight:500;color:#A1A1AA;text-transform:uppercase;letter-spacing:0.06em;margin:1rem 0 4px;">Model</p>', unsafe_allow_html=True)
    model_choice = st.radio(
        "Model", ["Collaborative Filtering", "Content-Based Filtering"],
        label_visibility="collapsed"
    )

    st.markdown('<p style="font-size:10.5px;font-weight:500;color:#A1A1AA;text-transform:uppercase;letter-spacing:0.06em;margin:1rem 0 4px;">Top K Items</p>', unsafe_allow_html=True)
    top_k = st.slider("Top K", min_value=3, max_value=10, value=5, label_visibility="collapsed")

    btn_clicked = st.button("🎯  Get Recommendations")

    st.markdown(
        f'<div class="stats-bar">{len(players)} players · {len(items)} items · {len(interactions)} interactions</div>',
        unsafe_allow_html=True
    )


# ── MAIN ──────────────────────────────────────────────────────────────────────
st.markdown('<p class="page-title">Recommendations</p>', unsafe_allow_html=True)
st.markdown(f'<p class="page-sub">Top {top_k} items suggested for this player</p>', unsafe_allow_html=True)

if btn_clicked:

    # Player banner
    style       = str(selected_player.get('play_style', '')).lower()
    level       = selected_player.get('level', '?')
    p_rated     = interactions[interactions['player_id'] == selected_player_id]
    avg_r       = round(p_rated['rating'].mean(), 1) if len(p_rated) > 0 else '–'
    n_rated     = len(p_rated)
    initials    = selected_name[:2].upper()
    badge_cls   = STYLE_BADGE.get(style, 'badge-aggressive')
    model_short = "Collaborative" if model_choice == "Collaborative Filtering" else "Content-Based"

    st.markdown(f"""
    <div class="player-banner">
      <div class="avatar">{initials}</div>
      <div>
        <div class="player-name">{selected_name} <span class="badge {badge_cls}">{style.capitalize()}</span></div>
        <div class="player-meta">Level {level} &nbsp;·&nbsp; {n_rated} items rated &nbsp;·&nbsp; Avg rating {avg_r}</div>
      </div>
      <div style="margin-left:auto;text-align:right;">
        <div class="model-badge-label">Model</div>
        <div class="model-badge">{model_short}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🎯 Top picks", "📋 Item details", "📊 Model metrics"])

    # ── TAB 1 ──────────────────────────────────────────────────────────────
    with tab1:
        sel_precision = CF_PRECISION if model_choice == "Collaborative Filtering" else CBF_PRECISION
        sel_recall    = CF_RECALL    if model_choice == "Collaborative Filtering" else CBF_RECALL

        mc1, mc2 = st.columns(2)
        mc1.markdown(f'<div class="metric-card"><div class="metric-label">Precision@5</div><div class="metric-val">{sel_precision:.4f}</div></div>', unsafe_allow_html=True)
        mc2.markdown(f'<div class="metric-card"><div class="metric-label">Recall@5</div><div class="metric-val">{sel_recall:.4f}</div></div>', unsafe_allow_html=True)

        st.markdown('<div class="section-title" style="margin-top:1rem;">Recommended items</div>', unsafe_allow_html=True)

        with st.spinner("Getting recommendations…"):
            if model_choice == "Collaborative Filtering":
                recs = get_cf_recommendations(selected_player_id, n=top_k)
            else:
                recs = get_cbf_recommendations(selected_player_id, n=top_k)

        if not recs:
            st.warning(f"No recommendations found for {selected_name}.")
        else:
            max_score = float(recs[0][1]) if recs[0][1] > 0 else 1.0

            for rank, (item_name, score) in enumerate(recs, 1):
                info = get_item_info(item_name)

                if info is not None:
                    category  = str(info.get('category', 'Item'))
                    item_type = str(info.get('type', '–'))
                    rarity    = str(info.get('rarity', 'Common'))
                    damage    = info.get('damage', '–')
                    price     = info.get('price', '–')
                    rng       = info.get('range', '–')
                else:
                    category, item_type, rarity = 'Item', '–', 'Common'
                    damage, price, rng = '–', '–', '–'

                icon    = CATEGORY_ICON.get(category, '🎮')
                bg      = RARITY_BG.get(rarity, '#F4F4F5')
                r_cls   = f'rarity-{rarity}'
                bar_pct = int((float(score) / max_score) * 100)
                score_display = f"{score:.2f}" if float(score) > 1 else f"{score:.4f}"

                st.markdown(f"""
                <div class="item-card">
                  <div class="rank">#{rank}</div>
                  <div class="item-icon" style="background:{bg};">{icon}</div>
                  <div style="flex:1;min-width:0;">
                    <div class="item-name">{item_name}</div>
                    <div class="item-type">{item_type}</div>
                    <div class="stat-row">
                      <span class="stat">DMG {damage}</span>
                      <span class="stat">RNG {rng}</span>
                      <span class="stat">{price}g</span>
                    </div>
                  </div>
                  <span class="rarity {r_cls}">{rarity}</span>
                  <div class="score-wrap">
                    <div class="score-bar-bg"><div class="score-bar" style="width:{bar_pct}%;"></div></div>
                    <span class="score-val">{score_display}</span>
                  </div>
                </div>
                """, unsafe_allow_html=True)

    # ── TAB 2 ──────────────────────────────────────────────────────────────
    with tab2:
        st.markdown('<div class="section-title">Full item details</div>', unsafe_allow_html=True)
        if recs:
            rec_names = [r[0] for r in recs]
            detail_df = items[items['item_name'].isin(rec_names)].copy()
            rank_map  = {name: i+1 for i, (name, _) in enumerate(recs)}
            detail_df['rank'] = detail_df['item_name'].map(rank_map)
            detail_df = detail_df.sort_values('rank').drop(columns=['rank'])
            st.dataframe(detail_df, use_container_width=True, hide_index=True)
        else:
            st.info("Get recommendations first.")

    # ── TAB 3 ──────────────────────────────────────────────────────────────
    with tab3:
        st.markdown('<div class="section-title">Model performance metrics</div>', unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
        m1.markdown(f'<div class="metric-card"><div class="metric-label">CF RMSE</div><div class="metric-val">{CF_RMSE:.4f}</div></div>', unsafe_allow_html=True)
        m2.markdown(f'<div class="metric-card"><div class="metric-label">CF MAE</div><div class="metric-val">{CF_MAE:.4f}</div></div>', unsafe_allow_html=True)
        m3.markdown(f'<div class="metric-card"><div class="metric-label">CF Precision@5</div><div class="metric-val">{CF_PRECISION:.4f}</div></div>', unsafe_allow_html=True)
        m4.markdown(f'<div class="metric-card"><div class="metric-label">CF Recall@5</div><div class="metric-val">{CF_RECALL:.4f}</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        mc1, mc2 = st.columns(2)
        mc1.markdown(f'<div class="metric-card"><div class="metric-label">CBF Precision@5</div><div class="metric-val">{CBF_PRECISION:.4f}</div></div>', unsafe_allow_html=True)
        mc2.markdown(f'<div class="metric-card"><div class="metric-label">CBF Recall@5</div><div class="metric-val">{CBF_RECALL:.4f}</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if os.path.exists('outputs/metrics_chart.png'):
            st.image('outputs/metrics_chart.png', use_column_width=True)
        else:
            st.info("metrics_chart.png එක නෑ — 04_evaluation.ipynb run කරන්න.")

else:
    st.markdown("""
    <div style="text-align:center;padding:5rem 2rem;color:#A1A1AA;">
      <div style="font-size:52px;margin-bottom:1rem;">🎮</div>
      <div style="font-size:15px;font-weight:500;color:#71717A;margin-bottom:8px;">Ready to recommend</div>
      <div style="font-size:13px;">Select a player and model from the sidebar,<br>then click <strong>Get Recommendations</strong></div>
    </div>
    """, unsafe_allow_html=True)

