"use client"

import React from 'react';
import AnimatedBackground from './AnimatedBackground';

const LandingPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-orange-900 via-orange-800 to-orange-600 text-white overflow-hidden">
      <AnimatedBackground />
    </div>
  );
};

export default LandingPage;
