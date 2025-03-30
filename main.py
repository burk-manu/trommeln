import tkinter as tk
import random

class SongTimerApp:
    """
    A Tkinter-based application that displays a countdown and then shows random song names
    from a predefined list with a timer for each song display.
    """
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Song Timer")
        
        # Main label to display the countdown and song names
        self.song_label = tk.Label(root, text="Start", width=22, font=("Helvetica Neue", 96))
        self.song_label.pack(expand=True, anchor="center")
        
        # Label for the countdown timer display
        self.timer_label = tk.Label(root, text="Timer", width=22, font=("Helvetica Neue", 26))
        self.timer_label.pack(expand=True, anchor="e")
        
        # List of available song names
        self.song_list = [
            "Caipirinha", "Cuba Libre", "Daiquiri", "Gin Tonic", 
            "Margarita", "Mojito Cocco", "Pina Colada", "Tequila Sunrise"
        ]
        
        # Bind the spacebar key to start the countdown
        self.root.bind("<space>", self.start_countdown)
        
        self.song_timer_delay = 10   # Initial timer delay in seconds for song display
        self.is_running = False      # Flag indicating whether the app is currently running
        self.current_color = "blue"  # Initial text color for song display

    def start_countdown(self, event=None) -> None:
        """
        Starts the countdown if the application is not already running.
        """
        if not self.is_running:
            self.is_running = True
            self.remaining_countdown = 5  # Countdown starting value in seconds
            self.remaining_songs = list(self.song_list)  # Create a copy of the song list
            self._update_countdown()

    def _update_countdown(self) -> None:
        """
        Updates the countdown display every second.
        Changes text color to red when 3 seconds or less remain.
        """
        if self.remaining_countdown > 0:
            # Use red for the final 3 seconds, black otherwise.
            color = "red" if self.remaining_countdown <= 3 else "black"
            self.song_label.config(text=str(self.remaining_countdown), fg=color)
            self.remaining_countdown -= 1
            self.root.after(1000, self._update_countdown)
        else:
            self._display_next_song()

    def _start_song_timer(self, duration: float) -> None:
        """
        Initializes and starts the timer for displaying the current song.
        
        Args:
            duration: The duration in seconds for which the song should be displayed.
        """
        self.song_timer_remaining = duration
        self._update_song_timer()

    def _update_song_timer(self) -> None:
        """
        Updates the timer display every 0.1 seconds and recursively continues until time runs out.
        """
        if self.song_timer_remaining > 0:
            self.timer_label.config(text=f"{self.song_timer_remaining:.1f}")
            self.song_timer_remaining -= 0.1
            self.root.after(100, self._update_song_timer)
        else:
            self._display_next_song()

    def _display_next_song(self) -> None:
        """
        Displays the next random song from the list if available.
        Alternates the display color and starts a new timer.
        Ends the session if no songs remain.
        """
        if self.remaining_songs:
            # Randomly select a song and remove it from the remaining songs list.
            next_song = random.choice(self.remaining_songs)
            self.remaining_songs.remove(next_song)
            self.song_label.config(text=next_song, fg=self.current_color)
            
            # Toggle the text color between blue and green for variety.
            self.current_color = "green" if self.current_color == "blue" else "blue"
            
            # Start the timer for the current song display.
            self._start_song_timer(self.song_timer_delay)
            
            # Optionally change the delay for subsequent songs.
            if self.song_timer_delay == 10:
                self.song_timer_delay = 20
        else:
            # No more songs available; end the session.
            self.song_label.config(text="You're Done", fg="black")
            self.timer_label.config(text="")
            self.is_running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = SongTimerApp(root)
    root.mainloop()

