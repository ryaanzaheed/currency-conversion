import tkinter as tk
from currency_converter import convert_currency, get_exchange_rates

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
        ts = getattr(get_exchange_rates, "last_fetch_time", None)
        if ts:
            
            label_ts.config(text="As of " + ts.strftime("%Y‑%m‑%d %H:%M UTC"))
    except Exception:
        label_result.config(text="Conversion error: check your inputs.")

#Convert button
btn = tk.Button(root, text="Convert", command=on_convert)
btn.pack(pady=(0,10))

root.mainloop()