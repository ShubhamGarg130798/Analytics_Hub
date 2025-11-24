import React from 'react';
import { BarChart3, Calculator, TrendingUp, AlertCircle, Users, MessageSquare, DollarSign, Target, Clock } from 'lucide-react';

const DashboardHub = () => {
  const dashboards = [
    {
      title: "Performance Dashboard",
      description: "Shows the live performance of all our brands",
      url: "https://sgdashboards.streamlit.app/",
      icon: <BarChart3 className="w-8 h-8" />,
      color: "from-blue-500 to-blue-600"
    },
    {
      title: "Opex",
      description: "Track the expenses of your domain",
      url: "#",
      icon: <DollarSign className="w-8 h-8" />,
      color: "from-teal-500 to-teal-600"
    },
    {
      title: "NPA Dashboard",
      description: "Coming Soon",
      url: "#",
      icon: <AlertCircle className="w-8 h-8" />,
      color: "from-red-500 to-red-600",
      comingSoon: true
    },
    {
      title: "Marketing Dashboard",
      description: "Coming Soon",
      url: "#",
      icon: <Target className="w-8 h-8" />,
      color: "from-orange-500 to-orange-600",
      comingSoon: true
    },
    {
      title: "Customer Complaints Dashboard",
      description: "Coming Soon",
      url: "#",
      icon: <MessageSquare className="w-8 h-8" />,
      color: "from-purple-500 to-purple-600",
      comingSoon: true
    }
  ];

  const calculators = [
    {
      title: "NBFC Projection Calculator",
      description: "Visualize your STPL growth story in real time 📈",
      url: "https://nbfclendingbusinesscalculatorfinal-2jeovxpeab8lxzqtflh3kp.streamlit.app/",
      icon: <TrendingUp className="w-8 h-8" />,
      color: "from-green-500 to-green-600"
    },
    {
      title: "Marketing Expense Requirement Calculator",
      description: "Helps you to analyze the expense required for Marketing",
      url: "https://subhamgargmarketinganalysis.streamlit.app/",
      icon: <DollarSign className="w-8 h-8" />,
      color: "from-orange-500 to-orange-600"
    },
    {
      title: "Work Force Requirement",
      description: "Calculates the ideal team size based on workload, productivity, and target utilization.",
      url: "https://sgssteamsize-eappd8e86tvycerctib4tsxgg.streamlit.app/",
      icon: <Users className="w-8 h-8" />,
      color: "from-purple-500 to-purple-600"
    },
    {
      title: "Incentive Calculator NPA Team",
      description: "Know the incentives earned by team members",
      url: "https://incentivecalculatorpersonaltarget-4gepaam4wzwqohtor5m7kr.streamlit.app/",
      icon: <Calculator className="w-8 h-8" />,
      color: "from-blue-500 to-blue-600"
    },
    {
      title: "Projection Calculator",
      description: "Analyse your growth in every FDPs and strategise accordingly.",
      url: "https://shuhamgargprojectioncalculator.streamlit.app/",
      icon: <BarChart3 className="w-8 h-8" />,
      color: "from-teal-500 to-teal-600"
    }
  ];

  const Card = ({ item }) => {
    const handleClick = () => {
      if (!item.comingSoon && item.url !== "#") {
        window.open(item.url, '_blank');
      }
    };

    return (
      <div
        onClick={handleClick}
        className={`relative bg-white rounded-2xl shadow-lg p-6 transition-all duration-300 hover:shadow-2xl hover:-translate-y-2 ${
          item.comingSoon ? 'opacity-60 cursor-not-allowed' : 'cursor-pointer'
        }`}
      >
        {item.comingSoon && (
          <div className="absolute top-4 right-4 bg-yellow-400 text-yellow-900 text-xs font-bold px-3 py-1 rounded-full">
            Coming Soon
          </div>
        )}
        <div className={`inline-flex items-center justify-center w-16 h-16 rounded-xl bg-gradient-to-br ${item.color} text-white mb-4`}>
          {item.icon}
        </div>
        <h3 className="text-xl font-bold text-gray-800 mb-2">{item.title}</h3>
        <p className="text-gray-600 text-sm leading-relaxed">{item.description}</p>
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-gray-900 mb-4">
            Analytics Hub
          </h1>
          <p className="text-xl text-gray-600">
            Your central hub for dashboards and calculators
          </p>
        </div>

        {/* Dashboards Section */}
        <div className="mb-16">
          <div className="flex items-center mb-6">
            <BarChart3 className="w-8 h-8 text-blue-600 mr-3" />
            <h2 className="text-3xl font-bold text-gray-900">Dashboards</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {dashboards.map((dashboard, index) => (
              <Card key={index} item={dashboard} />
            ))}
          </div>
        </div>

        {/* Calculators Section */}
        <div>
          <div className="flex items-center mb-6">
            <Calculator className="w-8 h-8 text-green-600 mr-3" />
            <h2 className="text-3xl font-bold text-gray-900">Calculators</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {calculators.map((calculator, index) => (
              <Card key={index} item={calculator} />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashboardHub;
