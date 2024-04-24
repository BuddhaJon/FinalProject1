import csv
from typing import Dict

FILE_NAME = 'results.csv'

def append_session_results(votes: Dict[str, int]) -> None:
    """
    Appends the current session's results to a CSV file.
    """
    with open(FILE_NAME, 'a', newline='') as file:  # 'a' is for append mode
        writer = csv.writer(file)
        john_votes = votes.get('John', 0)
        jane_votes = votes.get('Jane', 0)
        total_votes = john_votes + jane_votes
        writer.writerow(['John', john_votes, 'Jane', jane_votes, 'Total', total_votes])

def load_votes() -> Dict[str, int]:
    """
    Loads the vote count from a CSV file.
    """
    try:
        with open(FILE_NAME, 'r', newline='') as file:
            reader = csv.reader(file)
            return {row[0]: int(row[1]) for row in reader}
    except FileNotFoundError:
        return {"John": 0, "Jane": 0}
