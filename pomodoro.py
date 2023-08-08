import tkinter as tk
from tkinter import messagebox
import time

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.work_time = 25 * 60  # 25 minutes in seconds
        self.break_time = 5 * 60  # 5 minutes in seconds
        self.is_break = False
        self.time_remaining = self.work_time
        self.running = False
        self.timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        
        self.timer_label.pack(pady=20)
        self.start_button.pack()
        self.stop_button.pack()
        
    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()
    
    def stop_timer(self):
        if self.running:
            self.running = False
    
    def update_timer(self):
        if self.running:
            self.timer_label.config(text=self.format_time(self.time_remaining))
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

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
