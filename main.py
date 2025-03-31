import tkinter as tk
import random

class SongTimerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Song Timer")
        self.root.config(bg="#121212")
        
        # Main label to display the countdown and song names
        self.song_label = tk.Label(root, text="Start", width=22, font=("Helvetica Neue", 96))
        self.song_label.config(bg="#121212", fg="#8EADDB")
        self.song_label.pack(expand=True, anchor="center")
        
        # Label for the countdown timer display
        self.timer_label = tk.Label(root, text="Timer", width=22, font=("Helvetica Neue", 26))
        self.timer_label.config(bg="#121212", fg="#8EADDB")
        self.timer_label.pack(expand=True, anchor="e")
        
        # Label for song counter display
        self.counter_label = tk.Label(root, text="", width=22, font=("Helvetica Neue", 26))
        self.counter_label.config(bg="#121212", fg="#8EADDB")
        self.counter_label.pack(expand=True, anchor="w")
        
        # List of available song names
        self.song_list = [
            "Caipirinha", "Cuba Libre", "Daiquiri", "Gin Tonic", 
            "Margarita", "Mojito Cocco", "Pina Colada", "Tequila Sunrise"
        ]
        
        # Total number of songs available
        self.songs_total = len(self.song_list)
        # Counter for the current song number
        self.current_song_index = 0
        
        # Bind the spacebar key to start the countdown
        self.root.bind("<space>", self.start_countdown)
        
        self.song_timer_delay = 9    # Initial timer delay in seconds for song display
        self.is_running = False      # Flag indicating whether the app is currently running
        self.current_color = "#8EADDB"  # Initial text color for song display

    def start_countdown(self, event=None) -> None:
        if not self.is_running:
            self.is_running = True
            self.remaining_countdown = 5  # Countdown starting value in seconds
            self.remaining_songs = list(self.song_list)  # Create a copy of the song list
            self.current_song_index = 0  # Reset song counter
            self._update_countdown()

    def _update_countdown(self) -> None:
        if self.remaining_countdown > 0:
            # Use red for the final 3 seconds, black otherwise.
            color = "#8EADDB"
            self.song_label.config(text=str(self.remaining_countdown), fg=color)
            self.remaining_countdown -= 1
            self.root.after(1000, self._update_countdown)
        else:
            self._display_next_song()

    def _start_song_timer(self, duration: float) -> None:
        self.song_timer_remaining = duration
        self._update_song_timer()

    def _update_song_timer(self) -> None:
        if self.song_timer_remaining > 0:
            self.timer_label.config(text=f"{self.song_timer_remaining:.1f}")
            self.song_timer_remaining -= 0.1
            self.root.after(100, self._update_song_timer)
        else:
            self._display_next_song()

    def _display_next_song(self) -> None:
        if self.remaining_songs:
            # Increment song counter
            self.current_song_index += 1
            
            # Update the counter label with the current song number and total number of songs.
            self.counter_label.config(text=f"{self.current_song_index}/{self.songs_total}")
            
            # Randomly select a song and remove it from the remaining songs list.
            next_song = random.choice(self.remaining_songs)
            self.remaining_songs.remove(next_song)
            self.song_label.config(text=next_song, fg=self.current_color)
            
            # Toggle the text color between blue and green for variety.
            self.current_color = "#D884BF" if self.current_color == "#8EADDB" else "#8EADDB"
            
            # Start the timer for the current song display.
            self._start_song_timer(self.song_timer_delay)
            
            # Optionally change the delay for subsequent songs.
            if self.song_timer_delay == 9:
                self.song_timer_delay = 19
        else:
            # No more songs available; end the session.
            self.song_label.config(text="You're Done", fg="#8EADDB")
            self.timer_label.config(text="")
            self.counter_label.config(text="")
            self.is_running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = SongTimerApp(root)
    root.mainloop()

