import tkinter as tk
from datetime import datetime, timedelta, timezone
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from currency_converter import convert_currency, get_spot_history

#Build GUI window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x300")
root.minsize(400, 250)
root.resizable(True, True)

#Takes input for the "from" currency
tk.Label(root, text="From (Currency Code, e.g. USD/BTC):").pack(anchor="w", padx=10, pady=(10,0))
entry_from = tk.Entry(root)
entry_from.pack(fill="x", padx=10)

#Takes input for the "to" currency
tk.Label(root, text="To (Currency Code, e.g. USD/BTC):").pack(anchor="w", padx=10, pady=(10,0))
entry_to = tk.Entry(root)
entry_to.pack(fill="x", padx=10)

#Takes input for the amount
tk.Label(root, text="Amount (In original currency):").pack(anchor="w", padx=10, pady=(10,0))
entry_amt = tk.Entry(root)
entry_amt.pack(fill="x", padx=10)

#Result label
label_result = tk.Label(root, text="—", font=("Arial", 12), fg="blue")
label_result.pack(pady=5)

label_ts = tk.Label(root, text="", font=("Arial", 9), fg="gray")
label_ts.pack(pady=(0, 10))

def on_convert():
    f = entry_from.get().strip().upper()
    t = entry_to.get().strip().upper()
    try:
        a = float(entry_amt.get().strip())
        r = convert_currency(f, t, a)
        if r < 0.01:
                result_str = f"{r:.8f}"
        else:
                result_str = f"{r:,.2f}"

        label_result.config(text=f"{a} {f} = {result_str} {t}")
    except Exception:
        label_result.config(text="Conversion error: check your inputs.")

def on_show_history():
    f = entry_from.get().strip().upper()
    t = entry_to.get().strip().upper()
    pair = f"{f}-{t}"

    #amt user entered
    try:
        amt = float(entry_amt.get().strip())
    except ValueError:
        label_result.config(text="Enter a valid amount for history.")
        return

    #last 7 days
    today = datetime.now(timezone.utc).date()
    start = (today - timedelta(days=6)).isoformat()
    end = today.isoformat()

    try:
        hist = get_spot_history(pair, start, end)
    except Exception as e:
        label_result.config(text=f"History error: {e}")
        return

    dates = sorted(hist)
    xs= [datetime.fromisoformat(d) for d in dates]
    #scale numbers so it looks normal
    ys= [hist[d] * amt for d in dates]

    #plot it
    fig, ax = plt.subplots(figsize=(6,3), dpi=100)
    ax.plot(xs, ys, marker="o")
    ax.set_title(f"{amt:,.2f} {f} → {t} (Last 7 Days)")
    ax.set_xlabel("Date")
    ax.set_ylabel(f"Value ({t})")

    #disable scientific notation on y‑axis so it looks normal
    ax.ticklabel_format(axis="y", style="plain", useOffset=False)

    fig.autofmt_xdate()
    fig.tight_layout()

        #clear previous history canvas if it exists
    global history_canvas
    try:
        history_canvas.get_tk_widget().destroy()
    except NameError:
        pass
    history_canvas = FigureCanvasTkAgg(fig, master=root)
    history_canvas.draw()
    history_canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)
#Convert button
btn_convert = tk.Button(root, text="Convert", command=on_convert)
btn_convert.pack(side="left",  padx=20, pady=10)

btn_hist= tk.Button(root, text="Show 7 Day History", command=on_show_history)
btn_hist.pack(side="right", padx=20, pady=10)


root.mainloop()
