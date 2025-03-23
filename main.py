import tkinter as tk

count = 0

def increase():
    global count
    count += 1
    cnt_label.config(text=f"Score: {count}")

def decrease():
    global count
    if count > 0:
        count -= 1
    cnt_label.config(text=f"Score: {count}")

def reset():
    global count
    count = 0
    cnt_label.config(text=f"Score: {count}")

root = tk.Tk()
root.title("COUNTER")
root.geometry("350x350")

cnt_label = tk.Label(root, text="Score: 0", font=("Helvetica", 16))
cnt_label.pack(pady=20)

plus_button = tk.Button(root, text="+", font=("Helvetica", 16), command=increase)
plus_button.pack(pady=20)

minus_button = tk.Button(root, text="-", font=("Helvetica", 16), command=decrease)
minus_button.pack(pady=20)

reset_button = tk.Button(root, text="RESET", font=("Helvetica", 16), command=reset)
reset_button.pack(pady=20)

root.mainloop()