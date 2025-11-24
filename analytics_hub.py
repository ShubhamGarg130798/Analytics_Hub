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
            background-color: #ffffff;
            padding: 50px 30px;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1600px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 60px;
        }
        
        .header-icon {
            width: 80px;
            height: 80px;
            margin: 0 auto 20px;
        }
        
        .main-title {
            font-size: 3.5rem;
            font-weight: 800;
            color: #1d1d1f;
            margin-bottom: 15px;
            letter-spacing: -1px;
        }
        
        .subtitle {
            font-size: 1.3rem;
            color: #6e6e73;
            font-weight: 400;
        }
        
        .content-wrapper {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 50px;
        }
        
        .section-header {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 2rem;
            font-weight: 700;
            color: #1d1d1f;
            margin-bottom: 25px;
        }
        
        .section-icon {
            width: 35px;
            height: 35px;
        }
        
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }
        
        .card {
            background: #f8f9fa;
            border-radius: 18px;
            padding: 30px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
            transition: all 0.3s ease;
            position: relative;
            cursor: pointer;
            text-decoration: none;
            display: block;
            height: 220px;
            display: flex;
            flex-direction: column;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.12);
        }
        
        .card-icon-box {
            width: 70px;
            height: 70px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            margin-bottom: 18px;
            color: white;
            flex-shrink: 0;
        }
        
        /* Icon colors matching the images */
        .icon-blue {
            background: linear-gradient(135deg, #4285f4 0%, #2962ff 100%);
        }
        
        .icon-teal {
            background: linear-gradient(135deg, #14b8a6 0%, #0d9488 100%);
        }
        
        .icon-red {
            background: linear-gradient(135deg, #f8958d 0%, #f06b63 100%);
        }
        
        .icon-orange {
            background: linear-gradient(135deg, #ff9966 0%, #ff6b35 100%);
        }
        
        .icon-purple {
            background: linear-gradient(135deg, #b794f6 0%, #9333ea 100%);
        }
        
        .icon-green {
            background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
        }
        
        .icon-pink {
            background: linear-gradient(135deg, #f59e8f 0%, #ff8a80 100%);
        }
        
        .card-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: #1d1d1f;
            margin-bottom: 10px;
            line-height: 1.3;
        }
        
        .card-description {
            font-size: 0.9rem;
            color: #86868b;
            line-height: 1.5;
            flex-grow: 1;
        }
        
        .coming-soon-badge {
            position: absolute;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, #ffc658 0%, #ff9a23 100%);
            color: white;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            box-shadow: 0 2px 8px rgba(255, 154, 35, 0.3);
        }
        
        .card.disabled {
            opacity: 0.65;
            cursor: not-allowed;
        }
        
        .card.disabled:hover {
            transform: none;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        }
        
        .card.disabled .card-title {
            color: #86868b;
        }
        
        @media (max-width: 1400px) {
            .cards-grid {
                grid-template-columns: 1fr;
            }
        }
        
        @media (max-width: 1000px) {
            .content-wrapper {
                grid-template-columns: 1fr;
            }
        }
        
        @media (max-width: 768px) {
            .main-title {
                font-size: 2.5rem;
            }
            
            body {
                padding: 30px 20px;
            }
            
            .card {
                height: auto;
                min-height: 200px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <svg class="header-icon" viewBox="0 0 100 100" fill="none">
                <rect x="10" y="55" width="20" height="35" rx="3" fill="#22c55e"/>
                <rect x="35" y="40" width="20" height="50" rx="3" fill="#ef4444"/>
                <rect x="60" y="20" width="20" height="70" rx="3" fill="#3b82f6"/>
                <rect x="0" y="0" width="100" height="15" rx="2" fill="#e5e7eb"/>
                <line x1="0" y1="15" x2="100" y2="15" stroke="#d1d5db" stroke-width="1"/>
                <line x1="0" y1="90" x2="100" y2="90" stroke="#d1d5db" stroke-width="2"/>
            </svg>
            <h1 class="main-title">Analytics Hub</h1>
            <p class="subtitle">Your central hub for dashboards and calculators</p>
        </div>
        
        <div class="content-wrapper">
            <!-- Dashboards Section -->
            <div class="section">
                <div class="section-header">
                    <svg class="section-icon" viewBox="0 0 24 24" fill="none">
                        <rect x="3" y="3" width="7" height="7" rx="1" fill="#3b82f6"/>
                        <rect x="3" y="14" width="7" height="7" rx="1" fill="#ef4444"/>
                        <rect x="14" y="3" width="7" height="18" rx="1" fill="#22c55e"/>
                    </svg>
                    <span>Dashboards</span>
                </div>
                
                <div class="cards-grid">
                    <a href="https://sgdashboards.streamlit.app/" target="_blank" class="card">
                        <div class="card-icon-box icon-blue">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
                            </svg>
                        </div>
                        <div class="card-title">Performance Dashboard</div>
                        <div class="card-description">Shows the live performance of all our brands</div>
                    </a>
                    
                    <div class="card">
                        <div class="card-icon-box icon-teal">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <line x1="12" y1="1" x2="12" y2="23"></line>
                                <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                            </svg>
                        </div>
                        <div class="card-title">Opex</div>
                        <div class="card-description">Track the expenses of your domain</div>
                    </div>
                    
                    <div class="card disabled">
                        <div class="coming-soon-badge">Coming Soon</div>
                        <div class="card-icon-box icon-red">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <circle cx="12" cy="12" r="10"></circle>
                                <line x1="12" y1="8" x2="12" y2="12"></line>
                                <line x1="12" y1="16" x2="12.01" y2="16"></line>
                            </svg>
                        </div>
                        <div class="card-title">NPA Dashboard</div>
                        <div class="card-description">Coming Soon</div>
                    </div>
                    
                    <div class="card disabled">
                        <div class="coming-soon-badge">Coming Soon</div>
                        <div class="card-icon-box icon-pink">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <circle cx="12" cy="12" r="10"></circle>
                                <circle cx="12" cy="12" r="6"></circle>
                                <circle cx="12" cy="12" r="2"></circle>
                            </svg>
                        </div>
                        <div class="card-title">Marketing Dashboard</div>
                        <div class="card-description">Coming Soon</div>
                    </div>
                    
                    <div class="card disabled">
                        <div class="coming-soon-badge">Coming Soon</div>
                        <div class="card-icon-box icon-purple">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                            </svg>
                        </div>
                        <div class="card-title">Customer Complaints Dashboard</div>
                        <div class="card-description">Coming Soon</div>
                    </div>
                </div>
            </div>
            
            <!-- Calculators Section -->
            <div class="section">
                <div class="section-header">
                    <svg class="section-icon" viewBox="0 0 24 24" fill="none">
                        <rect x="4" y="2" width="16" height="20" rx="2" fill="#ff6b35"/>
                        <line x1="8" y1="7" x2="16" y2="7" stroke="white" stroke-width="1.5"/>
                        <line x1="8" y1="11" x2="16" y2="11" stroke="white" stroke-width="1.5"/>
                        <circle cx="9" cy="15" r="1" fill="white"/>
                        <circle cx="12" cy="15" r="1" fill="white"/>
                        <circle cx="15" cy="15" r="1" fill="white"/>
                        <circle cx="9" cy="18" r="1" fill="white"/>
                        <circle cx="12" cy="18" r="1" fill="white"/>
                        <circle cx="15" cy="18" r="1" fill="white"/>
                    </svg>
                    <span>Calculators</span>
                </div>
                
                <div class="cards-grid">
                    <a href="https://nbfclendingbusinesscalculatorfinal-2jeovxpeab8lxzqtflh3kp.streamlit.app/" target="_blank" class="card">
                        <div class="card-icon-box icon-green">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <line x1="12" y1="5" x2="12" y2="19"></line>
                                <polyline points="5 12 12 19 19 12"></polyline>
                            </svg>
                        </div>
                        <div class="card-title">NBFC Projection Calculator</div>
                        <div class="card-description">Visualize your STPL growth story in real time 📈</div>
                    </a>
                    
                    <a href="https://subhamgargmarketinganalysis.streamlit.app/" target="_blank" class="card">
                        <div class="card-icon-box icon-orange">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <line x1="12" y1="1" x2="12" y2="23"></line>
                                <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                            </svg>
                        </div>
                        <div class="card-title">Marketing Expense Requirement Calculator</div>
                        <div class="card-description">Helps you to analyze the expense required for Marketing</div>
                    </a>
                    
                    <a href="https://sgssteamsize-eappd8e86tvycerctib4tsxgg.streamlit.app/" target="_blank" class="card">
                        <div class="card-icon-box icon-purple">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                                <circle cx="9" cy="7" r="4"></circle>
                                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                            </svg>
                        </div>
                        <div class="card-title">Work Force Requirement</div>
                        <div class="card-description">Calculates the ideal team size based on workload, productivity, and target utilization.</div>
                    </a>
                    
                    <a href="https://incentivecalculatorpersonaltarget-4gepaam4wzwqohtor5m7kr.streamlit.app/" target="_blank" class="card">
                        <div class="card-icon-box icon-blue">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <rect x="3" y="3" width="7" height="7"></rect>
                                <rect x="14" y="3" width="7" height="7"></rect>
                                <rect x="14" y="14" width="7" height="7"></rect>
                                <rect x="3" y="14" width="7" height="7"></rect>
                            </svg>
                        </div>
                        <div class="card-title">Incentive Calculator NPA Team</div>
                        <div class="card-description">Know the incentives earned by team members</div>
                    </a>
                    
                    <a href="https://shuhamgargprojectioncalculator.streamlit.app/" target="_blank" class="card">
                        <div class="card-icon-box icon-teal">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <circle cx="12" cy="12" r="10"></circle>
                                <polyline points="12 6 12 12 16 14"></polyline>
                            </svg>
                        </div>
                        <div class="card-title">Projection Calculator</div>
                        <div class="card-description">Analyse your growth in every FDPs and strategise accordingly.</div>
                    </a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Render the complete HTML
components.html(html_code, height=1600, scrolling=True)
