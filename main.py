import tkinter as tk
from tkinter import IntVar, StringVar
from commons.constants import window_width, window_height, cpadx
from database.db_manager import check_pin, get_visitor_info, get_visitors, get_visitor, del_visitor, add_update_visitor

pin_mask = '****'
counter = 0
entered_pin = ''

def pin_entry(value):
    global counter, entered_pin
    entered_pin += str(value)
    counter += 1

    if counter == 1:
        pin_entry_digit1_var.set(value)
    if counter == 2:
        pin_entry_digit2_var.set(value)
    if counter == 3:
        pin_entry_digit3_var.set(value)
    if counter == 4:
        pin_entry_digit4_var.set(value)
        if check_pin(entered_pin):
            visitor = get_visitor_info(entered_pin)
            lbl_status_msg_var.set(f'Dobro došao/a {visitor.first_name}')
            if visitor.first_name == 'admin':
                show_panel(admin_panel)
        else:
            lbl_status_msg_var.set(f'Unijeli ste nepostojeći pin! \n Pokušajte ponovno ili pozvonite!')
            reset_parameters()
                  

def hide_panel(panel):
    panel.grid_remove()
    lbl_status_msg_var.set('Status i poruke')
    reset_parameters()
    
    
def reset_parameters():
    global counter, entered_pin
    counter = 0
    entered_pin = ''
    pin_entry_digit1_var.set('*')
    pin_entry_digit2_var.set('*')
    pin_entry_digit3_var.set('*')
    pin_entry_digit4_var.set('*')


def show_panel(panel):
    if panel == pin_panel:
        lbl_welcome_msg_var.set('Dobro došli!')    
        panel.grid(row=1, column=0, padx=cpadx, pady=(10, 10))
    else:
        admin_panel.grid(row=2, column=0, padx=cpadx, pady=(20, 20))
    

def ring():
    hide_panel(pin_panel)
    hide_panel(admin_panel)
    lbl_welcome_msg_var.set('Pričekajte koji trenutak.')


def on_element_clicked(event):
    index = lbox_names.curselection()
    value = lbox_names.get(index)
    user = get_visitor(value.split(' ')[0])
    entry_first_name_var.set(user.first_name)
    entry_last_name_var.set(user.last_name)
    entry_pin_var.set(user.pin)
    cb_status_var.set(user.status)


def visitor_edit(db_entry_first_name, db_entry_last_name, db_entry_pin, db_entry_status):
    lbl_status_msg_var.set(add_update_visitor(db_entry_first_name, db_entry_last_name, db_entry_pin, db_entry_status))
    lbox_names.delete(0, tk.END)
    refresh_lbox()

def visitor_delete(first_name):
    lbl_status_msg_var.set(del_visitor(first_name))
    lbox_names.delete(0, tk.END)
    refresh_lbox()



def refresh_lbox():
    global visitors_names
    visitors_names = get_visitors()
    for name in visitors_names:
        lbox_names.insert(tk.END, name)


#region MAIN WINDOW
main_window = tk.Tk()
main_window.title('Smart key app')
main_window.geometry(f'{window_width}x{window_height}')

#endregion

#region FRAMES
#region BUTTON PANEL
button_panel = tk.Frame(main_window)
button_panel.columnconfigure(0, minsize=window_width-(2 * cpadx))
lbl_welcome_msg_var = StringVar()
lbl_welcome_msg_var.set('Dobro došli!')
button_panel.grid(row=0, column=0, padx=cpadx, pady=(20, 10))

lbl_welcome_msg = tk.Label(button_panel,
                            textvariable=lbl_welcome_msg_var)
lbl_welcome_msg.grid(row=0, column=0, pady=(0 , 40), columnspan=6)

ring_button = tk.Button(button_panel,
                        text='Pozvoni',
                        command=lambda : ring())
ring_button.grid(row=1, column=0, padx=20, sticky='W')

unlock_button = tk.Button(button_panel,
                        text='Otključaj',
                        command=lambda : show_panel(pin_panel))
unlock_button.grid(row=1, column=0, padx=20, sticky='E')
#endregion

#region PIN PANEL
pin_panel = tk.Frame(main_window)
pin_panel.columnconfigure((0, 1, 2, 3), minsize=int((window_width - (2 * cpadx) - 40) / 9))
pin_panel.columnconfigure((4), minsize=int((window_width - (2 * cpadx) - 40) / 9) * 5)

pin_entry_digit1_var = StringVar()
pin_entry_digit2_var = StringVar()
pin_entry_digit3_var = StringVar()
pin_entry_digit4_var = StringVar()
pin_entry_digit1_var.set('*')
pin_entry_digit2_var.set('*')
pin_entry_digit3_var.set('*')
pin_entry_digit4_var.set('*')
    


lbl_pin_header = tk.Label(pin_panel,
                            text='Unos pina',)
lbl_pin_header.grid(row=0, column=0, pady=(0 , 40), columnspan=9)

lbl_pin_digit_one = tk.Label(pin_panel,
                                textvariable=pin_entry_digit1_var)
lbl_pin_digit_one.grid(row=1, column=0, padx=(0 , 20), pady=(0 , 10), sticky='W')

lbl_pin_digit_two = tk.Label(pin_panel,
                            textvariable=pin_entry_digit2_var)
lbl_pin_digit_two.grid(row=1, column=1, padx=(0 , 20), pady=(0 , 10), sticky='W')

lbl_pin_digit_three = tk.Label(pin_panel,
                            textvariable=pin_entry_digit3_var)
lbl_pin_digit_three.grid(row=1, column=2, padx=(0 , 20), pady=(0 , 10), sticky='W')

lbl_pin_digit_four = tk.Label(pin_panel,
                                textvariable=pin_entry_digit4_var)
lbl_pin_digit_four.grid(row=1, column=3, padx=(0 , 20), pady=(0 , 10), sticky='W')

lbl_status_msg_var = StringVar()
lbl_status_msg_var.set('Status i poruke')
lbl_status = tk.Label(pin_panel,
                    textvariable=lbl_status_msg_var)
lbl_status.grid(row=1, column=4, pady=(0 , 10), columnspan=5, rowspan=5)

pin_button_one = tk.Button(pin_panel,
                            text='1',
                            command=lambda : pin_entry(1))
pin_button_one.grid(row=2, column=0, padx=(0 , 20), pady=(0 , 10))

pin_button_two = tk.Button(pin_panel,
                            text='2',
                            command=lambda : pin_entry(2))
pin_button_two.grid(row=2, column=1, padx=(0 , 20), pady=(0 , 10))

pin_button_three= tk.Button(pin_panel,
                            text='3',
                            command=lambda : pin_entry(3))
pin_button_three.grid(row=2, column=2, padx=(0 , 20), pady=(0 , 10))

pin_button_four = tk.Button(pin_panel,
                            text='4',
                            command=lambda : pin_entry(4))
pin_button_four.grid(row=3, column=0, padx=(0 , 20), pady=(0 , 10))

pin_button_five = tk.Button(pin_panel,
                            text='5',
                            command=lambda : pin_entry(5))
pin_button_five.grid(row=3, column=1, padx=(0 , 20), pady=(0 , 10))

pin_button_six = tk.Button(pin_panel,
                            text='6',
                            command=lambda : pin_entry(6))
pin_button_six.grid(row=3, column=2, padx=(0 , 20), pady=(0 , 10))

pin_button_seven = tk.Button(pin_panel,
                            text='7',
                            command=lambda : pin_entry(7))
pin_button_seven.grid(row=4, column=0, padx=(0 , 20), pady=(0 , 10))

pin_button_eight = tk.Button(pin_panel,
                            text='8',
                            command=lambda : pin_entry(8))
pin_button_eight.grid(row=4, column=1, padx=(0 , 20), pady=(0 , 10))

pin_button_nine = tk.Button(pin_panel,
                            text='9',
                            command=lambda : pin_entry(9))
pin_button_nine.grid(row=4, column=2, padx=(0 , 20), pady=(0 , 10))

pin_button_zero = tk.Button(pin_panel,
                            text='0',
                            command=lambda : pin_entry(0))
pin_button_zero.grid(row=5, column=1, padx=(0 , 20), pady=(0 , 10))

pin_button_clear = tk.Button(pin_panel,
                            text='C',
                            command=lambda : reset_parameters())
pin_button_clear.grid(row=5, column=2, padx=(0 , 20), pady=(0 , 10))


#endregion


admin_panel = tk.Frame(main_window)
admin_panel.columnconfigure((0, 1, 2), minsize=15)
# admin_panel.columnconfigure((1), minsize=int(window_width - (2 * cpadx) / 32))
# admin_panel.columnconfigure((2), minsize=int(window_width - (2 * cpadx) / 32))

lbl_admin_header = tk.Label(admin_panel,
                             text='Upravljanje dodijeljenim ključevima')
lbl_admin_header.grid(row=0, column=0, pady=(0 , 20), columnspan=8)

lbox_names = tk.Listbox(admin_panel, width=15)
lbox_names.grid(row=1, column=0, padx=(10 , 10), sticky='W', rowspan=5)
visitors_names = get_visitors()
for name in visitors_names:
        lbox_names.insert(tk.END, name)
lbox_names.bind('<ButtonRelease-1>', on_element_clicked)


lbl_admin_first_name = tk.Label(admin_panel,
                                text='Ime',
                                justify='right')
lbl_admin_first_name.grid(row=1, column=1, padx=10, pady=(0, 5), sticky='E')

entry_first_name_var = StringVar()
entry_first_name = tk.Entry(admin_panel,
                            textvariable=entry_first_name_var)
entry_first_name.grid(row=1, column=2, columnspan=2)

lbl_admin_last_name = tk.Label(admin_panel,
                                text='Prezime',
                                justify='right')
lbl_admin_last_name.grid(row=2, column=1, padx=10, pady=(0, 5), sticky='E')

entry_last_name_var = StringVar()
entry_last_name = tk.Entry(admin_panel,
                           textvariable=entry_last_name_var)
entry_last_name.grid(row=2, column=2, columnspan=2)

lbl_admin_pin = tk.Label(admin_panel,
                        text='PIN (4 broja)',
                        justify='right')
lbl_admin_pin.grid(row=3, column=1, padx=10, pady=(0, 5), sticky='E')

entry_pin_var = StringVar()
entry_pin = tk.Entry(admin_panel,
                     textvariable=entry_pin_var)
entry_pin.grid(row=3, column=2, columnspan=2)

lbl_admin_status = tk.Label(admin_panel,
                            text='Aktivan',
                            justify='right')
lbl_admin_status.grid(row=4, column=1, padx=10, pady=(0, 5), sticky='E')
cb_status_var = IntVar()
cb_status = tk.Checkbutton(admin_panel, variable=cb_status_var)
cb_status.grid(row=4, column=2)

admin_button_save = tk.Button(admin_panel,
                                text='Spremi',
                                command=lambda : visitor_edit(entry_first_name_var.get(),
                                                            entry_last_name_var.get(),
                                                            entry_pin_var.get(),
                                                            cb_status_var.get()))
admin_button_save.grid(row=5, column=1)

admin_button_cancel = tk.Button(admin_panel,
                                text='Odustani',
                                command=lambda : hide_panel(admin_panel))
admin_button_cancel.grid(row=5, column=2, sticky='W')

admin_button_delete = tk.Button(admin_panel,
                                text='Obriši',
                                command=lambda : visitor_delete(entry_first_name_var.get()))
admin_button_delete.grid(row=5, column=3, sticky='W')



# names = ['Pero Peric', 'Ana Anic', 'Marko Maric', 'Iva Ivic', 'Vinko Vinic']
# for name in names:
#     lbox_names.insert(tk.END, name)
# lbox_names.bind('<ButtonRelease-1>', on_element_clicked)



main_window.mainloop()
#endregion






























    #endregion



