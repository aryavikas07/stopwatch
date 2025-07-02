import tkinter as tk
from datetime import datetime
import time

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("⏱ Stopwatch")
        self.master.geometry("300x400")
        self.master.resizable(False, False)

        # Timer Variables
        self.start_time = None
        self.running = False
        self.laps = []
        self.elapsed = 0.0

        # Time Display Label
        self.time_label = tk.Label(master, text="00:00:00.000", font=("Helvetica", 24), pady=20)
        self.time_label.pack()

        # Buttons
        self.start_button = tk.Button(master, text="Start", width=10, command=self.start)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Stop", width=10, command=self.stop)
        self.stop_button.pack(pady=5)

        self.lap_button = tk.Button(master, text="Lap", width=10, command=self.lap)
        self.lap_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset", width=10, command=self.reset)
        self.reset_button.pack(pady=5)

        # Lap Display
        self.lap_listbox = tk.Listbox(master, width=30, height=10)
        self.lap_listbox.pack(pady=10)

        # Update timer every 50ms
        self.update_timer()

    def update_timer(self):
        if self.running:
            current = time.time()
            self.elapsed = current - self.start_time
            self.update_display()
        self.master.after(50, self.update_timer)

    def update_display(self):
        millis = int((self.elapsed - int(self.elapsed)) * 1000)
        minutes = int(self.elapsed // 60)
        seconds = int(self.elapsed % 60)
        time_str = f"{minutes:02}:{seconds:02}.{millis:03}"
        self.time_label.config(text=f"00:{time_str}")

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed
            self.running = True

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed = 0.0
        self.time_label.config(text="00:00:00.000")
        self.laps.clear()
        self.lap_listbox.delete(0, tk.END)

    def lap(self):
        if self.running:
            lap_time = self.time_label.cget("text")
            self.laps.append(lap_time)
            self.lap_listbox.insert(tk.END, f"Lap {len(self.laps)}: {lap_time}")

# Run the GUI App
if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
