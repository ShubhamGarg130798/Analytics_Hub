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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px 20px;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1600px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 50px;
        }
        
        .main-title {
            font-size: 4rem;
            font-weight: 800;
            color: white;
            margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .subtitle {
            font-size: 1.4rem;
            color: rgba(255, 255, 255, 0.95);
            font-weight: 300;
        }
        
        .content-wrapper {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
        }
        
        .section {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 24px;
            padding: 30px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .section-header {
            display: flex;
            align-items: center;
            gap: 15px;
            font-size: 2.2rem;
            font-weight: 800;
            color: white;
            margin-bottom: 30px;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
        }
        
        .section-icon {
            font-size: 2.5rem;
        }
        
        .cards-container {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        .card {
            background: linear-gradient(135deg, var(--card-color-1) 0%, var(--card-color-2) 100%);
            border-radius: 16px;
            padding: 25px 30px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            cursor: pointer;
            text-decoration: none;
            display: block;
        }
        
        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0) 100%);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .card:hover {
            transform: translateX(10px) scale(1.02);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
        }
        
        .card:hover::before {
            opacity: 1;
        }
        
        .card-content {
            display: flex;
            align-items: center;
            gap: 20px;
            position: relative;
            z-index: 1;
        }
        
        .card-icon-box {
            width: 70px;
            height: 70px;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            flex-shrink: 0;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }
        
        .card-info {
            flex-grow: 1;
        }
        
        .card-label {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.9);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 5px;
        }
        
        .card-title {
            font-size: 1.6rem;
            font-weight: 800;
            color: white;
            line-height: 1.2;
        }
        
        .coming-soon-badge {
            position: absolute;
            top: 15px;
            right: 15px;
            background: rgba(255, 255, 255, 0.95);
            color: #f59e0b;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
        }
        
        /* Color schemes */
        .card-blue {
            --card-color-1: #3b82f6;
            --card-color-2: #2563eb;
        }
        
        .card-teal {
            --card-color-1: #14b8a6;
            --card-color-2: #0d9488;
        }
        
        .card-red {
            --card-color-1: #ef4444;
            --card-color-2: #dc2626;
        }
        
        .card-orange {
            --card-color-1: #f97316;
            --card-color-2: #ea580c;
        }
        
        .card-purple {
            --card-color-1: #a855f7;
            --card-color-2: #9333ea;
        }
        
        .card-green {
            --card-color-1: #22c55e;
            --card-color-2: #16a34a;
        }
        
        .card-pink {
            --card-color-1: #ec4899;
            --card-color-2: #db2777;
        }
        
        .card-indigo {
            --card-color-1: #6366f1;
            --card-color-2: #4f46e5;
        }
        
        .card.disabled {
            opacity: 0.7;
            cursor: not-allowed;
        }
        
        .card.disabled:hover {
            transform: none;
        }
        
        @media (max-width: 1200px) {
            .content-wrapper {
                grid-template-columns: 1fr;
            }
        }
        
        @media (max-width: 768px) {
            .main-title {
                font-size: 2.5rem;
            }
            
            .card-title {
                font-size: 1.3rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="main-title">📊 Analytics Hub</h1>
            <p class="subtitle">Your Premium Gateway to Data Intelligence & Business Insights</p>
        </div>
        
        <div class="content-wrapper">
            <!-- Dashboards Section -->
            <div class="section">
                <div class="section-header">
                    <span class="section-icon">📊</span>
                    <span>Dashboards</span>
                </div>
                
                <div class="cards-container">
                    <a href="https://sgdashboards.streamlit.app/" target="_blank" class="card card-blue">
                        <div class="card-content">
                            <div class="card-icon-box">📈</div>
                            <div class="card-info">
                                <div class="card-label">Live Analytics</div>
                                <div class="card-title">Performance Dashboard</div>
                            </div>
                        </div>
                    </a>
                    
                    <div class="card card-teal">
                        <div class="card-content">
                            <div class="card-icon-box">💰</div>
                            <div class="card-info">
                                <div class="card-label">Expense Tracking</div>
                                <div class="card-title">Opex Management</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card card-red disabled">
                        <div class="coming-soon-badge">Coming Soon</div>
                        <div class="card-content">
                            <div class="card-icon-box">⚠️</div>
                            <div class="card-info">
                                <div class="card-label">Risk Assessment</div>
                                <div class="card-title">NPA Dashboard</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card card-orange disabled">
                        <div class="coming-soon-badge">Coming Soon</div>
                        <div class="card-content">
                            <div class="card-icon-box">🎯</div>
                            <div class="card-info">
                                <div class="card-label">Campaign Analytics</div>
                                <div class="card-title">Marketing Dashboard</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card card-purple disabled">
                        <div class="coming-soon-badge">Coming Soon</div>
                        <div class="card-content">
                            <div class="card-icon-box">💬</div>
                            <div class="card-info">
                                <div class="card-label">Support Insights</div>
                                <div class="card-title">Customer Complaints</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Calculators Section -->
            <div class="section">
                <div class="section-header">
                    <span class="section-icon">🧮</span>
                    <span>Calculators</span>
                </div>
                
                <div class="cards-container">
                    <a href="https://nbfclendingbusinesscalculatorfinal-2jeovxpeab8lxzqtflh3kp.streamlit.app/" target="_blank" class="card card-green">
                        <div class="card-content">
                            <div class="card-icon-box">📊</div>
                            <div class="card-info">
                                <div class="card-label">Growth Projection</div>
                                <div class="card-title">NBFC Calculator</div>
                            </div>
                        </div>
                    </a>
                    
                    <a href="https://subhamgargmarketinganalysis.streamlit.app/" target="_blank" class="card card-orange">
                        <div class="card-content">
                            <div class="card-icon-box">📣</div>
                            <div class="card-info">
                                <div class="card-label">Budget Planning</div>
                                <div class="card-title">Marketing ROI</div>
                            </div>
                        </div>
                    </a>
                    
                    <a href="https://sgssteamsize-eappd8e86tvycerctib4tsxgg.streamlit.app/" target="_blank" class="card card-purple">
                        <div class="card-content">
                            <div class="card-icon-box">👥</div>
                            <div class="card-info">
                                <div class="card-label">Team Planning</div>
                                <div class="card-title">Workforce Optimizer</div>
                            </div>
                        </div>
                    </a>
                    
                    <a href="https://incentivecalculatorpersonaltarget-4gepaam4wzwqohtor5m7kr.streamlit.app/" target="_blank" class="card card-indigo">
                        <div class="card-content">
                            <div class="card-icon-box">🎁</div>
                            <div class="card-info">
                                <div class="card-label">Rewards System</div>
                                <div class="card-title">Incentive Calculator</div>
                            </div>
                        </div>
                    </a>
                    
                    <a href="https://shuhamgargprojectioncalculator.streamlit.app/" target="_blank" class="card card-pink">
                        <div class="card-content">
                            <div class="card-icon-box">🚀</div>
                            <div class="card-info">
                                <div class="card-label">Strategic Planning</div>
                                <div class="card-title">Growth Projection</div>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Render the complete HTML
components.html(html_code, height=1400, scrolling=True)
