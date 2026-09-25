import tkinter as tk
from tkinter import scrolledtext
from classificador import classificador

def ao_clicar():
    texto = caixa_texto.get("1.0", "end").lower()
    encontradas = classificador(texto)

    if encontradas:
        mensagem = f"⚠️ Encontramos: {', '.join(encontradas)}"
    else:
        mensagem = "✅ Nenhum dado sensível encontrado!"

    resultado.config(text=mensagem)

# Cria a janela principal
janela = tk.Tk()
janela.title("🛡️ Analisador de Dados LGPD")
janela.geometry("600x500")

# Instrução
tk.Label(janela, text="Cole seu texto abaixo:").pack(pady=10)

# Caixa de texto
caixa_texto = scrolledtext.ScrolledText(janela, width=60, height=10)
caixa_texto.pack(pady=5)

# Botão
tk.Button(janela, text="Analisar", command=ao_clicar).pack(pady=10)

# Resultado
resultado = tk.Label(janela, text="", wraplength=500, justify="left")
resultado.pack(pady=10)

# Mantém a janela aberta
janela.mainloop()