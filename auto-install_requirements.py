import importlib
import sys
import subprocess

# List of required modules
REQUIRED_MODULES = ["scapy.all", "matplotlib", "tabulate", "colorama"]

def check_requirements():
    missing = []
    for module in REQUIRED_MODULES:
        try:
            importlib.import_module(module)
        except ImportError:
            missing.append(module.split(".")[0])  # only show main package name
    
    if missing:
        print("\n[!] Missing dependencies detected:")
        for m in missing:
            print(f"   - {m}")
        
        # Ask user if they want auto-install
        choice = input("\nDo you want to auto-install them now? (y/n): ").strip().lower()
        
        if choice == "y":
            for m in missing:
                print(f"\n[*] Installing {m} ...")
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", m])
                except Exception as e:
                    print(f"[!] Failed to install {m}: {e}")
            print("\n✅ All missing modules installed. Please re-run the script.")
        else:
            print("\n⚠️  Please install manually by running:")
            print("   pip install -r requirements.txt")
        
        sys.exit(0)  # exit gracefully after handling

# Run check before anything else
check_requirements()
