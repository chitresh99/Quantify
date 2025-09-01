"use client";

import React from "react";
import {
  Globe,
  TrendingUp,
  BarChart3,
  Building2,
  ArrowRight,
} from "lucide-react";

interface Feature {
  icon: React.ReactNode;
  title: string;
  description: string;
  capabilities: string[];
}

interface FeatureCardProps {
  feature: Feature;
  index: number;
}

const FeatureCard: React.FC<FeatureCardProps> = ({ feature }) => {
  return (
    <div className="group relative bg-white/10 backdrop-blur-sm border border-orange-400/30 rounded-2xl p-8 hover:bg-white/15 transition-all duration-300 hover:shadow-2xl hover:scale-[1.02] cursor-pointer">
      <div className="absolute inset-0 bg-gradient-to-br from-orange-400/10 to-orange-600/10 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>

      <div className="relative">
        <div className="flex items-start gap-4 mb-4">
          <div className="p-3 bg-orange-500/20 rounded-lg group-hover:bg-orange-500/30 transition-colors duration-300">
            {feature.icon}
          </div>
          <div className="flex-1">
            <h3 className="text-xl font-bold mb-2 text-white group-hover:text-orange-100 transition-colors">
              {feature.title}
            </h3>
            <p className="text-orange-100 mb-4 leading-relaxed">
              {feature.description}
            </p>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-3">
          {feature.capabilities.map((capability, i) => (
            <div key={i} className="flex items-center gap-2">
              <div className="w-1.5 h-1.5 bg-orange-300 rounded-full"></div>
              <span className="text-sm text-orange-200">{capability}</span>
            </div>
          ))}
        </div>

        <div className="mt-6 flex items-center gap-2 text-orange-300 group-hover:text-white transition-colors">
          <span className="text-sm font-semibold">Learn more</span>
          <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
        </div>
      </div>
    </div>
  );
};

const Features: React.FC = () => {
  const features: Feature[] = [
    {
      icon: <Globe className="w-8 h-8 text-orange-300" />,
      title: "News & Sentiment Analysis",
      description: "Market News and Sentiment summary with our AI Agent",
      capabilities: [
        "Real-time Financial News",
        "AI Sentiment Analysis",
        "Ticker-specific Insights",
        "Investment Implications",
      ],
    },
    {
      icon: <TrendingUp className="w-8 h-8 text-orange-300" />,
      title: "Macroeconomic Data Analysis",
      description:
        "Comprehensive economic indicators, central bank policies, and global market trends analyzed with predictive modeling",
      capabilities: [
        "Economic Indicator Analysis",
        "Federal Reserve Policy Insights",
        "Cross-Asset Impact Modeling",
        "Investment Theme Generation",
      ],
    },
    {
      icon: <BarChart3 className="w-8 h-8 text-orange-300" />,
      title: "Multi-Asset Market Analysis",
      description:
        "Comprehensive AI-powered analysis for stocks, cryptocurrencies, futures, and forex",
      capabilities: ["Coming soon"],
    },
    {
      icon: <Building2 className="w-8 h-8 text-orange-300" />,
      title: "Company Fundamentals",
      description:
        "Comprehensive evaluation of financial statements, earnings reports, and corporate disclosures",
      capabilities: ["Coming Soon"],
    },
  ];

  return (
    <section id="features" className="px-6 py-20 lg:py-32">
      <div className="mx-auto max-w-7xl">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight mb-4">
            <span className="bg-gradient-to-r from-white to-orange-200 bg-clip-text text-transparent">
              Intelligent AI Agents at Your Service
            </span>
          </h2>
          <p className="mx-auto max-w-2xl text-lg text-orange-100">
            Each specialized agent works autonomously to deliver comprehensive
            financial intelligence
          </p>
        </div>

        <div className="grid gap-8 md:grid-cols-2">
          {features.map((feature, index) => (
            <FeatureCard key={index} feature={feature} index={index} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;
