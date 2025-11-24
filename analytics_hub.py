import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="Analytics Hub", page_icon="📊", layout="wide")

# Enhanced HTML/CSS/JS solution
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
            background: #ffffff;
            padding: 20px 30px;
            min-height: 100vh;
            position: relative;
            overflow-x: hidden;
        }
        
        /* Floating particles effect */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(circle at 20% 80%, rgba(59, 130, 246, 0.05) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(239, 68, 68, 0.05) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(34, 197, 94, 0.05) 0%, transparent 50%);
            pointer-events: none;
            animation: float 20s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translate(0, 0); }
            33% { transform: translate(30px, -30px); }
            66% { transform: translate(-20px, 20px); }
        }
        
        .container {
            max-width: 1600px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }
        
        .header {
            text-align: center;
            margin-bottom: 35px;
            animation: fadeInDown 0.8s ease-out;
        }
        
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .header-title-wrapper {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin-bottom: 15px;
        }
        
        .header-icon {
            width: 70px;
            height: 70px;
            filter: drop-shadow(0 10px 25px rgba(59, 130, 246, 0.3));
            animation: pulse 3s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        .main-title {
            font-size: 3.5rem;
            font-weight: 800;
            color: #1d1d1f;
            letter-spacing: -1px;
            margin: 0;
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
        
        .section {
            animation: fadeInUp 0.8s ease-out;
            animation-fill-mode: both;
        }
        
        .section:nth-child(1) { animation-delay: 0.2s; }
        .section:nth-child(2) { animation-delay: 0.4s; }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
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
            animation: rotate 10s linear infinite;
        }
        
        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }
        
        .card {
            backdrop-filter: blur(10px);
            border-radius: 18px;
            padding: 30px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            cursor: pointer;
            text-decoration: none;
            display: block;
            height: 220px;
            display: flex;
            flex-direction: column;
            border: 1px solid rgba(255, 255, 255, 0.2);
            overflow: hidden;
        }
        
        /* Card background colors - more vibrant */
        .card-bg-blue {
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        }
        
        .card-bg-teal {
            background: linear-gradient(135deg, #14b8a6 0%, #0d9488 100%);
        }
        
        .card-bg-red {
            background: linear-gradient(135deg, #fca5a5 0%, #f87171 100%);
        }
        
        .card-bg-pink {
            background: linear-gradient(135deg, #f9a8d4 0%, #f472b6 100%);
        }
        
        .card-bg-purple {
            background: linear-gradient(135deg, #a78bfa 0%, #8b5cf6 100%);
        }
        
        .card-bg-green {
            background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%);
        }
        
        .card-bg-orange {
            background: linear-gradient(135deg, #fb923c 0%, #f97316 100%);
        }
        
        .card-bg-yellow {
            background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        }
        
        .card-bg-indigo {
            background: linear-gradient(135deg, #818cf8 0%, #6366f1 100%);
        }
        
        .card-bg-cyan {
            background: linear-gradient(135deg, #22d3ee 0%, #06b6d4 100%);
        }
        
        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
        }
        
        .card:hover::before {
            opacity: 1;
        }
        
        .card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25);
            border-color: rgba(255, 255, 255, 0.4);
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
            position: relative;
            z-index: 1;
            transition: transform 0.4s ease;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }
        
        .card:hover .card-icon-box {
            transform: scale(1.1) rotate(5deg);
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
        }
        
        /* Icon colors with enhanced gradients */
        .icon-blue {
            background: linear-gradient(135deg, #4285f4 0%, #2962ff 100%);
            box-shadow: 0 8px 20px rgba(66, 133, 244, 0.3);
        }
        
        .icon-teal {
            background: linear-gradient(135deg, #14b8a6 0%, #0d9488 100%);
            box-shadow: 0 8px 20px rgba(20, 184, 166, 0.3);
        }
        
        .icon-red {
            background: linear-gradient(135deg, #f8958d 0%, #f06b63 100%);
            box-shadow: 0 8px 20px rgba(248, 149, 141, 0.3);
        }
        
        .icon-orange {
            background: linear-gradient(135deg, #ff9966 0%, #ff6b35 100%);
            box-shadow: 0 8px 20px rgba(255, 107, 53, 0.3);
        }
        
        .icon-purple {
            background: linear-gradient(135deg, #b794f6 0%, #9333ea 100%);
            box-shadow: 0 8px 20px rgba(147, 51, 234, 0.3);
        }
        
        .icon-green {
            background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
            box-shadow: 0 8px 20px rgba(76, 175, 80, 0.3);
        }
        
        .icon-pink {
            background: linear-gradient(135deg, #f59e8f 0%, #ff8a80 100%);
            box-shadow: 0 8px 20px rgba(255, 138, 128, 0.3);
        }
        
        .card-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 10px;
            line-height: 1.3;
            position: relative;
            z-index: 1;
            transition: color 0.3s ease;
        }
        
        .card:hover .card-title {
            color: #ffffff;
        }
        
        .card-description {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.9);
            line-height: 1.5;
            flex-grow: 1;
            position: relative;
            z-index: 1;
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
            box-shadow: 0 4px 12px rgba(255, 154, 35, 0.4);
            z-index: 2;
            animation: bounce 2s ease-in-out infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
        }
        
        .card.disabled {
            opacity: 0.65;
            cursor: not-allowed;
        }
        
        .card.disabled:hover {
            transform: none;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
            border-color: rgba(255, 255, 255, 0.2);
        }
        
        .card.disabled:hover .card-icon-box {
            transform: none;
        }
        
        .card.disabled .card-title {
            color: rgba(255, 255, 255, 0.7);
        }
        
        .card.disabled:hover .card-title {
            color: rgba(255, 255, 255, 0.7);
        }
        
        /* Shimmer effect for active cards */
        .card:not(.disabled)::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(
                45deg,
                transparent,
                rgba(255, 255, 255, 0.1),
                transparent
            );
            transform: rotate(45deg);
            transition: all 0.6s ease;
            opacity: 0;
        }
        
        .card:not(.disabled):hover::after {
            opacity: 1;
            left: 100%;
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
            <div class="header-title-wrapper">
                <svg class="header-icon" viewBox="0 0 100 100" fill="none">
                    <rect x="10" y="55" width="20" height="35" rx="3" fill="#22c55e"/>
                    <rect x="35" y="40" width="20" height="50" rx="3" fill="#ef4444"/>
                    <rect x="60" y="20" width="20" height="70" rx="3" fill="#3b82f6"/>
                    <rect x="0" y="0" width="100" height="15" rx="2" fill="#e5e7eb"/>
                    <line x1="0" y1="15" x2="100" y2="15" stroke="#d1d5db" stroke-width="1"/>
                    <line x1="0" y1="90" x2="100" y2="90" stroke="#d1d5db" stroke-width="2"/>
                </svg>
                <h1 class="main-title">Analytics Hub</h1>
            </div>
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
                    <a href="https://sgdashboards.streamlit.app/" target="_blank" class="card card-bg-blue">
                        <div class="card-icon-box icon-blue">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
                            </svg>
                        </div>
                        <div class="card-title">Performance Dashboard</div>
                        <div class="card-description">Shows the live performance of all our brands</div>
                    </a>
                    
                    <div class="card card-bg-teal">
                        <div class="card-icon-box icon-teal">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <line x1="12" y1="1" x2="12" y2="23"></line>
                                <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                            </svg>
                        </div>
                        <div class="card-title">Opex</div>
                        <div class="card-description">Track the expenses of your domain</div>
                    </div>
                    
                    <div class="card card-bg-red disabled">
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
                    
                    <div class="card card-bg-pink disabled">
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
                    
                    <div class="card card-bg-purple disabled">
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
                    <a href="https://nbfclendingbusinesscalculatorfinal-2jeovxpeab8lxzqtflh3kp.streamlit.app/" target="_blank" class="card card-bg-green">
                        <div class="card-icon-box icon-green">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <line x1="12" y1="5" x2="12" y2="19"></line>
                                <polyline points="5 12 12 19 19 12"></polyline>
                            </svg>
                        </div>
                        <div class="card-title">NBFC Projection Calculator</div>
                        <div class="card-description">Visualize your STPL growth story in real time 📈</div>
                    </a>
                    
                    <a href="https://subhamgargmarketinganalysis.streamlit.app/" target="_blank" class="card card-bg-orange">
                        <div class="card-icon-box icon-orange">
                            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <line x1="12" y1="1" x2="12" y2="23"></line>
                                <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                            </svg>
                        </div>
                        <div class="card-title">Marketing Expense Requirement Calculator</div>
                        <div class="card-description">Helps you to analyze the expense required for Marketing</div>
                    </a>
                    
                    <a href="https://sgssteamsize-eappd8e86tvycerctib4tsxgg.streamlit.app/" target="_blank" class="card card-bg-indigo">
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
                    
                    <a href="https://incentivecalculatorpersonaltarget-4gepaam4wzwqohtor5m7kr.streamlit.app/" target="_blank" class="card card-bg-yellow">
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
                    
                    <a href="https://shuhamgargprojectioncalculator.streamlit.app/" target="_blank" class="card card-bg-cyan">
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
components.html(html_code, height=1500, scrolling=True)
