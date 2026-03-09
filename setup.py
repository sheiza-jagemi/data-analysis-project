#!/usr/bin/env python3
"""
Quick setup script for Netflix Analysis Project
Run this to generate data and verify environment
"""

import sys
import subprocess

def check_dependencies():
    """Check if required packages are installed"""
    required = ['pandas', 'numpy', 'matplotlib', 'seaborn', 'jupyter']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"✓ {package} installed")
        except ImportError:
            missing.append(package)
            print(f"✗ {package} missing")
    
    if missing:
        print(f"\nInstall missing packages: pip install {' '.join(missing)}")
        return False
    return True

def generate_data():
    """Generate the Netflix dataset"""
    print("\nGenerating Netflix dataset...")
    try:
        subprocess.run([sys.executable, 'src/generate_dataset.py'], check=True)
        print("✓ Dataset generated successfully")
        return True
    except subprocess.CalledProcessError:
        print("✗ Failed to generate dataset")
        return False

def main():
    print("=" * 60)
    print("Netflix Analysis Project - Setup")
    print("=" * 60)
    
    print("\n1. Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    
    print("\n2. Generating dataset...")
    if not generate_data():
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("Setup complete! Run: jupyter notebook notebooks/netflix_analysis.ipynb")
    print("=" * 60)

if __name__ == "__main__":
    main()
