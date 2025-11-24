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
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
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
    
    /* Custom card styling */
    div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        border-left: 5px solid;
        transition: all 0.3s ease;
    }
    
    h1 {
        color: white !important;
        text-align: center;
        font-size: 3.5em !important;
        font-weight: 900 !important;
        margin-bottom: 0.2em !important;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
    }
    
    h2 {
        color: white !important;
        font-size: 2.2em !important;
        font-weight: 800 !important;
        margin-top: 1em !important;
        margin-bottom: 0.5em !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    h3 {
        color: #1a202c !important;
        font-size: 1.5em !important;
        font-weight: 700 !important;
    }
    
    p {
        color: #4a5568 !important;
        line-height: 1.6 !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("📊 Analytics Hub")
st.markdown("<p style='text-align: center; color: rgba(255, 255, 255, 0.9); font-size: 1.3em; margin-bottom: 2em;'>Your Premium Gateway to Data Intelligence & Business Insights</p>", unsafe_allow_html=True)

# Dashboards Data
dashboards = [
    {
        "title": "Performance Dashboard",
        "description": "Real-time insights into brand performance metrics, KPIs, and growth analytics across all business verticals",
        "url": "https://sgdashboards.streamlit.app/",
        "icon": "📈",
        "coming_soon": False
    },
    {
        "title": "Opex Management",
        "description": "Comprehensive expense tracking and operational cost analysis to optimize your domain's financial efficiency",
        "url": "#",
        "icon": "💰",
        "coming_soon": False
    },
    {
        "title": "NPA Dashboard",
        "description": "Advanced non-performing asset monitoring and risk assessment tools for portfolio management",
        "url": "#",
        "icon": "⚠️",
        "coming_soon": True
    },
    {
        "title": "Marketing Dashboard",
        "description": "Track campaign performance, ROI, and customer acquisition metrics in real-time",
        "url": "#",
        "icon": "🎯",
        "coming_soon": True
    },
    {
        "title": "Customer Complaints Dashboard",
        "description": "Centralized complaint tracking, resolution analytics, and customer satisfaction insights",
        "url": "#",
        "icon": "💬",
        "coming_soon": True
    }
]

# Calculators Data
calculators = [
    {
        "title": "NBFC Projection Calculator",
        "description": "Visualize your STPL growth trajectory with dynamic projections, revenue forecasts, and strategic planning tools",
        "url": "https://nbfclendingbusinesscalculatorfinal-2jeovxpeab8lxzqtflh3kp.streamlit.app/",
        "icon": "📊",
        "coming_soon": False
    },
    {
        "title": "Marketing ROI Calculator",
        "description": "Analyze and optimize your marketing spend with precision expense modeling and ROI projections",
        "url": "https://subhamgargmarketinganalysis.streamlit.app/",
        "icon": "📣",
        "coming_soon": False
    },
    {
        "title": "Workforce Optimizer",
        "description": "Data-driven team sizing based on workload analysis, productivity metrics, and optimal utilization rates",
        "url": "https://sgssteamsize-eappd8e86tvycerctib4tsxgg.streamlit.app/",
        "icon": "👥",
        "coming_soon": False
    },
    {
        "title": "NPA Team Incentive Calculator",
        "description": "Transparent incentive computation system with personalized targets and performance-based rewards",
        "url": "https://incentivecalculatorpersonaltarget-4gepaam4wzwqohtor5m7kr.streamlit.app/",
        "icon": "🎁",
        "coming_soon": False
    },
    {
        "title": "Growth Projection Engine",
        "description": "Strategic growth planning across FDPs with scenario modeling and data-driven strategy recommendations",
        "url": "https://shuhamgargprojectioncalculator.streamlit.app/",
        "icon": "🚀",
        "coming_soon": False
    }
]

# Dashboards Section
st.header("📊 Executive Dashboards")

cols = st.columns(3)
for idx, dashboard in enumerate(dashboards):
    with cols[idx % 3]:
        with st.container():
            if dashboard["coming_soon"]:
                st.markdown(f"**🚧 COMING SOON**")
            
            st.markdown(f"### {dashboard['icon']} {dashboard['title']}")
            st.write(dashboard['description'])
            
            if not dashboard["coming_soon"] and dashboard["url"] != "#":
                st.link_button(
                    "🚀 Launch Dashboard",
                    dashboard["url"],
                    use_container_width=True
                )
            st.markdown("<br>", unsafe_allow_html=True)

# Calculators Section
st.header("🧮 Business Calculators")

cols = st.columns(3)
for idx, calculator in enumerate(calculators):
    with cols[idx % 3]:
        with st.container():
            if calculator["coming_soon"]:
                st.markdown(f"**🚧 COMING SOON**")
            
            st.markdown(f"### {calculator['icon']} {calculator['title']}")
            st.write(calculator['description'])
            
            if not calculator["coming_soon"] and calculator["url"] != "#":
                st.link_button(
                    "⚡ Open Calculator",
                    calculator["url"],
                    use_container_width=True
                )
            st.markdown("<br>", unsafe_allow_html=True)

# Footer
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: white; padding: 20px; background: rgba(255, 255, 255, 0.1); border-radius: 15px; backdrop-filter: blur(10px); margin-top: 3em;'>
    <p style='margin: 0; font-size: 1.1em; font-weight: 600;'>✨ Powered by Advanced Analytics & Business Intelligence</p>
    <p style='margin: 5px 0 0 0; font-size: 0.9em; opacity: 0.8;'>Built with ❤️ for Data-Driven Decision Making</p>
</div>
""", unsafe_allow_html=True)
