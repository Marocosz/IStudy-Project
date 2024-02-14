from tkinter import *

window = Tk()


class Application():
    def __init__(self):
        self.window = window
        self.window_config()
        self.frames()
        self.buttons()
        window.mainloop()


    def window_config(self):
        largura = window.winfo_screenwidth()
        altura = window.winfo_screenheight()

        self.window.title("IStudy")
        self.window.configure(background='#84A0EB')
        self.window.geometry(f'{largura//2}x{altura//2}')
        self.window.resizable(True, True)
        self,window.minsize(width=largura//2, height=altura//2)

    def frames(self):
        self.frame1 = Frame(self.window, bg='#D2D8EB')
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.46, relheight=0.96)

        self.frame2 = Frame(self.window, bg='#D2D8EB')
        self.frame2.place(relx=0.50, rely=0.02, relwidth=0.48, relheight=0.96)

    def buttons(self):
        self.bt_limpar = Button(self.frame1, bg='#8983EB', text='Limpar')
        self.bt_limpar.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.2)

        self.bt_buscar = Button(self.frame1, bg='#8983EB', text='Buscar')
        self.bt_buscar.place(relx=0.02, rely=0.24, relwidth=0.96, relheight=0.2)







Application()