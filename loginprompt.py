import tkinter as tk 
from tkinter import ttk

root=tk.Tk()
root.title("Loginprompt")
root.resizable(0,0)
tabcontrol=ttk.Notebook(root)
tab1=ttk.Frame(tabcontrol)
tab2=ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text="Login")
tabcontrol.add(tab2, text="Sign up")
tabcontrol.grid(row=0, column=0)

#login tab gui..

login_label=ttk.Label(tab1, text="Username     ")
login_label.grid(row=0, column=0)

password_label=ttk.Label(tab1, text="Password")
password_label.grid(row=1, column=0, sticky=tk.W)

username_entry=ttk.Entry(tab1)
username_entry.grid(column=1, row=0)

password_entry=ttk.Entry(tab1, show="*")
password_entry.grid(column=1, row=1)

enter_button=ttk.Button(tab1, text="Enter")
enter_button.grid(column=2, row=2, sticky=tk.W)

#Login ends here...

#Sign up gui starts here..

login_label=ttk.Label(tab2, text="Username     ")
login_label.grid(row=0, column=0, sticky=tk.W)

password_label=ttk.Label(tab2, text="Password")
password_label.grid(row=1, column=0, sticky=tk.W)

username_entry=ttk.Entry(tab2)
username_entry.grid(column=1, row=0, sticky=tk.W+tk.E)

password_entry=ttk.Entry(tab2, show="*")
password_entry.grid(column=1, row=1, sticky=tk.W+tk.E)

Security_question_label=ttk.Label(tab2, text="Security Question     ")
Security_question_label.grid(column=0, row=2, sticky=tk.W)

Security_question_entry=ttk.Entry(tab2)
Security_question_entry.grid(column=1, row=2, columnspan=2, sticky=tk.W+tk.E)

Security_answer_label=ttk.Label(tab2, text="Answer     ")
Security_answer_label.grid(column=0, row=3, sticky=tk.W)

Security_answer_entry=ttk.Entry(tab2)
Security_answer_entry.grid(column=1, row=3, columnspan=2, sticky=tk.W+tk.E)

signup_button=ttk.Button(tab2, text="Sign Up")
signup_button.grid(column=2, row=4, sticky=tk.E)

#Sign up ends here...


root.mainloop()