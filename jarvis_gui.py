import tkinter as tk
from voice_assistant import run_jarvis, wish_user
import threading

def start_voice_assistant():
    threading.Thread(target=run_jarvis).start()

app = tk.Tk()
app.title("Jarvis Voice Assistant")
app.geometry("400x300")
app.configure(bg='black')

heading = tk.Label(app, text="Jarvis", font=("Arial", 24, 'bold'), bg='black', fg='cyan')
heading.pack(pady=20)

btn_start = tk.Button(app, text="Start Listening", font=("Arial", 16), command=start_voice_assistant, bg='green', fg='white')
btn_start.pack(pady=20)

btn_quit = tk.Button(app, text="Exit", font=("Arial", 16), command=app.quit, bg='red', fg='white')
btn_quit.pack(pady=10)

wish_user()
app.mainloop()
