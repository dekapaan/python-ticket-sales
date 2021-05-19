from tkinter import *
from tkinter import messagebox


class TicketSales(object):
    def __init__(self, master):
        # Initialise window
        self.master = master
        self.master.title('TicketSales')
        self.master.geometry('400x450')

        # Cell number label and entry
        self.cell_entry_lable = Label(self.master, text='Enter CellNumber:')
        self.cell_entry = Entry(self.master)
        self.cell_entry_lable.place(x=10, y=10)
        self.cell_entry.place(x=200, y=10)

        self.ticket_label = Label(self.master, text='Select Ticket Category:')
        self.options = ['Soccer', 'Movie', 'Theater']
        self.variable = StringVar(self.master)
        self.variable.set('Select Ticket')
        self.ticket_op = OptionMenu(master, self.variable, *self.options)
        self.ticket_label.place(x=10, y=50)
        self.ticket_op.place(x=200, y=45)

        self.ticket_no_label = Label(self.master, text='Number of Tickets Bought:')
        self.ticket_spinbox = Spinbox(self.master, width=10, from_=0, to=100)
        self.ticket_no_label.place(x=10, y=90)
        self.ticket_spinbox.place(x=200, y=90)

        self.calc_button = Button(self.master, text='Calculate Ticket', command=self.calc_prepayment)
        self.clear_button = Button(self.master, text='Clear Entries', command=self.clear)
        self.calc_button.place(x=70, y=180)
        self.clear_button.place(x=230, y=180)

        self.border1 = Label(self.master, text='---------------------------------------------------------------')
        self.border2 = Label(self.master, text='---------------------------------------------------------------')
        self.border1.place(x=40, y=220)
        self.border2.place(x=40, y=380)

        self.amount_pay = Label(self.master, text='')
        self.reserve = Label(self.master, text='')
        self.cell_label = Label(self.master, text='')
        self.amount_pay.place(x=50, y=260)
        self.reserve.place(x=50, y=300)
        self.cell_label.place(x=50, y=340)

    def calc_prepayment(self):
        ticket_no = int(self.ticket_spinbox.get())
        vat = 0.14
        try:
            int(self.cell_entry.get())
            if len(self.cell_entry.get()) < 10 or len(self.cell_entry.get()) > 10:
                raise ValueError

            elif self.variable.get() == 'Select Ticket':
                raise ValueError

            elif int(self.ticket_spinbox.get()) == 0:
                raise ValueError

            elif self.variable.get() == 'Soccer':
                price = 40  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ('Amount Payable: R{}'.format(price_pay))
                self.amount_pay.config(text=text)

            elif self.variable.get() == 'Movie':
                price = 75  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ('Amount Payable: R{}'.format(price_pay))
                self.amount_pay.config(text=text)

            elif self.variable.get() == 'Theater':
                price = 100  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ('Amount Payable: R{}'.format(price_pay))
                self.amount_pay.config(text=text)

            reserve_text = 'Reservation for {} for {}'.format(self.variable.get(), ticket_no)
            cell_text = 'was done by {}'.format(self.cell_entry.get())
            self.reserve.config(text=reserve_text)
            self.cell_label.config(text=cell_text)

        except ValueError:
            messagebox.showerror(message='Invalid combination')

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
TicketSales(root)
root.mainloop()
