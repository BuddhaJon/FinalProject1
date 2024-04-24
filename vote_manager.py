from data_storage import load_votes, append_session_results

class VoteManager:
    """Manages the logic of voting and maintaining vote counts."""
    def __init__(self):
        self.votes = {"John": 0, "Jane": 0}  # Initialize with zero votes

    def add_vote(self, candidate: str) -> None:
        """Adds a vote to a specified candidate."""
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            self.votes[candidate] = 1  # In case of a new candidate, not likely needed based on the setup

    def reset_votes(self) -> None:
        """Resets the vote counts to zero."""
        self.votes = {"John": 0, "Jane": 0} # Resets votes to zero

    def get_results(self) -> str:
        """Returns a formatted string of the voting results."""
        return "\n".join(f"{candidate} - {count} votes" for candidate, count in self.votes.items())
