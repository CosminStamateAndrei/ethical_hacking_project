import json
import subprocess
import time

from banner import GREEN, RESET, colored_banner

# From subdomains.json we enumerate whats in hosts only 
def list_subdomains():
    try: 
        subprocess.run(["bash", "get_subdomains.sh"], check=True)
    except FileNotFoundError:
        print("bash or get_subdomains.sh not found.")
        raise SystemExit(1)
    except subprocess.CalledProcessError as e:
        print(f"get_subdomains.sh failed (exit code {e.returncode}).")
        raise SystemExit(1)

def see_open_ports():
    print("To be implemented...")
    time.sleep(3)

def subdomain_choice():
    choice = input("Do you want to write subdomains to hosts.txt? (y/n): ")
    if choice.lower() == 'y':
        with open("sensitive_data/subdomains.json", "r") as f:
            data = json.load(f)
            with open("sensitive_data/hosts.txt", "w") as hosts_file:
                for host in data["hosts"]:
                    hosts_file.write(host + "\n")
        print("Subdomains written to hosts.txt.")
    else:
        print("Subdomains not written to hosts.txt.")
    time.sleep(3)

def starting_page():
    print(colored_banner())
    print()
    print(GREEN, end="")
    print("Hacking Project - Ethical Hacking MSc")
    print("1. List subdomains")
    print("2. See open ports")
    print("3. Exit")


# Main file to run the script
def main():
    while True:
        starting_page()
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            list_subdomains()
            subdomain_choice()
        elif choice == '2':
            see_open_ports()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1.2)
        # Clear the console
        print("\033c", end="")


if __name__ == "__main__":
    try:
        main()
    finally:
        print(RESET, end="")
