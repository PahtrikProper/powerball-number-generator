import tkinter as tk
import secrets
import sys

# --- Secure Random Generator ---
secure_rng = secrets.SystemRandom()

# --- Generate one secure Powerball game (7 numbers + 1 Powerball) ---
def generate_powerball_game_secure():
    main_numbers = sorted(secure_rng.sample(range(1, 36), 7))
    powerball = secure_rng.randint(1, 20)
    return main_numbers, powerball

def generate_multiple_games_secure(count=4):
    return [generate_powerball_game_secure() for _ in range(count)]

# --- Animate the number draw ---
def animate_draw(results, delay=80):
    def animate_label(label, final_value, is_powerball=False):
        steps = 10
        def step(i=0):
            if i < steps:
                flicker = secure_rng.randint(1, 35 if not is_powerball else 20)
                label.config(text=flicker, bg="lightyellow", fg="black")
                root.after(delay, lambda: step(i + 1))
            else:
                final_bg = "purple" if is_powerball else "white"
                final_fg = "white" if is_powerball else "black"
                label.config(text=final_value, bg=final_bg, fg=final_fg, highlightbackground="green", highlightthickness=2)
        step()

    for row in range(4):
        main, pb = results[row]
        for col in range(7):
            val = main[col]
            label = entries[row][col]
            delay_offset = (row * 8 + col) * delay
            root.after(delay_offset, lambda l=label, v=val: animate_label(l, v))
        pb_label = powerballs[row]
        pb_delay = (row * 8 + 7) * delay
        root.after(pb_delay, lambda l=pb_label, v=pb: animate_label(l, v, is_powerball=True))

# --- Trigger a new draw ---
def generate_and_display():
    results = generate_multiple_games_secure(4)
    animate_draw(results)

# --- Exit the app ---
def exit_app():
    root.destroy()
    sys.exit()

# --- GUI Setup ---
root = tk.Tk()
root.title("Powerball Number Generator")
root.geometry("600x420")
root.overrideredirect(True)  # 🟨 Remove OS title bar
root.configure(bg="yellow")
root.resizable(False, False)

# --- Center the window on screen ---
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 600
window_height = 420
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# --- Title Label ---
tk.Label(
    root,
    text="Powerball Number Generator",
    font=("Helvetica", 18, "bold"),
    bg="yellow",
    fg="black"
).pack(pady=12)

# --- Game Ball Grid ---
entries = []
powerballs = []
frame = tk.Frame(root, bg="yellow")
frame.pack()

for row in range(4):
    row_entries = []
    for col in range(7):
        label = tk.Label(
            frame,
            text="--",
            width=4,
            height=2,
            font=("Helvetica", 16, "bold"),
            bg="white",
            fg="black",
            relief="solid",
            bd=2,
            highlightbackground="green",
            highlightthickness=1
        )
        label.grid(row=row, column=col, padx=6, pady=6)
        row_entries.append(label)

    pb_label = tk.Label(
        frame,
        text="PB",
        width=4,
        height=2,
        font=("Helvetica", 16, "bold"),
        bg="purple",
        fg="white",
        relief="raised",
        bd=2,
        highlightbackground="green",
        highlightthickness=1
    )
    pb_label.grid(row=row, column=7, padx=12)
    entries.append(row_entries)
    powerballs.append(pb_label)

# --- Buttons ---
btn_frame = tk.Frame(root, bg="yellow")
btn_frame.pack(pady=15)

tk.Button(
    btn_frame,
    text="🎲 Draw Numbers",
    command=generate_and_display,
    font=("Helvetica", 14),
    bg="green",
    fg="white",
    relief="raised",
    padx=15,
    pady=5
).grid(row=0, column=0, padx=20)

tk.Button(
    btn_frame,
    text="❌ Exit",
    command=exit_app,
    font=("Helvetica", 14),
    bg="darkred",
    fg="white",
    relief="raised",
    padx=15,
    pady=5
).grid(row=0, column=1, padx=20)

# --- First automatic draw ---
generate_and_display()
root.mainloop()
