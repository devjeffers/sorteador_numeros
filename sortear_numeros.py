import tkinter as tk
from tkinter import messagebox
import random

class SorteadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorteador de Números")
        self.root.geometry("300x250")
        self.root.resizable(False, False)

        self.numeros_disponiveis = list(range(1, 150))
        self.sorteados = []

        self.label = tk.Label(root, text="Clique para sortear", font=("Arial", 14))
        self.label.pack(pady=20)

        self.botao_sortear = tk.Button(root, text="Sortear Número", command=self.sortear_numero, font=("Arial", 12))
        self.botao_sortear.pack(pady=10)

        self.resultado = tk.Label(root, text="", font=("Arial", 20, "bold"), fg="blue")
        self.resultado.pack(pady=10)

        self.botao_resetar = tk.Button(root, text="Resetar", command=self.resetar, font=("Arial", 10), fg="red")
        self.botao_resetar.pack(pady=5)

    def sortear_numero(self):
        if not self.numeros_disponiveis:
            messagebox.showinfo("Fim", "Todos os números já foram sorteados!")
            return

        numero = random.choice(self.numeros_disponiveis)
        self.numeros_disponiveis.remove(numero)
        self.sorteados.append(numero)
        self.resultado.config(text=str(numero))

    def resetar(self):
        confirmar = messagebox.askyesno("Resetar", "Deseja realmente reiniciar o sorteio?")
        if confirmar:
            self.numeros_disponiveis = list(range(1, 150))
            self.sorteados.clear()
            self.resultado.config(text="")
            self.label.config(text="Clique para sortear")


if __name__ == "__main__":
    root = tk.Tk()
    app = SorteadorApp(root)
    root.mainloop()
