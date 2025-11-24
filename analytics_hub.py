import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Analytics Hub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a classy, modern dashboard
st.markdown("""
<style>
    /* Main background with gradient */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0;
    }
    
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Card styling */
    .dashboard-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        min-height: 200px;
    }
    
    .dashboard-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 5px;
        height: 100%;
        transition: width 0.3s ease;
    }
    
    .dashboard-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
    }
    
    .dashboard-card:hover::before {
        width: 100%;
        opacity: 0.1;
    }
    
    /* Color variants */
    .card-blue::before { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .card-green::before { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
    .card-orange::before { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); }
    .card-purple::before { background: linear-gradient(135deg, #30cfd0 0%, #330867 100%); }
    .card-teal::before { background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); }
    .card-red::before { background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); }
    
    /* Card title */
    .card-title {
        font-size: 1.5em;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 12px;
        letter-spacing: -0.5px;
    }
    
    /* Card description */
    .card-description {
        color: #4a5568;
        font-size: 1em;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    /* Coming soon badge */
    .coming-soon-badge {
        background: linear-gradient(135deg, #ffd89b 0%, #19547b 100%);
        color: white;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.75em;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* Section headers */
    .section-header {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px 30px;
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .section-title {
        font-size: 2.2em;
        font-weight: 800;
        color: white;
        margin: 0;
        display: flex;
        align-items: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .section-icon {
        font-size: 1.3em;
        margin-right: 15px;
    }
    
    /* Main title */
    .main-title {
        text-align: center;
        color: white;
        font-size: 3.5em;
        font-weight: 900;
        margin-bottom: 10px;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
        letter-spacing: -1px;
    }
    
    .main-subtitle {
        text-align: center;
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.3em;
        margin-bottom: 50px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        font-size: 1em;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Disable state for coming soon */
    .disabled-card {
        opacity: 0.7;
        cursor: not-allowed;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-title">📊 Analytics Hub</h1>', unsafe_allow_html=True)
st.markdown('<p class="main-subtitle">Your Premium Gateway to Data Intelligence & Business Insights</p>', unsafe_allow_html=True)

# Dashboards Data
dashboards = [
    {
        "title": "Performance Dashboard",
        "description": "Real-time insights into brand performance metrics, KPIs, and growth analytics across all business verticals",
        "url": "https://sgdashboards.streamlit.app/",
        "color": "blue",
        "icon": "📈",
        "coming_soon": False
    },
    {
        "title": "Opex Management",
        "description": "Comprehensive expense tracking and operational cost analysis to optimize your domain's financial efficiency",
        "url": "#",
        "color": "teal",
        "icon": "💰",
        "coming_soon": False
    },
    {
        "title": "NPA Dashboard",
        "description": "Advanced non-performing asset monitoring and risk assessment tools for portfolio management",
        "url": "#",
        "color": "red",
        "icon": "⚠️",
        "coming_soon": True
    },
    {
        "title": "Marketing Dashboard",
        "description": "Track campaign performance, ROI, and customer acquisition metrics in real-time",
        "url": "#",
        "color": "orange",
        "icon": "🎯",
        "coming_soon": True
    },
    {
        "title": "Customer Complaints Dashboard",
        "description": "Centralized complaint tracking, resolution analytics, and customer satisfaction insights",
        "url": "#",
        "color": "purple",
        "icon": "💬",
        "coming_soon": True
    }
]

# Calculators Data
calculators = [
    {
        "title": "NBFC Projection Calculator",
        "description": "Visualize your STPL growth trajectory with dynamic projections, revenue forecasts, and strategic planning tools 📈",
        "url": "https://nbfclendingbusinesscalculatorfinal-2jeovxpeab8lxzqtflh3kp.streamlit.app/",
        "color": "green",
        "icon": "📊",
        "coming_soon": False
    },
    {
        "title": "Marketing ROI Calculator",
        "description": "Analyze and optimize your marketing spend with precision expense modeling and ROI projections",
        "url": "https://subhamgargmarketinganalysis.streamlit.app/",
        "color": "orange",
        "icon": "📣",
        "coming_soon": False
    },
    {
        "title": "Workforce Optimizer",
        "description": "Data-driven team sizing based on workload analysis, productivity metrics, and optimal utilization rates",
        "url": "https://sgssteamsize-eappd8e86tvycerctib4tsxgg.streamlit.app/",
        "color": "purple",
        "icon": "👥",
        "coming_soon": False
    },
    {
        "title": "NPA Team Incentive Calculator",
        "description": "Transparent incentive computation system with personalized targets and performance-based rewards",
        "url": "https://incentivecalculatorpersonaltarget-4gepaam4wzwqohtor5m7kr.streamlit.app/",
        "color": "blue",
        "icon": "🎁",
        "coming_soon": False
    },
    {
        "title": "Growth Projection Engine",
        "description": "Strategic growth planning across FDPs with scenario modeling and data-driven strategy recommendations",
        "url": "https://shuhamgargprojectioncalculator.streamlit.app/",
        "color": "teal",
        "icon": "🚀",
        "coming_soon": False
    }
]

def create_card(item, index, category):
    """Create a beautiful card for dashboard or calculator"""
    coming_soon_html = '<div class="coming-soon-badge">🚧 Coming Soon</div>' if item["coming_soon"] else ''
    disabled_class = 'disabled-card' if item["coming_soon"] else ''
    
    card_html = f"""
    <div class="dashboard-card card-{item['color']} {disabled_class}">
        {coming_soon_html}
        <div style="font-size: 2.5em; margin-bottom: 15px;">{item['icon']}</div>
        <div class="card-title">{item['title']}</div>
        <div class="card-description">{item['description']}</div>
    </div>
    """
    return card_html

# Dashboards Section
st.markdown('''
<div class="section-header">
    <h2 class="section-title">
        <span class="section-icon">📊</span>
        Executive Dashboards
    </h2>
</div>
''', unsafe_allow_html=True)

cols = st.columns(3)
for idx, dashboard in enumerate(dashboards):
    with cols[idx % 3]:
        st.markdown(create_card(dashboard, idx, "dashboard"), unsafe_allow_html=True)
        if not dashboard["coming_soon"] and dashboard["url"] != "#":
            if st.button(f"🚀 Launch Dashboard", key=f"dashboard_{idx}", use_container_width=True):
                st.markdown(f'<meta http-equiv="refresh" content="0; url={dashboard["url"]}">', unsafe_allow_html=True)
                st.link_button("🔗 Open in New Tab", dashboard["url"], use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# Calculators Section
st.markdown('''
<div class="section-header">
    <h2 class="section-title">
        <span class="section-icon">🧮</span>
        Business Calculators
    </h2>
</div>
''', unsafe_allow_html=True)

cols = st.columns(3)
for idx, calculator in enumerate(calculators):
    with cols[idx % 3]:
        st.markdown(create_card(calculator, idx, "calculator"), unsafe_allow_html=True)
        if not calculator["coming_soon"] and calculator["url"] != "#":
            st.link_button(f"⚡ Open Calculator", calculator["url"], key=f"calculator_{idx}", use_container_width=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: white; padding: 20px; background: rgba(255, 255, 255, 0.1); border-radius: 15px; backdrop-filter: blur(10px);'>
    <p style='margin: 0; font-size: 1.1em; font-weight: 600;'>✨ Powered by Advanced Analytics & Business Intelligence</p>
    <p style='margin: 5px 0 0 0; font-size: 0.9em; opacity: 0.8;'>Built with ❤️ for Data-Driven Decision Making</p>
</div>
""", unsafe_allow_html=True)
