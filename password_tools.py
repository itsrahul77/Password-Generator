
import string
import secrets
import json
import os
import math
import getpass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_FILE = os.path.join(BASE_DIR, "passwords.json")

def load_credentials():
    if not os.path.exists(STORAGE_FILE):
        return []
    try:
        with open(STORAGE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_credentials(data):
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def get_character_pool():
    pool=""
    if input("Include Uppercase (y/n): ").lower()=="y": pool+=string.ascii_uppercase
    if input("Include Lowercase (y/n): ").lower()=="y": pool+=string.ascii_lowercase
    if input("Include Numbers (y/n): ").lower()=="y": pool+=string.digits
    if input("Include Symbols (y/n): ").lower()=="y": pool+=string.punctuation
    return pool

def generate_password(length,pool):
    if not pool:
        return None
    return "".join(secrets.choice(pool) for _ in range(length))

def analyze_password():
    password=getpass.getpass("Enter password: ")
    if not password:
        print("Empty password.")
        return
    lower=sum(c.islower() for c in password)
    upper=sum(c.isupper() for c in password)
    digits=sum(c.isdigit() for c in password)
    symbols=sum(not c.isalnum() for c in password)

    score=0
    suggestions=[]

    if len(password)>=8: score+=20
    else: suggestions.append("Use at least 8 characters")
    if len(password)>=12: score+=20
    if lower: score+=15
    else: suggestions.append("Add lowercase letters")
    if upper: score+=15
    else: suggestions.append("Add uppercase letters")
    if digits: score+=15
    else: suggestions.append("Add numbers")
    if symbols: score+=15
    else: suggestions.append("Add symbols")

    pool=0
    if lower: pool+=26
    if upper: pool+=26
    if digits: pool+=10
    if symbols: pool+=32

    entropy=len(password)*math.log2(pool) if pool else 0

    if entropy<28: crack="Instant"
    elif entropy<36: crack="Minutes"
    elif entropy<60: crack="Hours / Days"
    elif entropy<80: crack="Years"
    else: crack="Millions of years"

    if score<40: level="Very Weak"
    elif score<60: level="Weak"
    elif score<80: level="Good"
    elif score<95: level="Strong"
    else: level="Very Strong"

    print("\n===== PASSWORD ANALYSIS =====")
    print(f"Score      : {score}/100")
    print(f"Strength   : {level}")
    print(f"Entropy    : {entropy:.2f} bits")
    print(f"Crack Time : {crack}")
    print(f"Length     : {len(password)}")
    print(f"Uppercase  : {upper}")
    print(f"Lowercase  : {lower}")
    print(f"Numbers    : {digits}")
    print(f"Symbols    : {symbols}")
    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print("-",s)

def add_credential():
    data=load_credentials()
    website=input("Website: ")
    username=input("Username: ")
    password=getpass.getpass("Password: ")
    data.append({"website":website,"username":username,"password":password})
    save_credentials(data)
    print("Saved.")

def search_credential():
    data=load_credentials()
    key=input("Search website or username: ").lower()
    found=False
    for item in data:
        if key in item["website"].lower() or key in item["username"].lower():
            print(item)
            found=True
    if not found:
        print("No record found.")

def view_all():
    data=load_credentials()
    if not data:
        print("No credentials.")
        return
    for i,item in enumerate(data,1):
        print(f"{i}. {item['website']} | {item['username']} | {item['password']}")

def delete_credential():
    data=load_credentials()
    site=input("Website to delete: ").lower()
    new=[d for d in data if d["website"].lower()!=site]
    save_credentials(new)
    print("Delete completed.")

def main():
    while True:
        print("\n=== BitXBytes Password Tools ===")
        print("1.Generate Password")
        print("2.Analyze Password")
        print("3.Save Credential")
        print("4.Search Credential")
        print("5.View All")
        print("6.Delete Credential")
        print("7.Exit")
        choice=input("Choice: ")

        match choice:
            case "1":
                try:
                    length=int(input("Length: "))
                except ValueError:
                    print("Invalid length.")
                    continue
                pool=get_character_pool()
                pwd=generate_password(length,pool)
                print("Generated:", pwd if pwd else "No character set selected.")
            case "2":
                analyze_password()
            case "3":
                add_credential()
            case "4":
                search_credential()
            case "5":
                view_all()
            case "6":
                delete_credential()
            case "7":
                break
            case _:
                print("Invalid choice.")

if __name__=="__main__":
    main()
