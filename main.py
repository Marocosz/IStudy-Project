from customtkinter import *

window = CTk(fg_color='#0E1F0D')


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
        self.window.geometry(f'{largura//2}x{altura//2}')
        self.window.resizable(True, True)
        self,window.minsize(width=largura//2, height=altura//2)

    def frames(self):
        self.frame1 = CTkFrame(self.window)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.08)

        self.frame2 = CTkFrame(self.window)
        self.frame2.place(relx=0.02, rely=0.12, relwidth=0.47, relheight=0.86)

        self.frame3 = CTkFrame(self.window)
        self.frame3.place(relx=0.51, rely=0.12, relwidth=0.47, relheight=0.86)

    def buttons(self):
        self.bt_limpar = CTkButton(self.frame1, text='Limpar')
        self.bt_limpar.place(relx=0.01, rely=0.125, relwidth=0.10, relheight=0.75)

        self.bt_buscar = CTkButton(self.frame1, text='Buscar')
        self.bt_buscar.place(relx=0.12, rely=0.125, relwidth=0.10, relheight=0.75)

        self.bt_buscar = CTkButton(self.frame1, text='Buscar')
        self.bt_buscar.place(relx=0.23, rely=0.125, relwidth=0.10, relheight=0.75)

        self.bt_buscar = CTkButton(self.frame1, text='Buscar')
        self.bt_buscar.place(relx=0.34, rely=0.125, relwidth=0.10, relheight=0.75)

        self.bt_buscar = CTkButton(self.frame1, text='Buscar')
        self.bt_buscar.place(relx=0.45, rely=0.125, relwidth=0.10, relheight=0.75)

        self.bt_buscar = CTkButton(self.frame1, text='Buscar')
        self.bt_buscar.place(relx=0.56, rely=0.125, relwidth=0.10, relheight=0.75)

        self.bt_buscar = CTkButton(self.frame1, text='Buscar')
        self.bt_buscar.place(relx=0.67, rely=0.125, relwidth=0.10, relheight=0.75)

        self.bt_buscar = CTkButton(self.frame1, text='Buscar')
        self.bt_buscar.place(relx=0.78, rely=0.125, relwidth=0.10, relheight=0.75)

        self.bt_buscar = CTkButton(self.frame1, text='Buscar')
        self.bt_buscar.place(relx=0.89, rely=0.125, relwidth=0.10, relheight=0.75)






Application()