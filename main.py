import tkinter as tk

class PaginaPrincipal(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(bg="pink", width=300, height=300)
        self.pack_propagate(0)

        self.label = tk.Label(self, text="Feliz Dia dos Namorados!", font=("Arial", 16), bg="pink")
        self.label.pack(pady=50)

        self.botao = tk.Button(self, text="Abrir Carta", command=self.abrir_carta)
        self.botao.pack()

    def abrir_carta(self):
        self.master.switch_frame(CartaPage)

class CartaPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(bg="lightblue", width=300, height=300)
        self.pack_propagate(0)

        self.label = tk.Label(self, text="Querido(a),\n\nFeliz Dia dos Namorados!\n\nCom amor,\nSeu Nome", font=("Arial", 12), bg="lightblue")
        self.label.pack(pady=50)

        self.botao = tk.Button(self, text="Voltar", command=self.voltar_pagina)
        self.botao.pack()

    def voltar_pagina(self):
        self.master.switch_frame(PaginaPrincipal)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dia dos Namorados")
        self.geometry("300x300")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        self.create_frames()

        self.show_frame(PaginaPrincipal)

    def create_frames(self):
        for F in (PaginaPrincipal, CartaPage):
            frame = F(self.container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def switch_frame(self, frame_class):
        new_frame = self.frames[frame_class]
        new_frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
