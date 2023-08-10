import tkinter as tk
from tkinter import messagebox
import time
import csv

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.work_time = 25 * 60  # 25 minutes in seconds
        self.break_time = 5 * 60  # 5 minutes in seconds
        self.is_break = False
        self.time_remaining = self.work_time
        self.running = False

        self.comment_entry = tk.Entry(root)
        self.display_panel = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.start_stop = tk.Button(root, text="Start", command=self.start_stop_timer)
        self.pause_resume = tk.Button(root, text="Pause", command=self.pause_resume_timer)
        
        self.comment_entry.pack(pady=10)
        self.display_panel.pack(pady=20)
        self.start_stop.pack()
        self.pause_resume.pack()

        self.log_file = open("pomodoro_log.csv", "a", newline="")
        self.log_writer = csv.writer(self.log_file)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Capture the window close event
    
    def on_closing(self):
        self.log_file.close()
        self.root.destroy()
    
    def start_stop_timer(self):
        action = "Start" if not self.running else "Stop"
        self.log_action(action)
        
        if not self.running:
            self.running = True
            self.start_stop.config(text="Stop")
            self.update_timer()
        else:
            self.running = False
            self.start_stop.config(text="Start")
    
    def pause_resume_timer(self):
        action = "Pause" if self.running else "Resume"
        self.log_action(action)
        
        if self.running:
            self.running = False
            self.pause_resume.config(text="Resume")
        else:
            self.running = True
            self.pause_resume.config(text="Pause")
            self.update_timer()
    
    def update_timer(self):
        if self.running:
            self.display_panel.config(text=self.format_time(self.time_remaining))
            self.time_remaining -= 1
            if self.time_remaining < 0:
                self.toggle_break()
        
        self.root.after(1000, self.update_timer)
    
    def toggle_break(self):
        self.is_break = not self.is_break
        if self.is_break:
            self.time_remaining = self.break_time
            messagebox.showinfo("Break Time", "Take a short break!")
        else:
            self.time_remaining = self.work_time
            messagebox.showinfo("Work Time", "Time to work!")
    
    @staticmethod
    def format_time(seconds):
        minutes = seconds // 60
        seconds %= 60
        return f"{minutes:02d}:{seconds:02d}"

    def log_action(self, action):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.log_writer.writerow([timestamp, f"Action: {action}"])

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
