import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Analytics Hub",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for beautiful cards
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e9f2 100%);
    }
    
    .card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        height: 100%;
        border-left: 4px solid;
        cursor: pointer;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(0, 0, 0, 0.15);
    }
    
    .card-blue { border-left-color: #3b82f6; }
    .card-teal { border-left-color: #14b8a6; }
    .card-red { border-left-color: #ef4444; }
    .card-orange { border-left-color: #f97316; }
    .card-purple { border-left-color: #a855f7; }
    .card-green { border-left-color: #22c55e; }
    
    .card-title {
        font-size: 1.3em;
        font-weight: bold;
        color: #1f2937;
        margin-bottom: 10px;
    }
    
    .card-description {
        color: #6b7280;
        font-size: 0.95em;
        line-height: 1.5;
    }
    
    .coming-soon-badge {
        background: #fbbf24;
        color: #92400e;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.75em;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    
    .section-header {
        font-size: 2em;
        font-weight: bold;
        color: #1f2937;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
    }
    
    .header-icon {
        font-size: 1.2em;
        margin-right: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; font-size: 3em; color: #1f2937; margin-bottom: 10px;'>📊 Analytics Hub</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em; color: #6b7280; margin-bottom: 40px;'>Your central hub for dashboards and calculators</p>", unsafe_allow_html=True)

# Dashboards Data
dashboards = [
    {
        "title": "Performance Dashboard",
        "description": "Shows the live performance of all our brands",
        "url": "https://sgdashboards.streamlit.app/",
        "color": "blue",
        "coming_soon": False
    },
    {
        "title": "Opex",
        "description": "Track the expenses of your domain",
        "url": "#",
        "color": "teal",
        "coming_soon": False
    },
    {
        "title": "NPA Dashboard",
        "description": "Coming Soon",
        "url": "#",
        "color": "red",
        "coming_soon": True
    },
    {
        "title": "Marketing Dashboard",
        "description": "Coming Soon",
        "url": "#",
        "color": "orange",
        "coming_soon": True
    },
    {
        "title": "Customer Complaints Dashboard",
        "description": "Coming Soon",
        "url": "#",
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
        "color": "green",
        "coming_soon": False
    },
    {
        "title": "Marketing Expense Requirement Calculator",
        "description": "Helps you to analyze the expense required for Marketing",
        "url": "https://subhamgargmarketinganalysis.streamlit.app/",
        "color": "orange",
        "coming_soon": False
    },
    {
        "title": "Work Force Requirement",
        "description": "Calculates the ideal team size based on workload, productivity, and target utilization.",
        "url": "https://sgssteamsize-eappd8e86tvycerctib4tsxgg.streamlit.app/",
        "color": "purple",
        "coming_soon": False
    },
    {
        "title": "Incentive Calculator NPA Team",
        "description": "Know the incentives earned by team members",
        "url": "https://incentivecalculatorpersonaltarget-4gepaam4wzwqohtor5m7kr.streamlit.app/",
        "color": "blue",
        "coming_soon": False
    },
    {
        "title": "Projection Calculator",
        "description": "Analyse your growth in every FDPs and strategise accordingly.",
        "url": "https://shuhamgargprojectioncalculator.streamlit.app/",
        "color": "teal",
        "coming_soon": False
    }
]

def create_card(item):
    coming_soon_html = f'<div class="coming-soon-badge">Coming Soon</div>' if item["coming_soon"] else ''
    
    card_html = f"""
    <div class="card card-{item['color']}">
        {coming_soon_html}
        <div class="card-title">{item['title']}</div>
        <div class="card-description">{item['description']}</div>
    </div>
    """
    return card_html

# Dashboards Section
st.markdown('<div class="section-header"><span class="header-icon">📊</span> Dashboards</div>', unsafe_allow_html=True)

cols = st.columns(3)
for idx, dashboard in enumerate(dashboards):
    with cols[idx % 3]:
        st.markdown(create_card(dashboard), unsafe_allow_html=True)
        if not dashboard["coming_soon"] and dashboard["url"] != "#":
            if st.button(f"Open {dashboard['title']}", key=f"dash_{idx}", use_container_width=True):
                st.markdown(f'<meta http-equiv="refresh" content="0; url={dashboard["url"]}">', unsafe_allow_html=True)
                st.link_button("🔗 Click here if not redirected", dashboard["url"], use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Calculators Section
st.markdown('<div class="section-header"><span class="header-icon">🧮</span> Calculators</div>', unsafe_allow_html=True)

cols = st.columns(3)
for idx, calculator in enumerate(calculators):
    with cols[idx % 3]:
        st.markdown(create_card(calculator), unsafe_allow_html=True)
        if not calculator["coming_soon"] and calculator["url"] != "#":
            st.link_button(f"Open {calculator['title']}", calculator["url"], key=f"calc_{idx}", use_container_width=True)
