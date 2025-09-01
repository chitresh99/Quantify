"use client"

import React from 'react';

interface NavbarProps {
  className?: string;
}

const Navbar: React.FC<NavbarProps> = ({ className = "" }) => {
  return (
    <nav className={`sticky top-0 z-50 bg-white/10 backdrop-blur-sm border-b border-orange-500/30 ${className}`}>
      <div className="mx-auto max-w-7xl px-6 py-4">
        <span className="text-2xl font-extrabold tracking-tight bg-gradient-to-r from-orange-200 to-white bg-clip-text text-transparent">
          Quantify
        </span>
      </div>
    </nav>
  );
};

export default Navbar;
