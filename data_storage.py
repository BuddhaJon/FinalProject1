import csv
from typing import Dict

FILE_NAME = 'results.csv'

def save_votes(votes: Dict[str, int]) -> None:
    """
    Saves the vote count to a CSV file.

    Args:
        votes (Dict[str, int]): A dictionary containing candidate names as keys and vote counts as values.
    """
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for candidate, count in votes.items():
            writer.writerow([candidate, count])

def load_votes() -> Dict[str, int]:
    """
    Loads the vote count from a CSV file.

    Returns:
        Dict[str, int]: A dictionary containing candidate names as keys and vote counts as values.
    """
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.reader(file)
            return {rows[0]: int(rows[1]) for rows in reader}
    except FileNotFoundError:
        return {"John": 0, "Jane": 0}
