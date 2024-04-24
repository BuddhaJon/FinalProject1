from vote_manager import VoteManager

def main():
    """
    Main function to run the voting application.
    """
    vote_manager = VoteManager()

    while True:
        print("--------------------------")
        print("VOTE MENU")
        print("--------------------------")
        print("v: Vote")
        print("x: Exit")
        option = input("Option: ").strip().lower()

        if option == 'v':
            print("--------------------------")
            print("CANDIDATE MENU")
            print("--------------------------")
            print("1: John")
            print("2: Jane")
            candidate_option = input("Option: ").strip()

            if candidate_option == '1':
                vote_manager.add_vote("John")
                print("Voted for Candidate 1")
            elif candidate_option == '2':
                vote_manager.add_vote("Jane")
                print("Voted for Candidate 2")
            else:
                print(f"Invalid (1/2): {candidate_option}")

        elif option == 'x':
            print("Exiting. Final results:")
            print(vote_manager.get_results())
            print(f"Total - {vote_manager.total_votes()} votes")
            vote_manager.reset_votes()  # Reset the votes for the next session.
            break
        else:
            print(f"Invalid (v/x): {option}")

if __name__ == "__main__":
    main()
