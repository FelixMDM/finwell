import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: 'export',
  webpack: (config) => {
    config.optimization.minimize = false;
    return config;
  }
};

export default nextConfig;
