"use client"

import React from 'react';

const Footer: React.FC = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-black/20 backdrop-blur-sm border-t border-orange-500/30">
      <div className="mx-auto max-w-7xl px-6 py-12 text-center">
        {/* Brand */}
        <div className="flex items-center justify-center gap-2 mb-4">
          <span className="text-2xl font-extrabold tracking-tight bg-gradient-to-r from-orange-200 to-white bg-clip-text text-transparent">
            Quantify
          </span>
        </div>
        <p className="text-orange-100 text-sm mb-6 leading-relaxed max-w-xl mx-auto">
          AI-powered financial research platform revolutionizing how investors analyze markets.
        </p>
        <div className="text-orange-100 text-xs">
          © {currentYear} Quantify. All rights reserved.
        </div>
      </div>
    </footer>
  );
};

export default Footer;
