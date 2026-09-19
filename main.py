import customtkinter
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD


class App(customtkinter.CTk, TkinterDnD.DnDWrapper):

    def __init__(self):
        super().__init__()

        self.TkdndVersion = TkinterDnD._require(self)

        self.geometry("700x500")
        self.maxsize(700, 500)
        self.minsize(350, 250)

        self.title("Arquinivete")
        self.iconbitmap(
            self._resource_path("icons/fileSearchIcon/web/favicon.ico")
        )

        self.button = customtkinter.CTkButton(
            self,
            text="my button",
            command=self.button_callbck
        )
        self.button.pack(padx=20, pady=20)

        self.drop_area = customtkinter.CTkFrame(self)
        self.drop_area.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.label = customtkinter.CTkLabel(
            self.drop_area,
            text="Clique para selecionar ou arraste um arquivo aqui"
        )
        self.label.pack(expand=True)

        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind(
            "<<Drop>>",
            self.arquivo_arrastado
        )

        self.drop_area.bind(
            "<Button-1>",
            lambda event: self.selecionar_arquivo()
        )

    def _resource_path(self, relative_path):
        import sys
        import os

        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative_path)

        return os.path.join(
            os.path.abspath("."),
            relative_path
        )

    def button_callbck(self):
        if customtkinter.get_appearance_mode().lower() == "dark":
            customtkinter.set_appearance_mode("light")
        else:
            customtkinter.set_appearance_mode("dark")

    def selecionar_arquivo(self):
        arquivo = filedialog.askopenfilename()

        if arquivo:
            self.processar_arquivo(arquivo)

    def arquivo_arrastado(self, event):
        arquivos = self.tk.splitlist(event.data)

        for arquivo in arquivos:
            self.processar_arquivo(arquivo)

    def processar_arquivo(self, arquivo):
        print("Arquivo:", arquivo)


app = App()
app.mainloop()