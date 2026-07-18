from dashboard import display_dashboard
import password_tools


def main():
    display_dashboard()

    while True:
        print("\n[1] Password Generator")
        print("[2] Analyze Password Strength")
        print("[3] Save Credentials")
        print("[4] Search Credentials")
        print("[5] View All Credentials")
        print("[6] Delete Credentials")
        print("[7] Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            try:
                length = int(input("Enter password length: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            pool = password_tools.get_character_pool()
            password = password_tools.generate_password(length, pool)
            if password:
                print("Generated password:", password)
            else:
                print("No character set selected.")
        elif choice == "2":
            password_tools.analyze_password()
        elif choice == "3":
            password_tools.add_credential()
        elif choice == "4":
            password_tools.search_credential()
        elif choice == "5":
            password_tools.view_all()
        elif choice == "6":
            password_tools.delete_credential()
        elif choice == "7":
            print("Exiting BitXBytes... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()