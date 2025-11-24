import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Analytics Hub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    /* Custom card */
    .card-container {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        position: relative;
        min-height: 220px;
        margin-bottom: 1.5rem;
    }
    
    .card-container:hover {
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        transform: translateY(-5px);
    }
    
    .card-icon {
        width: 72px;
        height: 72px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        margin-bottom: 1.5rem;
        color: white;
    }
    
    .icon-blue { background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); }
    .icon-teal { background: linear-gradient(135deg, #14b8a6 0%, #0d9488 100%); }
    .icon-red { background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); }
    .icon-orange { background: linear-gradient(135deg, #f97316 0%, #ea580c 100%); }
    .icon-purple { background: linear-gradient(135deg, #a855f7 0%, #9333ea 100%); }
    .icon-green { background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%); }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 0.75rem;
    }
    
    .card-description {
        color: #6b7280;
        font-size: 1rem;
        line-height: 1.5;
    }
    
    .coming-soon-badge {
        position: absolute;
        top: 1.5rem;
        right: 1.5rem;
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        color: #78350f;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 600;
    }
    
    .card-disabled {
        opacity: 0.6;
    }
    
    .card-disabled .card-title {
        color: #9ca3af;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div style="text-align: center; margin-bottom: 3rem;">
    <h1 style="font-size: 3.5rem; font-weight: 700; color: #1a1a1a; margin-bottom: 0.5rem;">Analytics Hub</h1>
    <p style="font-size: 1.25rem; color: #6b7280;">Your central hub for dashboards and calculators</p>
</div>
""", unsafe_allow_html=True)

# Dashboards
dashboards = [
    {"title": "Performance Dashboard", "desc": "Shows the live performance of all our brands", 
     "url": "https://sgdashboards.streamlit.app/", "icon": "📊", "color": "blue", "soon": False},
    {"title": "Opex", "desc": "Track the expenses of your domain", 
     "url": "#", "icon": "💲", "color": "teal", "soon": False},
    {"title": "NPA Dashboard", "desc": "Coming Soon", 
     "url": "#", "icon": "⚠️", "color": "red", "soon": True},
    {"title": "Marketing Dashboard", "desc": "Coming Soon", 
     "url": "#", "icon": "🎯", "color": "orange", "soon": True},
    {"title": "Customer Complaints Dashboard", "desc": "Coming Soon", 
     "url": "#", "icon": "💬", "color": "purple", "soon": True},
]

# Calculators
calculators = [
    {"title": "NBFC Projection Calculator", "desc": "Visualize your STPL growth story in real time 📈",
     "url": "https://nbfclendingbusinesscalculatorfinal-2jeovxpeab8lxzqtflh3kp.streamlit.app/", 
     "icon": "📈", "color": "green", "soon": False},
    {"title": "Marketing Expense Requirement Calculator", "desc": "Helps you to analyze the expense required for Marketing",
     "url": "https://subhamgargmarketinganalysis.streamlit.app/", 
     "icon": "📣", "color": "orange", "soon": False},
    {"title": "Work Force Requirement", "desc": "Calculates the ideal team size based on workload, productivity, and target utilization.",
     "url": "https://sgssteamsize-eappd8e86tvycerctib4tsxgg.streamlit.app/", 
     "icon": "👥", "color": "purple", "soon": False},
    {"title": "Incentive Calculator NPA Team", "desc": "Know the incentives earned by team members",
     "url": "https://incentivecalculatorpersonaltarget-4gepaam4wzwqohtor5m7kr.streamlit.app/", 
     "icon": "🎁", "color": "blue", "soon": False},
    {"title": "Projection Calculator", "desc": "Analyse your growth in every FDPs and strategise accordingly.",
     "url": "https://shuhamgargprojectioncalculator.streamlit.app/", 
     "icon": "🚀", "color": "teal", "soon": False},
]

# Dashboards Section
st.markdown("""
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 2rem; margin-top: 2rem;">
    <span style="font-size: 2rem;">📊</span>
    <h2 style="font-size: 2rem; font-weight: 700; color: #1a1a1a; margin: 0;">Dashboards</h2>
</div>
""", unsafe_allow_html=True)

cols = st.columns(3)
for idx, item in enumerate(dashboards):
    with cols[idx % 3]:
        disabled = "card-disabled" if item["soon"] else ""
        badge = f'<div class="coming-soon-badge">Coming Soon</div>' if item["soon"] else ''
        
        st.markdown(f"""
        <div class="card-container {disabled}">
            {badge}
            <div class="card-icon icon-{item['color']}">{item['icon']}</div>
            <div class="card-title">{item['title']}</div>
            <div class="card-description">{item['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        if not item["soon"] and item["url"] != "#":
            st.link_button(f"Open {item['title']}", item["url"], use_container_width=True)

# Calculators Section
st.markdown("""
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 2rem; margin-top: 3rem;">
    <span style="font-size: 2rem;">🧮</span>
    <h2 style="font-size: 2rem; font-weight: 700; color: #1a1a1a; margin: 0;">Calculators</h2>
</div>
""", unsafe_allow_html=True)

cols = st.columns(3)
for idx, item in enumerate(calculators):
    with cols[idx % 3]:
        disabled = "card-disabled" if item["soon"] else ""
        badge = f'<div class="coming-soon-badge">Coming Soon</div>' if item["soon"] else ''
        
        st.markdown(f"""
        <div class="card-container {disabled}">
            {badge}
            <div class="card-icon icon-{item['color']}">{item['icon']}</div>
            <div class="card-title">{item['title']}</div>
            <div class="card-description">{item['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        if not item["soon"] and item["url"] != "#":
            st.link_button(f"Open {item['title']}", item["url"], use_container_width=True)
