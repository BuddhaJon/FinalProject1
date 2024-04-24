import tkinter as tk
from tkinter import messagebox
from vote_manager import VoteManager
from data_storage import append_session_results



class VotingApp(tk.Tk):
    """A GUI application for voting."""

    def __init__(self):
        super().__init__() # Sets up the GUI interface below
        self.title('Voting System')
        self.geometry('300x250')
        self.vote_manager = VoteManager()

        self.create_widgets()
        self.update_vote_count_labels()

    def create_widgets(self):
        """Creates widgets for the application."""
        tk.Label(self, text='Voting App', font=('Helvetica', 16)).pack(pady=10)

        tk.Button(self, text='Vote for John', command=lambda: self.vote('John')).pack(pady=5)
        tk.Button(self, text='Vote for Jane', command=lambda: self.vote('Jane')).pack(pady=5)
        tk.Button(self, text='Exit', command=self.exit_app).pack(pady=10)

        # Labels to display the vote counts
        self.john_vote_label = tk.Label(self, text='', font=('Helvetica', 12))
        self.john_vote_label.pack()
        self.jane_vote_label = tk.Label(self, text='', font=('Helvetica', 12))
        self.jane_vote_label.pack()
        self.total_vote_label = tk.Label(self, text='', font=('Helvetica', 12))
        self.total_vote_label.pack()

    def vote(self, candidate: str):
        """Handles voting for a candidate."""
        self.vote_manager.add_vote(candidate)
        messagebox.showinfo("Vote Recorded", f"Voted for {candidate}")
        self.update_vote_count_labels()

    def update_vote_count_labels(self):
        """Updates the labels with the current vote counts."""
        votes = self.vote_manager.votes
        john_votes = votes.get('John', 0)
        jane_votes = votes.get('Jane', 0)
        total_votes = john_votes + jane_votes # Logic for totalling the vote count
        self.john_vote_label.config(text=f"John: {john_votes} votes")
        self.jane_vote_label.config(text=f"Jane: {jane_votes} votes")
        self.total_vote_label.config(text=f"Total: {total_votes} votes")

    def exit_app(self):
        """Exits the app after appending results to CSV and showing results."""
        results = self.vote_manager.get_results()
        append_session_results(self.vote_manager.votes)  # Append results to CSV
        messagebox.showinfo("Results", results)
        self.vote_manager.reset_votes()  # Reset votes after appending
        self.destroy()


def main():
    app = VotingApp()
    app.mainloop()


if __name__ == "__main__":
    main()
