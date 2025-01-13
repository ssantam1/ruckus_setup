import subprocess
import sys
import main

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Successfully installed requirements")
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        sys.exit(1)

def run_main():
    main.main()

if __name__ == "__main__":
    install_requirements()
    run_main()