"use client";

import React from "react";
import { Sparkles, ArrowRight, ChevronRight, CheckCircle } from "lucide-react";

interface StatCardProps {
  label: string;
  value: string;
  trend: string;
}

const StatCard: React.FC<StatCardProps> = ({ label, value, trend }) => (
  <div className="text-center">
    <div className="text-2xl sm:text-3xl font-extrabold text-white mb-1">
      {value}
    </div>
    <div className="text-sm text-orange-200">{label}</div>
    <div className="text-xs text-green-400 mt-1">{trend}</div>
  </div>
);

const Hero: React.FC = () => {
  const stats: StatCardProps[] = [
    { label: "Markets Analyzed", value: "15,000+", trend: "+12%" },
    { label: "Data Points/Day", value: "2.5M", trend: "+8%" },
    { label: "Accuracy Rate", value: "94.7%", trend: "+3%" },
    { label: "Response Time", value: "<100ms", trend: "-15%" },
  ];

  const benefits = [
    "100% free forever",
    "Unlimited access to all features",
    "No hidden fees or paywalls",
  ];

  return (
    <section className="relative px-6 pt-20 lg:pt-32 pb-0">
      <div className="mx-auto max-w-7xl">
        <div className="text-center">
          <div className="flex justify-center mb-6">
            <div className="inline-flex items-center gap-2 px-4 py-2 bg-white/10 backdrop-blur-sm border border-orange-400/30 rounded-full">
              <Sparkles className="w-4 h-4 text-orange-300" />
              <span className="text-sm font-semibold text-orange-100">
                AI-Powered Financial Intelligence
              </span>
            </div>
          </div>

          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight mb-6">
            <span className="bg-gradient-to-r from-white via-orange-100 to-orange-200 bg-clip-text text-transparent">
              Transform Your Financial Research
            </span>
            <br />
            <span className="bg-gradient-to-r from-orange-200 to-white bg-clip-text text-transparent">
              with Intelligent AI Agents
            </span>
          </h1>

          <p className="mx-auto max-w-2xl text-lg sm:text-xl text-orange-100 mb-10 leading-relaxed">
            Deploy sophisticated AI agents that analyze markets , process vast
            amounts of financial data, and deliver actionable insights in real
            time. Make smarter investment decisions with the power of artificial
            intelligence.
          </p>

          <div className="flex flex-col items-center justify-center gap-4 sm:flex-row">
            <button className="group px-8 py-4 bg-white text-orange-800 font-bold rounded-lg hover:bg-orange-100 transition-all duration-300 hover:shadow-2xl hover:scale-105 flex items-center gap-2">
              Get Started
              <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </button>
          </div>

          <div className="mt-12 flex flex-wrap justify-center gap-8 text-sm text-orange-200">
            {benefits.map((benefit) => (
              <div key={benefit} className="flex items-center gap-2">
                <CheckCircle className="w-5 h-5 text-orange-300" />
                <span>{benefit}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
