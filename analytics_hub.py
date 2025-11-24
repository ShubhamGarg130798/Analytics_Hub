import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="Analytics Hub", page_icon="📊", layout="wide")

# Complete HTML/CSS/JS solution
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background-color: #f8f9fa;
            padding: 40px 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 60px;
        }
        
        .main-title {
            font-size: 3.5rem;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 12px;
        }
        
        .subtitle {
            font-size: 1.25rem;
            color: #6b7280;
        }
        
        .section-header {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 2rem;
            font-weight: 700;
            color: #1a1a1a;
            margin: 50px 0 30px 0;
        }
        
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 24px;
            margin-bottom: 40px;
        }
        
        .card {
            background: white;
            border-radius: 16px;
            padding: 32px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            position: relative;
            min-height: 240px;
            display: flex;
            flex-direction: column;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        }
        
        .card.disabled {
            opacity: 0.6;
        }
        
        .card-icon {
            width: 72px;
            height: 72px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            margin-bottom: 20px;
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
            margin-bottom: 12px;
        }
        
        .card.disabled .card-title {
            color: #9ca3af;
        }
        
        .card-description {
            color: #6b7280;
            font-size: 1rem;
            line-height: 1.6;
            flex-grow: 1;
        }
        
        .coming-soon-badge {
            position: absolute;
            top: 24px;
            right: 24px;
            background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
            color: #78350f;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.875rem;
            font-weight: 600;
        }
        
        .btn {
            display: inline-block;
            width: 100%;
            margin-top: 16px;
            padding: 12px 24px;
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
            color: white;
            text-decoration: none;
            text-align: center;
            border-radius: 10px;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
        }
        
        @media (max-width: 768px) {
            .cards-grid {
                grid-template-columns: 1fr;
            }
            
            .main-title {
                font-size: 2.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="main-title">Analytics Hub</h1>
            <p class="subtitle">Your central hub for dashboards and calculators</p>
        </div>
        
        <div class="section-header">
            <span>📊</span>
            <span>Dashboards</span>
        </div>
        
        <div class="cards-grid">
            <div class="card">
                <div class="card-icon icon-blue">📊</div>
                <div class="card-title">Performance Dashboard</div>
                <div class="card-description">Shows the live performance of all our brands</div>
                <a href="https://sgdashboards.streamlit.app/" target="_blank" class="btn">Open Performance Dashboard</a>
            </div>
            
            <div class="card">
                <div class="card-icon icon-teal">💲</div>
                <div class="card-title">Opex</div>
                <div class="card-description">Track the expenses of your domain</div>
            </div>
            
            <div class="card disabled">
                <div class="coming-soon-badge">Coming Soon</div>
                <div class="card-icon icon-red">⚠️</div>
                <div class="card-title">NPA Dashboard</div>
                <div class="card-description">Coming Soon</div>
            </div>
            
            <div class="card disabled">
                <div class="coming-soon-badge">Coming Soon</div>
                <div class="card-icon icon-orange">🎯</div>
                <div class="card-title">Marketing Dashboard</div>
                <div class="card-description">Coming Soon</div>
            </div>
            
            <div class="card disabled">
                <div class="coming-soon-badge">Coming Soon</div>
                <div class="card-icon icon-purple">💬</div>
                <div class="card-title">Customer Complaints Dashboard</div>
                <div class="card-description">Coming Soon</div>
            </div>
        </div>
        
        <div class="section-header">
            <span>🧮</span>
            <span>Calculators</span>
        </div>
        
        <div class="cards-grid">
            <div class="card">
                <div class="card-icon icon-green">📈</div>
                <div class="card-title">NBFC Projection Calculator</div>
                <div class="card-description">Visualize your STPL growth story in real time 📈</div>
                <a href="https://nbfclendingbusinesscalculatorfinal-2jeovxpeab8lxzqtflh3kp.streamlit.app/" target="_blank" class="btn">Open NBFC Projection Calculator</a>
            </div>
            
            <div class="card">
                <div class="card-icon icon-orange">📣</div>
                <div class="card-title">Marketing Expense Requirement Calculator</div>
                <div class="card-description">Helps you to analyze the expense required for Marketing</div>
                <a href="https://subhamgargmarketinganalysis.streamlit.app/" target="_blank" class="btn">Open Marketing Expense Requirement Calculator</a>
            </div>
            
            <div class="card">
                <div class="card-icon icon-purple">👥</div>
                <div class="card-title">Work Force Requirement</div>
                <div class="card-description">Calculates the ideal team size based on workload, productivity, and target utilization.</div>
                <a href="https://sgssteamsize-eappd8e86tvycerctib4tsxgg.streamlit.app/" target="_blank" class="btn">Open Work Force Requirement</a>
            </div>
            
            <div class="card">
                <div class="card-icon icon-blue">🎁</div>
                <div class="card-title">Incentive Calculator NPA Team</div>
                <div class="card-description">Know the incentives earned by team members</div>
                <a href="https://incentivecalculatorpersonaltarget-4gepaam4wzwqohtor5m7kr.streamlit.app/" target="_blank" class="btn">Open Incentive Calculator NPA Team</a>
            </div>
            
            <div class="card">
                <div class="card-icon icon-teal">🚀</div>
                <div class="card-title">Projection Calculator</div>
                <div class="card-description">Analyse your growth in every FDPs and strategise accordingly.</div>
                <a href="https://shuhamgargprojectioncalculator.streamlit.app/" target="_blank" class="btn">Open Projection Calculator</a>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Render the complete HTML
components.html(html_code, height=2000, scrolling=True)
