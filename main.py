from customtkinter import *

window = CTk()
window._set_appearance_mode('dark')


class Application():
    def __init__(self):
        self.window = window
        self.window_config()
        self.tab1()
        #self.frames()
        #self.widgets_frame1()
        self.window.mainloop()


    def window_config(self):
        largura = window.winfo_screenwidth()
        altura = window.winfo_screenheight()

        self.window.title("IStudy")
        self.window.geometry(f'1000x600')
        self.window.resizable(False, False)

    def tab1(self):
        self.tab1 = CTkFrame(self.window, width=960, height=80)
        self.tab1.place(x=20, y=20)

    def frames(self):
        self.frame1 = CTkFrame(self.window)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.08)

        self.frame2 = CTkFrame(self.window)
        self.frame2.place(relx=0.02, rely=0.12, relwidth=0.47, relheight=0.86)

        self.frame3 = CTkFrame(self.window)
        self.frame3.place(relx=0.51, rely=0.12, relwidth=0.47, relheight=0.86)

    def widgets_frame1(self):
        self.bt_limpar = CTkButton(self.frame1, text='Limpar')
        self.bt_limpar.place(relx=0.01, rely=0.125, relwidth=0.1, relheight=0.75)

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