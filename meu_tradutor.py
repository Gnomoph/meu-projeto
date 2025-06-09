import tkinter as tk
from tkinter import ttk, messagebox

# Dicionário de tradução inicial
dicionario = {
    "olá": {"en": "hello", "es": "hola", "fr": "bonjour", "de": "hallo"},
    "mundo": {"en": "world", "es": "mundo", "fr": "monde", "de": "welt"},
    "bom": {"en": "good", "es": "bueno", "fr": "bon", "de": "gut"},
    "dia": {"en": "day", "es": "día", "fr": "jour", "de": "tag"},
    "noite": {"en": "night", "es": "noche", "fr": "nuit", "de": "nacht"}
}

# Função de tradução
def traduzir():
    texto_original = entrada_texto.get("1.0", tk.END).strip().lower()
    idioma_destino = combo_idioma.get()

    codigos = {"Inglês": "en", "Espanhol": "es", "Francês": "fr", "Alemão": "de"}
    codigo_idioma = codigos.get(idioma_destino, "en")

    palavras = texto_original.split()
    traducao = []

    for palavra in palavras:
        if palavra in dicionario:
            traducao.append(dicionario[palavra][codigo_idioma])
        else:
            traducao.append(f"[{palavra}]")  # Palavra desconhecida

    texto_traduzido.delete("1.0", tk.END)
    texto_traduzido.insert(tk.END, " ".join(traducao))

# Função para adicionar nova palavra ao dicionário
def abrir_janela_adicao():
    janela_adicao = tk.Toplevel(janela)
    janela_adicao.title("Adicionar Nova Palavra")
    janela_adicao.geometry("300x300")
    janela_adicao.configure(bg="#2b2b2b")

    def salvar_palavra():
        pt = entrada_pt.get().strip().lower()
        en = entrada_en.get().strip().lower()
        es = entrada_es.get().strip().lower()
        fr = entrada_fr.get().strip().lower()
        de = entrada_de.get().strip().lower()

        if not pt or not en or not es or not fr or not de:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
            return

        dicionario[pt] = {"en": en, "es": es, "fr": fr, "de": de}
        messagebox.showinfo("Sucesso", f'Palavra "{pt}" adicionada com sucesso!')
        janela_adicao.destroy()

    campos = [("Português", "entrada_pt"), ("Inglês", "entrada_en"), ("Espanhol", "entrada_es"),
              ("Francês", "entrada_fr"), ("Alemão", "entrada_de")]
    entradas = {}

    for texto, var in campos:
        ttk.Label(janela_adicao, text=texto + ":", background="#2b2b2b", foreground="white").pack(pady=(5, 0))
        entrada = ttk.Entry(janela_adicao)
        entrada.pack(pady=2, fill="x", padx=10)
        entradas[var] = entrada

    entrada_pt = entradas["entrada_pt"]
    entrada_en = entradas["entrada_en"]
    entrada_es = entradas["entrada_es"]
    entrada_fr = entradas["entrada_fr"]
    entrada_de = entradas["entrada_de"]

    ttk.Button(janela_adicao, text="Salvar", command=salvar_palavra).pack(pady=10)

# Janela principal
janela = tk.Tk()
janela.title("Tradutor de Texto")
janela.geometry("450x550")
janela.configure(bg="#1e1e1e")

# Estilo escuro
style = ttk.Style(janela)
style.theme_use("default")

style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 10))
style.configure("TButton", background="#333333", foreground="white", font=("Segoe UI", 10), padding=6)
style.map("TButton", background=[("active", "#555555")], foreground=[("active", "white")])
style.configure("TCombobox", fieldbackground="#2e2e2e", background="#2e2e2e", foreground="white", arrowcolor="white")

# Entrada de texto
ttk.Label(janela, text="Texto para traduzir:").pack(pady=(10, 0))
entrada_texto = tk.Text(janela, height=5, bg="#2d2d2d", fg="#ffffff", insertbackground="white", font=("Segoe UI", 10))
entrada_texto.pack(padx=10, pady=5, fill="x")

# Idioma de destino
ttk.Label(janela, text="Selecionar idioma de destino:").pack(pady=(10, 0))
combo_idioma = ttk.Combobox(janela, values=["Inglês", "Espanhol", "Francês", "Alemão"], font=("Segoe UI", 10))
combo_idioma.set("Inglês")
combo_idioma.pack(padx=10, pady=5, fill="x")

# Botões
ttk.Button(janela, text="Traduzir", command=traduzir).pack(pady=10)
ttk.Button(janela, text="Adicionar nova palavra", command=abrir_janela_adicao).pack(pady=5)

# Resultado da tradução
ttk.Label(janela, text="Texto traduzido:").pack(pady=(10, 0))
texto_traduzido = tk.Text(janela, height=5, bg="#2d2d2d", fg="#ffffff", insertbackground="white", font=("Segoe UI", 10))
texto_traduzido.pack(padx=10, pady=5, fill="x")

janela.mainloop()
