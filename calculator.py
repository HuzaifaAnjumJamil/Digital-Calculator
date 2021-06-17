from tkinter import*

# Created Main class for Calculator


class Application(Frame):

    """Initialize the Frame """

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.tasks = " "
        self.UserIn = StringVar()
        self.grid()
        self.create_widget()

    def create_widget(self):
        """Buttons for Calculator"""

        self.user_input = Entry(self, bg="#5BC8AC", bd=29,
                                insertwidth=4, width=24,
                                font=("Verdana", 20, "bold"), textvariable=self.UserIn, justify=RIGHT)
        self.user_input.grid(columnspan=4)

        self.user_input.insert(0, "0")

        # Button for value 0
        self.button9 = Button(self, bg="#98DBC6", bd=12,
                              text="0",  padx=33, pady=25,
                              command=lambda: self.buttonClick(0), font=("Helvetica", 20, "bold"))
        self.button9.grid(row=5, column=0, sticky=W)

        # Button for value 1
        self.button7 = Button(self, bg="#98DBC6", bd=12,
                              text="1",  padx=33, pady=25,
                              command=lambda: self.buttonClick(1), font=("Helvetica", 20, "bold"))
        self.button7.grid(row=4, column=0, sticky=W)

       # Button for value 2
        self.button8 = Button(self, bg="#98DBC6", bd=12,
                              text="2",  padx=35, pady=25,
                              command=lambda: self.buttonClick(2), font=("Helvetica", 20, "bold"))
        self.button8.grid(row=4, column=1, sticky=W)

        # Button for value 3
        self.button9 = Button(self, bg="#98DBC6", bd=12,
                              text="3",  padx=33, pady=25,
                              command=lambda: self.buttonClick(3), font=("Helvetica", 20, "bold"))
        self.button9.grid(row=4, column=2, sticky=W)

        # Button for value 4
        self.button4 = Button(self, bg="#98DBC6", bd=12,
                              text="4",  padx=33, pady=25,
                              command=lambda: self.buttonClick(4), font=("Helvetica", 20, "bold"))
        self.button4.grid(row=3, column=0, sticky=W)

        # Button for value 5
        self.button5 = Button(self, bg="#98DBC6", bd=12,
                              text="5",  padx=35, pady=25,
                              command=lambda: self.buttonClick(5), font=("Helvetica", 20, "bold"))
        self.button5.grid(row=3, column=1, sticky=W)
