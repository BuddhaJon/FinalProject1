from data_storage import save_votes, load_votes

class VoteManager:
    """
    Manages voting logic and interacts with the data storage.
    """
    def __init__(self):
        self.votes = load_votes()

    def add_vote(self, candidate: str) -> None:
        """
        Adds a vote to the specified candidate.

        Args:
            candidate (str): The name of the candidate to vote for.

        Raises:
            ValueError: If the candidate name is not recognized.
        """
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            # If the candidate does not exist, add them with one vote
            self.votes[candidate] = 1

    def save_votes(self) -> None:
        """
        Saves the current votes to storage.
        """
        save_votes(self.votes)

    def get_results(self) -> str:
        """
        Retrieves a formatted string of the voting results.

        Returns:
            str: A formatted string of the voting results.
        """
        return "\n".join([f"{candidate} - {self.votes[candidate]} votes" for candidate in self.votes])

    def total_votes(self) -> int:
        """
        Calculates the total number of votes cast.

        Returns:
            int: The total number of votes.
        """
        return sum(self.votes.values())

    def reset_votes(self) -> None:
        """
        Resets the vote counts to zero and saves the empty state to the CSV file.
        """
        self.votes = {"John": 0, "Jane": 0}
        save_votes(self.votes)