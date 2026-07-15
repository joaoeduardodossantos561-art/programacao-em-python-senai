import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


# --- BANCO DE DADOS ---
def conectar():
    conexao = sqlite3.connect("clientes_xyz.db")
    conexao.execute(
        "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, endereco TEXT)"
    )
    return conexao


# --- FUNÇÕES ---
def limpar():
    for entrada in [txt_nome, txt_email, txt_tel, txt_end]:
        entrada.delete(0, tk.END)
    lbl_id.config(text="-")


def listar(busca=""):
    for row in tabela.get_children():
        tabela.delete(row)
    con = conectar()
    cursor = con.cursor()
    if busca:
        cursor.execute(
            "SELECT * FROM clientes WHERE nome LIKE ?", (f"%{busca}%",)
        )
    else:
        cursor.execute("SELECT * FROM clientes")
    for linha in cursor.fetchall():
        tabela.insert("", tk.END, values=linha)
    con.close()


def salvar():
    if not txt_nome.get().strip():
        return messagebox.showwarning("Erro", "Nome é obrigatório!")
    con = conectar()
    id_atual = lbl_id.cget("text")
    if id_atual == "-":
        con.execute(
            "INSERT INTO clientes (nome, email, telefone, endereco) VALUES (?,?,?,?)",
            (txt_nome.get(), txt_email.get(), txt_tel.get(), txt_end.get()),
        )
    else:
        con.execute(
            "UPDATE clientes SET nome=?, email=?, telefone=?, endereco=? WHERE id=?",
            (
                txt_nome.get(),
                txt_email.get(),
                txt_tel.get(),
                txt_end.get(),
                id_atual,
            ),
        )
    con.commit()
    con.close()
    limpar()
    listar()


def excluir():
    id_atual = lbl_id.cget("text")
    if id_atual == "-":
        return messagebox.showwarning("Erro", "Selecione um cliente!")
    if messagebox.askyesno("Confirmar", "Deseja excluir?"):
        con = conectar()
        con.execute("DELETE FROM clientes WHERE id=?", (id_atual,))
        con.commit()
        con.close()
        limpar()
        listar()


def carregar_campos(event):
    item = tabela.selection()
    if item:
        dados = tabela.item(item)["values"]
        limpar()
        lbl_id.config(text=dados[0])
        txt_nome.insert(0, dados[1])
        txt_email.insert(0, dados[2])
        txt_tel.insert(0, dados[3])
        txt_end.insert(0, dados[4])


# --- INTERFACE ---
janela = tk.Tk()
janela.title("XYZ Comércio")
janela.geometry("650x450")

# Campos de texto
tk.Label(janela, text="ID:").grid(row=0, column=0, sticky="w", px=10, py=5)
lbl_id = tk.Label(janela, text="-", font=("Arial", 10, "bold"))
lbl_id.grid(row=0, column=1, sticky="w")

tk.Label(janela, text="Nome:").grid(row=1, column=0, sticky="w", px=10, py=5)
txt_nome = tk.Entry(janela, width=30)
txt_nome.grid(row=1, column=1)

tk.Label(janela, text="E-mail:").grid(row=1, column=2, sticky="w", px=10, py=5)
txt_email = tk.Entry(janela, width=30)
txt_email.grid(row=1, column=3)

tk.Label(janela, text="Telefone:").grid(row=2, column=0, sticky="w", px=10, py=5)
txt_tel = tk.Entry(janela, width=30)
txt_tel.grid(row=2, column=1)

tk.Label(janela, text="Endereço:").grid(
    row=2, column=2, sticky="w", px=10, py=5
)
txt_end = tk.Entry(janela, width=30)
txt_end.grid(row=2, column=3)

# Botões de Ação
frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=3, column=0, columnspan=4, py=10)

tk.Button(frame_botoes, text="Salvar / Atualizar", command=salvar).pack(
    side="left", padx=5
)
tk.Button(frame_botoes, text="Excluir", command=excluir).pack(
    side="left", padx=5
)
tk.Button(frame_botoes, text="Limpar", command=limpar).pack(side="left", padx=5)

# Barra de Busca
frame_busca = tk.Frame(janela)
frame_busca.grid(row=4, column=0, columnspan=4, py=5)
txt_busca = tk.Entry(frame_busca, width=30)
txt_busca.pack(side="left", padx=5)
tk.Button(
    frame_busca, text="Buscar", command=lambda: listar(txt_busca.get())
).pack(side="left")
tk.Button(frame_busca, text="Ver Todos", command=lambda: listar()).pack(
    side="left", padx=5
)

# Tabela
tabela = ttk.Treeview(
    janela,
    columns=("ID", "Nome", "E-mail", "Telefone", "Endereço"),
    show="headings",
    height=8,
)
for col, tam in zip(
    ["ID", "Nome", "E-mail", "Telefone", "Endereço"], [40, 150, 150, 100, 150]
):
    tabela.heading(col, text=col)
    tabela.column(col, width=tam)
tabela.grid(row=5, column=0, columnspan=4, padx=10, pady=5)
tabela.bind("<<TreeviewSelect>>", carregar_campos)

listar()
janela.mainloop()


