"""
Security Automation & API Integration Tool
Main entry point with CLI interface
"""

import sys
import argparse
from typing import Optional
from dotenv import load_dotenv
import os

# Import modules (we'll create these next)
from api_handler import ThreatIntelligenceAPI
from report_generator import ReportGenerator
from utils.logger import setup_logger
from utils.validators import validate_ip, validate_domain, validate_hash

# Load environment variables
load_dotenv()

# Setup logger
logger = setup_logger()


def print_banner():
    """ Displaying tool banner"""
    banner = """
    ╔═══════════════════════════════════════════════╗
    ║   Security Automation & API Integration Tool  ║
    ║              VirusTotal Integration           ║
    ╚═══════════════════════════════════════════════╝
    """
    print(banner)


def interactive_mode():
    """Opening Interactive mode """
    print_banner()

    api_key = os.getenv('VIRUSTOTAL_API_KEY')
    if not api_key:
        logger.error("API key was not found in the .env file")
        print(" Error: VIRUSTOTAL_API_KEY not found in .env file")
        sys.exit(1)

    api =  ThreatIntelligenceAPI(api_key)
    report_gen = ReportGenerator()

def scan_ip_address(ip):
    print(f"\nScanning IP address: {ip}")
    print("Scan complete (placeholder result)")
# creating functions that would scan the users input and print a result

def scan_domain(domain):
    print(f"\nScanning Domain: {domain}")
    print("Scan Complete (placeholder result)")

def scan_file_hash(file_hash):
    print(f"\nScanning File Hash: {file_hash}")
    print("Scan Complete (placeholder result)")

def scan_recent_reports(time_range):
    print(f"\nScan Recent Reports: {time_range}")
    print("Scan Complete (placeholder result)")

def security_weakpoints(weakpoints):
     print(f"\nScanning for Security Weakpoints: {weakpoints}")
     print("Scan Complete (placeholder result)")

while True:
    print("MAIN INTERACTIVE MENU")
    print("1. Scan For IP Address")
    print("2. Scan For Domain")
    print("3. Scan For File Hash")
    print("4. Check Recent Reports")
    print("5. Scan For Security Weakpoints")
    print("6. Exit") 

    choice = input("\n Select option 1-6").strip()

    if choice == "1":
            ip = input("Enter IP address To Scan: ").strip()
            scan_ip_address(ip)

    elif choice == "2":
            domain = input("Enter Domain To Scan").strip()
            scan_domain(domain)

    elif choice == "3":
            file_hash = input("Enter File Hash To Scan").strip()
            scan_file_hash(file_hash)

    elif choice == "4":
            time_range = input("Enter time range (e.g 24 hours 9 days)").strip()
            scan_recent_reports(time_range)

    elif choice == "5":
         print("\nScanning for security weakpoints (placeholder result)")
         print(" No weakpoints detected")
    
    elif choice == "6":
         print("\nExit")
         break 
    
    else:
         print("Invalid input. Select between 1 - 6")


def is_valid_ip(ip):
     parts = ip.split(".")

     if len(parts) != 4:
          return False
     
     for part in parts:
          if not part.isdigit():
               return False
          
          number = int(part)
          if number not in range (0, 256):
               return False
          
     return True
          
class APIhandler:
 def check_ip(ip, api_handler):
      if not is_valid_ip(ip):
           print("Invalid IP")
           return
     
      print(f"Checking IP address: {ip}")


def fetch_data()
