import tkinter as tk
import random

class Application:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Trommeln")
        self.root.state('zoomed')
        
        # Display initial "Start" text and center it in the window.
        self.label = tk.Label(root, text="Start", width=22, font=("Helvetica Neue", 168))
        self.label.pack(expand=True, anchor="center")
        
        # Sequential list of songs
        self.songs = ["Caipirinha", "Cuba Libre", "Daiquiri", "Gin Tonic", 
                      "Margarita", "Mojito Cocco", "Pina Colada", "Tequila Sunrise"]
        
        # Countdown duration (in seconds)
        self.countdown_time = 5
        
        # Bind the space key to the start method
        self.root.bind("<space>", self.start)
        
        self.delay = 10000
    
    def start(self, event=None):
        # Unbind the space key to avoid multiple triggers
        self.root.unbind("<space>")
        # Start the countdown
        self.countdown()
    
    def countdown(self):
        if self.countdown_time > 0:
            self.label.config(text=str(self.countdown_time))
            self.countdown_time -= 1
            self.root.after(1000, self.countdown)
        else:
            # After the countdown, show the first song
            self.show_next_song()
    
    def show_next_song(self):
        if self.songs != []:
            self.song = random.choice(self.songs)
            self.song_index = self.songs.index(self.song)
            self.songs.pop(self.song_index)
            self.label.config(text=self.song)
            if self.delay == 10000:
                self.root.after(self.delay, self.show_next_song)
                self.delay = 20000
            else:
                self.root.after(self.delay, self.show_next_song)

        else:
            self.label.config(text="You're Done")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
