import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta
import calendar

def calculate_age():
    try:
        birthdate = date_picker.get_date()
        birthdate = datetime(birthdate.year, birthdate.month, birthdate.day)
        today = datetime.today()

        years = today.year - birthdate.year
        months = today.month - birthdate.month
        days = today.day - birthdate.day

        if days < 0:
            months -= 1
            prev_month = (today.month - 1) or 12
            prev_year = today.year if today.month > 1 else today.year - 1
            days += (datetime(prev_year, prev_month + 1, 1) - timedelta(days=1)).day

        if months < 0:
            years -= 1
            months += 12

        total_days = (today - birthdate).days
        next_birthday_year = today.year if (today.month, today.day) < (birthdate.month, birthdate.day) else today.year + 1
        next_birthday = datetime(next_birthday_year, birthdate.month, birthdate.day)
        days_left = (next_birthday - today).days
        weekday = calendar.day_name[next_birthday.weekday()]
        next_birthday_str = f"{weekday}, {next_birthday.strftime('%B %d, %Y')}"
        candle = years + 1

        label_age.config(text=f"Age: {years} y, {months} m, {days} d")
        label_days.config(text=f"Days Lived: {total_days:,}")
        label_next.config(text=f"Next Birthday: {next_birthday_str}")
        label_left.config(text=f"Days Left: {days_left}")
        label_candle.config(text=f"Next Candle: {candle}")

        progress = int(100 - (days_left / 365) * 100)
        progress_bar['value'] = progress
        progress_text.config(text=f"{progress}% of the year passed")

        celebration.config(text="🎉 Happy Birthday! 🎉" if days_left == 0 else "")
    except:
        label_age.config(text="❌ Invalid Input", fg="red")

# GUI setup
root = tk.Tk()
root.title("Age Calculator")
root.geometry("500x570")
root.config(bg="#f0f0f0")

frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=460, height=520)

tk.Label(frame, text="Age Calculator", font=("Segoe UI", 17, "bold"), bg="white", fg="#1a237e").pack(pady=15)
tk.Label(frame, text="Select your birthdate:", font=("Segoe UI", 12), bg="white").pack()
date_picker = DateEntry(frame, width=20, font=("Segoe UI", 12), background="darkblue", foreground="white", borderwidth=2, year=2000)
date_picker.pack(pady=10)

tk.Button(frame, text="Calculate", font=("Segoe UI", 12), bg="#2196f3", fg="white", relief="flat", command=calculate_age).pack(pady=15)

label_age = tk.Label(frame, text="", font=("Segoe UI", 12), bg="white")
label_age.pack(pady=3)
label_days = tk.Label(frame, text="", font=("Segoe UI", 12), bg="white")
label_days.pack(pady=3)
label_next = tk.Label(frame, text="", font=("Segoe UI", 12), bg="white")
label_next.pack(pady=3)
label_left = tk.Label(frame, text="", font=("Segoe UI", 12), bg="white")
label_left.pack(pady=3)
label_candle = tk.Label(frame, text="", font=("Segoe UI", 12), bg="white")
label_candle.pack(pady=3)

progress_text = tk.Label(frame, text="", font=("Segoe UI", 11), bg="white", fg="gray")
progress_text.pack(pady=(10, 5))
progress_bar = ttk.Progressbar(frame, length=280, mode='determinate')
progress_bar.pack()

celebration = tk.Label(frame, text="", font=("Segoe UI", 13, "bold"), bg="white", fg="purple")
celebration.pack(pady=20)

root.mainloop()
