import tkinter as tk


window = tk.Tk()
window.title("Address Entry Form")

frm_form = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=1)
frm_form.pack()


lbl_firstName = tk.Label(master=frm_form, text="First Name")
lbl_firstName.grid(row=0, column=0, sticky="e")
ent_firstName = tk.Entry(master=frm_form,  width=40)
ent_firstName.grid(row=0, column=1)

lbl_surName = tk.Label(master=frm_form, text="SurName")
lbl_surName.grid(row=1, column=0, sticky="e")
ent_surName = tk.Entry(master=frm_form,  width=40)
ent_surName.grid(row=1, column=1, padx=5)


lbl_address1 = tk.Label(master=frm_form, text="Adress Line 1")
lbl_address1.grid(row=2, column=0, sticky="e")
ent_address1 = tk.Entry(master=frm_form,  width=40)
ent_address1.grid(row=2, column=1, padx=5)

lbl_address2 = tk.Label(master=frm_form, text="Adress Line 2")
lbl_address2.grid(row=3, column=0, sticky="e")
ent_address2 = tk.Entry(master=frm_form,  width=40)
ent_address2.grid(row=3, column=1, padx=5)

lbl_city = tk.Label(master=frm_form, text="City")
lbl_city.grid(row=4, column=0, sticky="e")
ent_city = tk.Entry(master=frm_form,  width=40)
ent_city.grid(row=4, column=1, padx=5)

lbl_state = tk.Label(master=frm_form, text="State")
lbl_state.grid(row=5, column=0, sticky="e")
ent_state = tk.Entry(master=frm_form,  width=40)
ent_state.grid(row=5, column=1, padx=5)

lbl_postCode = tk.Label(master=frm_form, text="Post Code")
lbl_postCode.grid(row=6, column=0, sticky="e")
ent_postCode = tk.Entry(master=frm_form,  width=40)
ent_postCode.grid(row=6, column=1, padx=5)

lbl_country = tk.Label(master=frm_form, text="Country")
lbl_country.grid(row=7, column=0, sticky="e")
ent_country = tk.Entry(master=frm_form,  width=40)
ent_country.grid(row=7, column=1, padx=5)

frm_buttons = tk.Frame(master=window)
frm_buttons.pack(side=tk.RIGHT)
btn_save = tk.Button(master=frm_buttons, text="Save")
btn_save.pack(side=tk.LEFT)
btn_cancel = tk.Button(master=frm_buttons, text="Cancel")
btn_cancel.pack(side=tk.LEFT)


window.mainloop()
