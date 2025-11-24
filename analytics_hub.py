import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Analytics Hub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to match the design
st.markdown("""
<style>
    /* Main background */
    .main {
        background-color: #f8f9fa;
    }
    
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    /* Title styling */
    h1 {
        color: #1a1a1a !important;
        text-align: center;
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.5px;
    }
    
    /* Subtitle styling */
    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 1.25rem;
        margin-bottom: 3rem;
        font-weight: 400;
    }
    
    /* Section header styling */
    .section-header {
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 2rem;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 2rem;
        margin-top: 3rem;
    }
    
    /* Card container styling */
    div[data-testid="column"] {
        padding: 0.5rem;
    }
    
    /* Custom card styling */
    .custom-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        position: relative;
        min-height: 200px;
        display: flex;
        flex-direction: column;
    }
    
    .custom-card:hover {
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        transform: translateY(-5px);
    }
    
    /* Icon styling */
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
    
    /* Card title */
    .card-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 0.75rem;
    }
    
    /* Card description */
    .card-description {
        color: #6b7280;
        font-size: 1rem;
        line-height: 1.5;
        flex-grow: 1;
    }
    
    /* Coming soon badge */
    .coming-soon {
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
    
    /* Disabled card styling */
    .custom-card.disabled {
        opacity: 0.6;
    }
    
    .custom-card.disabled .card-title {
        color: #9ca3af;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        width: 100%;
        margin-top: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>Analytics Hub</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your central hub for dashboards and calculators</div>", unsafe_allow_html=True)

# Dashboards Data
dashboards = [
    {
        "title": "Performance Dashboard",
        "description": "Shows the live performance of all our brands",
        "url": "https://sgdashboards.streamlit.app/",
        "icon": "📊",
        "color": "blue",
        "coming_soon": False
    },
    {
        "title": "Opex",
        "description": "Track the expenses of your domain",
        "url": "#",
        "icon": "💲",
        "color": "teal",
        "coming_soon": False
    },
    {
        "title": "NPA Dashboard",
        "description": "Coming Soon",
        "url": "#",
        "icon": "⚠️",
        "color": "red",
        "coming_soon": True
    },
    {
        "title": "Marketing Dashboard",
        "description": "Coming Soon",
        "url": "#",
        "icon": "🎯",
        "color": "orange",
        "coming_soon": True
    },
    {
        "title": "Customer Complaints Dashboard",
        "description": "Coming Soon",
        "url": "#",
        "icon": "💬",
        "color": "purple",
        "coming_soon": True
    }
]

# Calculators Data
calculators = [
    {
        "title": "NBFC Projection Calculator",
        "description": "Visualize your STPL growth story in real time 📈",
        "url": "https://nbfclendingbusinesscalculatorfinal-2jeovxpeab8lxzqtflh3kp.streamlit.app/",
        "icon": "📈",
        "color": "green",
        "coming_soon": False
    },
    {
        "title": "Marketing Expense Requirement Calculator",
        "description": "Helps you to analyze the expense required for Marketing",
        "url": "https://subhamgargmarketinganalysis.streamlit.app/",
        "icon": "📣",
        "color": "orange",
        "coming_soon": False
    },
    {
        "title": "Work Force Requirement",
        "description": "Calculates the ideal team size based on workload, productivity, and target utilization.",
        "url": "https://sgssteamsize-eappd8e86tvycerctib4tsxgg.streamlit.app/",
        "icon": "👥",
        "color": "purple",
        "coming_soon": False
    },
    {
        "title": "Incentive Calculator NPA Team",
        "description": "Know the incentives earned by team members",
        "url": "https://incentivecalculatorpersonaltarget-4gepaam4wzwqohtor5m7kr.streamlit.app/",
        "icon": "🎁",
        "color": "blue",
        "coming_soon": False
    },
    {
        "title": "Projection Calculator",
        "description": "Analyse your growth in every FDPs and strategise accordingly.",
        "url": "https://shuhamgargprojectioncalculator.streamlit.app/",
        "icon": "🚀",
        "color": "teal",
        "coming_soon": False
    }
]

def create_card(item):
    """Create a card with proper styling"""
    disabled_class = "disabled" if item["coming_soon"] else ""
    coming_soon_badge = f'<div class="coming-soon">Coming Soon</div>' if item["coming_soon"] else ''
    
    card_html = f"""
    <div class="custom-card {disabled_class}">
        {coming_soon_badge}
        <div class="card-icon icon-{item['color']}">{item['icon']}</div>
        <div class="card-title">{item['title']}</div>
        <div class="card-description">{item['description']}</div>
    </div>
    """
    return card_html

# Dashboards Section
st.markdown('<div class="section-header">📊 Dashboards</div>', unsafe_allow_html=True)

cols = st.columns(3)
for idx, dashboard in enumerate(dashboards):
    with cols[idx % 3]:
        st.markdown(create_card(dashboard), unsafe_allow_html=True)
        if not dashboard["coming_soon"] and dashboard["url"] != "#":
            st.link_button(
                f"Open {dashboard['title']}",
                dashboard["url"],
                use_container_width=True
            )
        st.markdown("<br>", unsafe_allow_html=True)

# Calculators Section
st.markdown('<div class="section-header">🧮 Calculators</div>', unsafe_allow_html=True)

cols = st.columns(3)
for idx, calculator in enumerate(calculators):
    with cols[idx % 3]:
        st.markdown(create_card(calculator), unsafe_allow_html=True)
        if not calculator["coming_soon"] and calculator["url"] != "#":
            st.link_button(
                f"Open {calculator['title']}",
                calculator["url"],
                use_container_width=True
            )
        st.markdown("<br>", unsafe_allow_html=True)
