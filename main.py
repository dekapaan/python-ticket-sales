from tkinter import *
from tkinter import messagebox


class TicketSales:
    def __init__(self, master):
        # Initialise window
        self.master = master
        self.master.title('TicketSales')
        self.master.geometry('400x450')
        self.master.config(bg='#191923')

        # Cell number label and entry
        self.cell_entry_lable = Label(self.master, text='Enter CellNumber:', bg='#191923', fg='#BDBF09', font="monospace 10")
        self.cell_entry = Entry(self.master, bg='#BDBF09', fg='#191923', font="monospace 10")
        self.cell_entry_lable.place(x=10, y=10)
        self.cell_entry.place(x=220, y=10)

        # Ticket type label and option box for ticket type
        self.ticket_label = Label(self.master, text='Select Ticket Category:', bg='#191923', fg='#BDBF09', font="monospace 10")
        self.options = ['Soccer', 'Movie', 'Theater']
        self.variable = StringVar()
        self.variable.set('Select Ticket')
        self.ticket_op = OptionMenu(master, self.variable, *self.options)
        self.ticket_op.config(font="monospace 10")
        menu = self.master.nametowidget(self.ticket_op.menuname)
        menu.config(font='monospace 10')
        self.ticket_label.place(x=10, y=50)
        self.ticket_op.place(x=220, y=45)

        # Ticket number label and ticket number spinbox
        self.ticket_no_label = Label(self.master, text='Number of Tickets Bought:', bg='#191923', fg='#BDBF09', font="monospace 10")
        self.ticket_spinbox = Spinbox(self.master, width=10, from_=0, to=100, bg='#BDBF09', fg='#191923', font="monospace 10")
        self.ticket_no_label.place(x=10, y=90)
        self.ticket_spinbox.place(x=220, y=90)

        # Calculate button
        self.calc_button = Button(self.master, text='Calculate Ticket', command=self.calc_prepayment, font="monospace 10")
        self.clear_button = Button(self.master, text='Clear Entries', command=self.clear, font="monospace 10")
        self.calc_button.place(x=40, y=180)
        self.clear_button.place(x=225, y=180)

        # Payment info frame
        self.frame = Frame(self.master, width=318, height=180, bg='#BDBF09')
        self.frame.place(x=40, y=230)

        # Payment info
        self.amount_pay = Label(self.frame, text='', fg='#191923', bg='#BDBF09', font="monospace 10")
        self.reserve = Label(self.frame, text='', fg='#191923', bg='#BDBF09', font="monospace 10")
        self.cell_label = Label(self.frame, text='', fg='#191923', bg='#BDBF09', font="monospace 10")
        self.amount_pay.place(x=10, y=30)
        self.reserve.place(x=10, y=70)
        self.cell_label.place(x=10, y=110)

    def calc_prepayment(self):
        # Initialise variables and constants
        ticket_no = int(self.ticket_spinbox.get())
        vat = 0.14

        # If try fails, traps error and shows ValueError messagebox
        try:
            int(self.cell_entry.get())  # To check if cell no is not float or string
            if len(self.cell_entry.get()) < 10 or len(self.cell_entry.get()) > 10:
                raise ValueError  # raise ValueError if cell number is </> than 10 digits

            elif self.variable.get() == 'Select Ticket':
                raise ValueError  # If ticket type not selected, ValueError raised

            elif ticket_no == 0:
                raise ValueError  # If spinbox value == 0, raise ValueError

            # Soccer type calculation total price calculation
            elif self.variable.get() == 'Soccer':
                price = 40  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ('Amount Payable: R{}'.format(price_pay))
                self.amount_pay.config(text=text)

            # Movie type total price calculation
            elif self.variable.get() == 'Movie':
                price = 75  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ('Amount Payable: R{}'.format(price_pay))
                self.amount_pay.config(text=text)

            # Theater type total price calculation
            elif self.variable.get() == 'Theater':
                price = 100  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ('Amount Payable: R{}'.format(price_pay))
                self.amount_pay.config(text=text)

            # Displaying amount payable, reservation and cell number
            reserve_text = 'Reservation for {} for {}'.format(self.variable.get(), ticket_no)
            cell_text = 'was done by {}'.format(self.cell_entry.get())
            self.reserve.config(text=reserve_text)
            self.cell_label.config(text=cell_text)

        except ValueError:
            messagebox.showerror(message='Invalid combination')

    # Clear all entry fields
    def clear(self):
        self.cell_entry.delete(0, END)
        self.cell_entry.focus()
        self.variable.set('Select Ticket')
        self.ticket_spinbox.delete(0, END)
        self.ticket_spinbox.insert(0, 0)
        self.amount_pay.config(text='')
        self.reserve.config(text='')
        self.cell_label.config(text='')


root = Tk()
TicketSales(root)   # Instance of class
root.mainloop()
