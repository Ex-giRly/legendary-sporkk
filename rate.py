from tkinter import *
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())
        si = (principal * time * rate) / 100
        result_si.set(f"Simple Interest: {si:.2f}")
    except ValueError:
        messagebox.showerror("Error", "write it correctly!")

root = Tk()
root.title("Simple Interest Calculator")
root.configure(bg="lightblue")
root.geometry("400x250")

Label(root, text="Principle:", bg="lightblue").place(x=50, y=50)
Label(root, text="Time  (years):", bg="lightblue").place(x=50, y=90)
Label(root, text="Rate  (%):", bg="lightblue").place(x=50, y=130)

entry_principal = Entry(root)
entry_time = Entry(root)
entry_rate = Entry(root)

entry_principal.place(x=200, y=50)
entry_time.place(x=200, y=90)
entry_rate.place(x=200, y=130)

Button(root, text="Calculate", command=calculate_interest, bg="brown", fg="white").place(x=160, y=170)

result_si = StringVar()
Label(root, textvariable=result_si, bg="lightblue", font=("Arial", 10, "bold")).place(x=50, y=210)

root.mainloop()