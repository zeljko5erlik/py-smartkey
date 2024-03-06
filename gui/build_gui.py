import tkinter as tk
from tkinter import IntVar, StringVar
from commons.constants import window_width, cpadx

pin_mask = '****'
counter = 0

def pin_entry(value):
    entered_pin += value
    pass



def hide_panel(panel):
    panel.grid_remove()

def show_panel(panel):
    global pin_mask
    pin_mask = '****'
    
    panel.grid(row=1, column=0, padx=cpadx, pady=(10, 10))
    

def on_element_clicked():
    pass

def create_main_window():
    global window_width, pin_mask
    #region MAIN WINDOW
    main_window = tk.Tk()
    main_window.title('Smart key app')
    main_window.geometry(f'{window_width}x800')
    #endregion

    #region FRAMES
    #region BUTTON PANEL
    button_panel = tk.Frame(main_window)
    button_panel.columnconfigure(0, minsize=window_width-(2 * cpadx))
    
    button_panel.grid(row=0, column=0, padx=cpadx, pady=(20, 10))

    lbl_welcome_msg = tk.Label(button_panel,
                               text='Dobro došli!')
    lbl_welcome_msg.grid(row=0, column=0, pady=(0 , 40), columnspan=6)

    ring_button = tk.Button(button_panel,
                            text='Pozvoni',
                            command=lambda : hide_panel(pin_panel))
    ring_button.grid(row=1, column=0, padx=20, sticky='W')

    unlock_button = tk.Button(button_panel,
                            text='Otključaj',
                            command=lambda : show_panel(pin_panel))
    unlock_button.grid(row=1, column=0, padx=20, sticky='E')
    #endregion


    pin_panel = tk.Frame(main_window)
    pin_panel.columnconfigure((0, 1, 2, 3), minsize=int((window_width - (2 * cpadx) - 40) / 9))
    pin_panel.columnconfigure((4), minsize=int((window_width - (2 * cpadx) - 40) / 9) * 5)
    
    pin_entry_digit1_var = StringVar()
    pin_entry_digit2_var = StringVar()
    pin_entry_digit3_var = StringVar()
    pin_entry_digit4_var = StringVar()
    pin_entry_digit1_var.set(pin_mask[0])
    pin_entry_digit2_var.set(pin_mask[1])
    pin_entry_digit3_var.set(pin_mask[2])
    pin_entry_digit4_var.set(pin_mask[3])
       


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

    lbl_status = tk.Label(pin_panel,
                       text='Status i poruke')
    lbl_status.grid(row=1, column=4, pady=(0 , 10), columnspan=5, rowspan=5)

    pin_button_one = tk.Button(pin_panel,
                               text='1')
    pin_button_one.grid(row=2, column=0, padx=(0 , 20), pady=(0 , 10))

    pin_button_two = tk.Button(pin_panel,
                               text='2')
    pin_button_two.grid(row=2, column=1, padx=(0 , 20), pady=(0 , 10))

    pin_button_three= tk.Button(pin_panel,
                               text='3')
    pin_button_three.grid(row=2, column=2, padx=(0 , 20), pady=(0 , 10))

    pin_button_four = tk.Button(pin_panel,
                               text='4')
    pin_button_four.grid(row=3, column=0, padx=(0 , 20), pady=(0 , 10))

    pin_button_five = tk.Button(pin_panel,
                               text='5')
    pin_button_five.grid(row=3, column=1, padx=(0 , 20), pady=(0 , 10))

    pin_button_six = tk.Button(pin_panel,
                               text='6')
    pin_button_six.grid(row=3, column=2, padx=(0 , 20), pady=(0 , 10))

    pin_button_seven = tk.Button(pin_panel,
                               text='7')
    pin_button_seven.grid(row=4, column=0, padx=(0 , 20), pady=(0 , 10))

    pin_button_eight = tk.Button(pin_panel,
                               text='8')
    pin_button_eight.grid(row=4, column=1, padx=(0 , 20), pady=(0 , 10))

    pin_button_nine = tk.Button(pin_panel,
                               text='9')
    pin_button_nine.grid(row=4, column=2, padx=(0 , 20), pady=(0 , 10))

    pin_button_zero = tk.Button(pin_panel,
                               text='0')
    pin_button_zero.grid(row=5, column=1, padx=(0 , 20), pady=(0 , 10))

    pin_button_clear = tk.Button(pin_panel,
                               text='C')
    pin_button_clear.grid(row=5, column=2, padx=(0 , 20), pady=(0 , 10))




    

    admin_panel = tk.Frame(main_window)
    admin_panel.grid(row=2, column=0, padx=cpadx, pady=(20, 20))
    admin_panel.columnconfigure((0, 1, 2), minsize=15)
    # admin_panel.columnconfigure((1), minsize=int(window_width - (2 * cpadx) / 32))
    # admin_panel.columnconfigure((2), minsize=int(window_width - (2 * cpadx) / 32))

    lbl_admin_header = tk.Label(admin_panel,
                             text='Upravljanje dodijeljenim ključevima')
    lbl_admin_header.grid(row=0, column=0, pady=(0 , 20), columnspan=8)

    lbox_names = tk.Listbox(admin_panel, width=15)
    lbox_names.grid(row=1, column=0, padx=(10 , 10), sticky='W', rowspan=5)

    lbl_admin_first_name = tk.Label(admin_panel,
                                    text='Ime',
                                    justify='right')
    lbl_admin_first_name.grid(row=1, column=1, padx=10, pady=(0, 5), sticky='E')
    entry_first_name = tk.Entry(admin_panel)
    entry_first_name.grid(row=1, column=2, columnspan=2)

    lbl_admin_last_name = tk.Label(admin_panel,
                                   text='Prezime',
                                   justify='right')
    lbl_admin_last_name.grid(row=2, column=1, padx=10, pady=(0, 5), sticky='E')
    entry_last_name = tk.Entry(admin_panel)
    entry_last_name.grid(row=2, column=2, columnspan=2)

    lbl_admin_pin = tk.Label(admin_panel,
                             text='PIN (4 broja)',
                             justify='right')
    lbl_admin_pin.grid(row=3, column=1, padx=10, pady=(0, 5), sticky='E')
    entry_pin = tk.Entry(admin_panel)
    entry_pin.grid(row=3, column=2, columnspan=2)

    lbl_admin_status = tk.Label(admin_panel,
                                text='Aktivan',
                                justify='right')
    lbl_admin_status.grid(row=4, column=1, padx=10, pady=(0, 5), sticky='E')
    cb_status_var = IntVar()
    cb_status = tk.Checkbutton(admin_panel, variable=cb_status_var)
    cb_status.grid(row=4, column=2)

    admin_button_save = tk.Button(admin_panel,
                                  text='Spremi')
    admin_button_save.grid(row=5, column=1)

    admin_button_cancel = tk.Button(admin_panel,
                                  text='Odustani')
    admin_button_cancel.grid(row=5, column=2, sticky='W')

    admin_button_delete = tk.Button(admin_panel,
                                  text='Obriši')
    admin_button_delete.grid(row=5, column=3, sticky='W')

    names = ['Pero Peric', 'Ana Anic', 'Marko Maric', 'Iva Ivic', 'Vinko Vinic']
    for name in names:
        lbox_names.insert(tk.END, name)
    lbox_names.bind('<ButtonRelease-1>', on_element_clicked)



    main_window.mainloop()
    #endregion






























    #endregion



