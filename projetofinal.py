from tkinter import *
from tkinter import messagebox
import mysql.connector 
from time import *
from tkinter import ttk



conexao_banco = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "restaurante"
) 

tema = "#EEEEEE"
tema_text = "#242424"
 
cursor = conexao_banco.cursor()

def entrarADM():
  usuario = usuario_id_entrada1.get()
  senha = senha_entrada1.get()
  if senha != "" or usuario != "": 
    id = f'SELECT * FROM funcionarios WHERE id={usuario}'
    cursor.execute(id)
    select = cursor.fetchall()
    if len(select) > 0:
      if senha == "1111" and select[0][2] == "administrador":
        usuario_id_entrada1.delete(0, END)
        senha_entrada1.delete(0, END)
        frame_adm.pack_forget()
        frameADM.pack(expand=True)
      else:
        messagebox.showwarning(title = "ERR0", message= "Senha Inválida ou Cargo inválido!!")
    else:
      messagebox.showwarning(title = "ERR0", message= "ID não castrado")
  else:
    messagebox.showwarning(title = "ERR0", message= "Preencha os campos corretamente")

def entrarGARCOM(): 
  usuario = usuario_id_entrada2.get()
  senha = senha_entrada2.get()
  if senha != "" or usuario != "": 
    id = f'SELECT * FROM funcionarios WHERE id={usuario}'
    cursor.execute(id)
    select = cursor.fetchall()
    if len(select) > 0:
      if senha == "2222" and select[0][2] == "garçom":
        frame_garcom.pack_forget()
        frameGARCOM.pack(expand=True)
      else:
        messagebox.showwarning(title = "ERR0", message= "Senha Inválida ou Cargo inválido!!")
    else:
      messagebox.showwarning(title = "ERR0", message= "ID não castrado")
  else:
    messagebox.showwarning(title = "ERR0", message= "Preencha os campos corretamente")

def entrarCOZINHEIRO():
  usuario = usuario_id_entrada3.get()
  senha = senha_entrada3.get()
  if senha != "" or usuario != "": 
    id = f'SELECT * FROM funcionarios WHERE id={usuario}'
    cursor.execute(id)
    select = cursor.fetchall()
    if len(select) > 0:
      if senha == "3333" and select[0][2] == "cozinheiro":
        frame_cozinheiro.pack_forget()
        cozinheiro_MENU.pack(expand=True)
      else:
        messagebox.showwarning(title = "ERR0", message= "Senha Inválida ou Cargo inválido!!")
    else:
      messagebox.showwarning(title = "ERR0", message= "ID não castrado")
  else:
    messagebox.showwarning(title = "ERR0", message= "Preencha os campos corretamente")

def entrarRECEPCIONISTA():
  usuario = usuario_id_entrada4.get()
  senha = senha_entrada4.get()
  if senha != "" or usuario != "": 
    id = f'SELECT * FROM funcionarios WHERE id={usuario}'
    cursor.execute(id)
    select = cursor.fetchall()
    if len(select) > 0:
      if senha == "4444" and select[0][2] == "recepcionista":
        frame_recepcionista.pack_forget()
        frame_recepcionsta_menu.pack(expand=True)
      else:
        messagebox.showwarning(title = "ERR0", message= "Senha ou Cargo inválido!")
    else:
      messagebox.showwarning(title = "ERR0", message= "ID não castrado")
  else:
    messagebox.showwarning(title = "ERR0", message= "Preencha os campos corretamente")

def adm():
  homep.pack_forget()
  frame_adm.pack(expand=True) 

def garcom():
  homep.pack_forget()
  frame_garcom.pack(expand=True)

def cozinheiro():
  homep.pack_forget()
  frame_cozinheiro.pack(expand=True)

def recepcionista():
  homep.pack_forget()
  frame_recepcionista.pack(expand=True)

def voltar_adm():
  usuario_id_entrada1.delete(0, END) 
  senha_entrada1.delete(0, END)  
  frame_adm.pack_forget()
  homep.pack(expand=True)

def voltar_garcom():
  frame_garcom.pack_forget()
  homep.pack(expand=True)

def voltar_cozinheiro():
  frame_cozinheiro.pack_forget()
  homep.pack(expand=True)

def voltar_recepcionista():
  frame_recepcionista.pack_forget()
  homep.pack(expand=True)

def voltar_pedido_menu():
  frameADM.pack_forget() 
  frameGARCOM.pack_forget()
  homep.pack(expand=True)

def voltar_adm_menu():
  frameADM.pack_forget()
  cozinheiro_MENU.pack_forget()
  homep.pack(expand=True)

def adicionar_pedido():
  frameADM.pack_forget()
  frameGARCOM.pack_forget()
  adicionar_p.pack(expand=True)

def alterar_pedido():
  frameADM.pack_forget()
  frameGARCOM.pack_forget()
  alterar_p.pack(expand=True)

def excluir_pedido():
  frameGARCOM.pack_forget()
  excluir_p.pack(expand=True)

def alterar_mesa():
  frameGARCOM.pack_forget()
  alterar_m.pack(expand=True)

def cozinheiro_alterar_status_pedido():
  cozinheiro_MENU.pack_forget()
  status_pedido_coz.pack(expand=True)

def pesquisar_pedido():
  frameADM.pack_forget()
  cozinheiro_MENU.pack_forget()
  pesquisa_pedido.pack(expand= True)

def voltar_coz_menu():
  frame_arvore_pratos.pack_forget()
  frame_arvore_em_preparo.pack_forget()
  frame_arvore_status.pack_forget()
  frame_arvore_total.pack_forget()
  cozinheiro_MENU.pack(expand=True)

def voltar_rec_menu():
  frame_recepcionsta_menu.pack_forget()
  frame_arvore_mesa_pesq.pack_forget()
  frame_recepcionsta_menu.pack(expand=True)

def voltar_para_menu_depois_do_rec():
  frame_recepcionsta_menu.pack_forget()
  homep.pack(expand=True)

def pesquisar_tabela_status():
  frame_recepcionsta_menu.pack_forget()
  pesquisa_pedido.pack_forget()
  frame_status_coz.pack(expand=True)

def ir_pratos():
  pesquisa_pedido.pack_forget()
  frame_pratos.pack(expand= True)

def ir_status_mesa():
  frame_recepcionsta_menu.pack_forget()
  frame_status_mesa.pack(expand=True)

def alterar_mesa_disponivel():
  id = id_pedido_entry_mesa.get()
  if id != "":
    cursor.execute(f'SELECT * FROM mesas WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Não possui esta mesa no sistema!")
    else:
      cursor.execute(f'UPDATE mesas SET disponibilidade = "DISPONIVEL" WHERE id = {id}')
      conexao_banco.commit()
      id_pedido_entry_mesa.delete(0, END)
      frame_status_mesa.pack_forget()
      frame_recepcionsta_menu.pack(expand=True)

def alterar_mesa_indisponivel():
  id = id_pedido_entry_mesa.get()
  if id != "":
    cursor.execute(f'SELECT * FROM mesas WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Não possui esta mesa no sistema!")
    else:
      cursor.execute(f'UPDATE mesas SET disponibilidade = "INDISPONIVEL" WHERE id = {id}')
      conexao_banco.commit()
      id_pedido_entry_mesa.delete(0, END)
      frame_status_mesa.pack_forget()
      frame_recepcionsta_menu.pack(expand=True)

def ir_pesquisar_mesa_la():
  frame_recepcionsta_menu.pack_forget()
  frame_pesquisar_mesa.pack(expand=True)

def pesq_mesa():
  mesa = id_pedido_entry_mesa_pesquisa.get()
  if mesa != "":
    cursor.execute(f'SELECT * FROM mesas WHERE id = {mesa}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Não possui esta mesa no sistema!")
    else:
      cursor.execute(f'SELECT * FROM mesas WHERE id = {mesa}')
      dados = cursor.fetchall()
      id_pedido_entry_mesa_pesquisa.delete(0, END)
      frame_pesquisar_mesa.pack_forget()
      frame_arvore_mesa_pesq.pack(expand=True)
      for x in treeeeee.get_children():
        treeeeee.delete(x)
        
      for y in dados:
        treeeeee.insert("", "end", values=y)
      
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")

def alteracao_status():
  id = id_pedido_entry_coz.get()
  if id != "":
    cursor.execute(f'SELECT * FROM pedidos WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Não possui nada com esse ID!")
    else:
      cursor.execute(f'UPDATE pedidos SET status = "PRONTO" WHERE id = {id}')
      conexao_banco.commit()
      id_pedido_entry_coz.delete(0, END)
      status_pedido_coz.pack_forget()
      cozinheiro_MENU.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")

def limpar_pedidos():
  id_pedido_entrada.delete(0, END)
  pratos_pedido_entrada.delete(0,END)
  observacoes_pedido_entrada.delete(0,END)

def adicionar_pedidu():
  id = id_pedido_entrada.get()
  pratos = pratos_pedido_entrada.get()
  observacoes = observacoes_pedido_entrada.get()
  if id != "" or pratos != "":
    cursor.execute(f'SELECT * FROM pedidos WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) > 0:
      messagebox.showwarning(title = "ERR0", message= "Já possui algo com esse ID!")
    else:
      horario_atual = strftime("%H:%M:%S", localtime())
      cursor.execute(f'INSERT INTO PEDIDOS(id, horario, status, pratos, observacoes) VALUES({id},"{horario_atual}","EM PREPARO", "{pratos}", "{observacoes}")')
      conexao_banco.commit()
      limpar_pedidos()
      adicionar_p.pack_forget()
      frameGARCOM.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")

def alterar_pedidu():
  id = id_pedido_alterar_garcom.get()
  pratos = pratos_pedido_alterar_entry.get()
  observacoes = observacoes_pedido_alterar_entry.get()
  if id != "" or pratos != "":
    cursor.execute(f'SELECT * FROM pedidos WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Não possui nada com esse ID!")
    else:
      cursor.execute(f'UPDATE pedidos SET pratos = "{pratos}", observacoes = "{observacoes}" WHERE id = {id}')
      conexao_banco.commit()
      id_pedido_alterar_garcom.delete(0, END)
      pratos_pedido_alterar_entry.delete(0,END)
      observacoes_pedido_alterar_entry.delete(0,END)
      alterar_p.pack_forget()
      frameGARCOM.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")

def excluir_pedidu():
  id = id_pedido_excluir_garcom.get()
  if id != "":
    cursor.execute(f'SELECT * FROM pedidos WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Não possui nada com esse ID!")
    else:
      cursor.execute(f'DELETE FROM pedidos WHERE id = {id}')
      conexao_banco.commit()
      id_pedido_excluir_garcom.delete(0, END)
      excluir_p.pack_forget()
      frameGARCOM.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")

def alterar_disponivel():
  id = id_mesa_entry.get()
  if id != "":
    cursor.execute(f'SELECT * FROM mesas WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Não possui nada com esse ID!")
    else:
      cursor.execute(f'UPDATE mesas SET disponibilidade = "DISPONIVEL" WHERE id = {id}')
      conexao_banco.commit()
      id_mesa_entry.delete(0, END)
      alterar_m.pack_forget()
      frameGARCOM.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")

def alterar_indisponivel():
  id = id_mesa_entry.get()
  if id != "":
    cursor.execute(f'SELECT * FROM mesas WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Não possui nada com esse ID!")
    else:
      cursor.execute(f'UPDATE mesas SET disponibilidade = "INDISPONIVEL" WHERE id = {id}')
      conexao_banco.commit()
      id_mesa_entry.delete(0, END)
      alterar_m.pack_forget()
      frameGARCOM.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")

def tudo_pesq_tabela():

  cursor.execute(f'SELECT * FROM pedidos')
  dados = cursor.fetchall()

  for x in treee.get_children():
    tree.delete(x)
    
  for y in dados:
    treee.insert("", "end", values=y)
  pesquisa_pedido.pack_forget()
  frame_arvore_total.pack(expand=True)

def status_pesq_tabela_pronto():
  cursor.execute(f'SELECT * FROM pedidos WHERE status = "PRONTO"')
  dados = cursor.fetchall()
  for x in tree.get_children():
        tree.delete(x)
    
  for y in dados:
      tree.insert("", "end", values=y)
  frame_status_coz.pack_forget()
  frame_arvore_status.pack(expand=True)

def status_pesq_tabela_em_preparo():
  cursor.execute(f'SELECT * FROM pedidos WHERE status = "EM PREPARO"')
  dados = cursor.fetchall()
  for x in treeee.get_children():
        tree.delete(x)
    
  for y in dados:
      treeee.insert("", "end", values=y)
  frame_status_coz.pack_forget()
  frame_arvore_em_preparo.pack(expand=True)

def verificar_id_prato():
  prato = id_pedido_entry_prato.get()
  if prato != "":
    cursor.execute(f'SELECT * FROM pedidos WHERE pratos = "{prato}"')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Não possui este prato no sistema!")
    else:
      cursor.execute(f'SELECT * FROM pedidos WHERE pratos = "{prato}"')
      dados = cursor.fetchall()
      for x in treeeee.get_children():
        treeeee.delete(x)
        
      for y in dados:
        treeeee.insert("", "end", values=y)
      id_pedido_entry_prato.delete(0, END)
      frame_pratos.pack_forget()
      frame_arvore_pratos.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")


# ----------- ADM ------------ 

def voltar_adicionar_pedido_adm():
  id_pedido_entrada_adicionar.delete(0, END)
  pratos_pedido_entrada_adicionar.delete(0, END)
  observacoes_pedido_entrada_adicionar.delete(0, END)
  adicionar_pedido_adm.pack_forget()
  frameADM.pack(expand=True)

def voltar_alterar_pedido_adm():
    id_pedido_entrada_alterar.delete(0, END)
    pratos_pedido_entrada_alterar.delete(0, END)
    observacoes_pedido_entrada_alterar.delete(0, END)
    alterar_pedido_adm.pack_forget()
    frameADM.pack(expand=True)
  
def voltar_excluir_pedido_adm():
    id_pedido_entrada_excluir.delete(0, END)
    excluir_pedido_adm.pack_forget()
    frameADM.pack(expand=True)

def voltar_pesquisar_pedido_adm():
  pesquisar_p.pack_forget()
  frameADM.pack(expand=True)

def voltar_pesquisar_pedido():
  frame_arvore_pesquisar_pedido_em_preparo.pack_forget()
  frame_arvore_pesquisar_pedido_pronto.pack_forget()
  frame_arvore_pesquisar_pedido_tudo.pack_forget()
  pesquisar_p.pack(expand=True)





def voltar_adicionar_funcionario_adm():
  id_funcionario_entrada_adicionar.delete(0, END)
  nome_funcionario_entrada_adicionar.delete(0, END)
  cargo_funcionario_entrada_adicionar.delete(0, END)
  adicionar_f.pack_forget()
  frameADM.pack(expand=True)

def voltar_alterar_funcionario_adm():
  id_funcionario_entrada_alterar.delete(0, END)
  cargo_funcionario_entrada_alterar.delete(0, END)
  alterar_f.pack_forget()
  frameADM.pack(expand=True)

def voltar_excluir_funcionario_adm():
  id_funcionario_entrada_excluir.delete(0, END)
  excluir_f.pack_forget()
  frameADM.pack(expand=True)

def voltar_pesquisar_funcionario_adm():
  pesquisar_f.pack_forget()
  frameADM.pack(expand=True)

def voltar_pesquisar_funcionario():
  frame_arvore_pesquisar_funcionario_adm.pack_forget()
  frame_arvore_pesquisar_funcionario_garcom.pack_forget()
  frame_arvore_pesquisar_funcionario_recepcionista.pack_forget()
  frame_arvore_pesquisar_funcionario_cozinheiro.pack_forget()
  frame_arvore_pesquisar_funcionario_tudo.pack_forget()
  pesquisar_f.pack(expand=True)



def voltar_adicionar_mesa_adm():
  id_mesa_entrada_adicionar.delete(0, END)
  adicionar_m.pack_forget()
  frameADM.pack(expand=True)

def voltar_alterar_mesa_adm():
  alterar_m_adm.pack_forget()
  frameADM.pack(expand=True)

def voltar_excluir_mesa_adm():
  id_funcionario_entrada_excluir.delete(0, END)
  excluir_m.pack_forget()
  frameADM.pack(expand=True)

def voltar_pesquisar_mesa_adm():
  pesquisar_m.pack_forget()
  frameADM.pack(expand=True)

def voltar_pesquisar_mesa():
  frame_arvore_pesquisar_mesa_disponivel.pack_forget()
  frame_arvore_pesquisar_mesa_indisponivel.pack_forget()
  frame_arvore_pesquisar_mesa_tudo.pack_forget()
  pesquisar_m.pack(expand=True)



def adicionar_p_adm():
  frameADM.pack_forget()
  adicionar_pedido_adm.pack(expand=True)

def alterar_p_adm():
  frameADM.pack_forget()
  alterar_pedido_adm.pack(expand=True)  

def excluir_p_adm():
  frameADM.pack_forget()
  excluir_pedido_adm.pack(expand=True)  

def pesquisar_p_adm(): 
  frameADM.pack_forget()
  pesquisar_p.pack(expand=True)  


def adicionar_funcionario():
  frameADM.pack_forget()
  adicionar_f.pack(expand=True)

def alterar_funcionario():
  frameADM.pack_forget()
  alterar_f.pack(expand=True)

def excluir_funcionario():
  frameADM.pack_forget()
  excluir_f.pack(expand=True)

def pesquisar_funcionario():
  frameADM.pack_forget()
  pesquisar_f.pack(expand=True)



def adicionar_mesa():
  frameADM.pack_forget()
  adicionar_m.pack(expand=True)

def alterar_mesa_adm():
  frameADM.pack_forget()
  alterar_m_adm.pack(expand=True)

def excluir_mesa():
  frameADM.pack_forget()
  excluir_m.pack(expand=True)

def pesquisar_mesa():
  frameADM.pack_forget()
  pesquisar_m.pack(expand=True)

def pesquisar_funcionario_button_by_tudo():
  cursor.execute(f'SELECT * FROM funcionarios')
  dados = cursor.fetchall()
  for x in tree_pesquisar_funcionario_tudo.get_children():
    tree_pesquisar_funcionario_tudo.delete(x)
    
  for y in dados:
    tree_pesquisar_funcionario_tudo.insert("", "end", values=y)
  pesquisar_f.pack_forget()
  frame_arvore_pesquisar_funcionario_tudo.pack(expand=True)

def adicionar_p_adm_button():
  id = id_pedido_entrada_adicionar.get()
  prato = pratos_pedido_entrada_adicionar.get().title().strip()
  observacoes = observacoes_pedido_entrada_adicionar.get().lower().strip()
  if id != "" or prato != "":
    cursor.execute(f'SELECT * FROM pedidos WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) > 0:
      messagebox.showwarning(title = "ERR0", message= "Já possui algo com esse ID!")
    else:
      horario_atual = strftime("%H:%M:%S", localtime())
      cursor.execute(f'INSERT INTO pedidos(id, horario, status, pratos, observacoes) VALUES({id}, "{horario_atual}", "EM PREPARO", "{prato}", "{observacoes}")')
      conexao_banco.commit()
      id_pedido_entrada_adicionar.delete(0, END)
      pratos_pedido_entrada_adicionar.delete(0, END)
      observacoes_pedido_entrada_adicionar.delete(0, END)
      adicionar_pedido_adm.pack_forget()
      frameADM.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")

def adicionar_p_adm_button():
  id = id_pedido_entrada_adicionar.get()
  prato = pratos_pedido_entrada_adicionar.get().title().strip()
  observacoes = observacoes_pedido_entrada_adicionar.get().lower().strip()
  if id != "" or prato != "":
    cursor.execute(f'SELECT * FROM pedidos WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) > 0:
      messagebox.showwarning(title = "ERR0", message= "Já possui algo com esse ID!")
    else:
      horario_atual = strftime("%H:%M:%S", localtime())
      cursor.execute(f'INSERT INTO pedidos(id, horario, status, pratos, observacoes) VALUES({id}, "{horario_atual}", "EM PREPARO", "{prato}", "{observacoes}")')
      conexao_banco.commit()
      id_pedido_entrada_adicionar.delete(0, END)
      pratos_pedido_entrada_adicionar.delete(0, END)
      observacoes_pedido_entrada_adicionar.delete(0, END)
      adicionar_pedido_adm.pack_forget()
      frameADM.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")

def excluir_p_adm_button():
  id = id_pedido_entrada_excluir.get()
  if id != "":
    cursor.execute(f'SELECT * FROM pedidos WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Esse ID não está registrado!")
    else:
      cursor.execute(f'DELETE FROM pedidos WHERE id = {id}')
      conexao_banco.commit()
      id_pedido_entrada_excluir.delete(0, END)
      excluir_pedido_adm.pack_forget()
      frameADM.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "As opções de cargo são: administrador, garçom, cozinheiro e recepcionista!")

def alterar_p_adm_button():
  id = id_pedido_entrada_alterar.get()
  pratos = pratos_pedido_entrada_alterar.get()
  observacoes = observacoes_pedido_entrada_alterar.get()
  if id != "" or pratos != "":
    cursor.execute(f'SELECT * FROM pedidos WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Não possui nada com esse ID!")
    else:
      cursor.execute(f'UPDATE pedidos SET pratos = "{pratos}", observacoes = "{observacoes}" WHERE id = {id}')
      conexao_banco.commit()
      id_pedido_entrada_alterar.delete(0, END)
      pratos_pedido_entrada_alterar.delete(0,END)
      observacoes_pedido_entrada_alterar.delete(0,END)
      alterar_pedido_adm.pack_forget()
      frameADM.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")

def pesquisar_pedido_button_by_pronto():
  cursor.execute(f'SELECT * FROM pedidos WHERE status = "PRONTO"')
  dados = cursor.fetchall()
  for x in tree_pesquisar_pedido_pronto.get_children():
    tree_pesquisar_pedido_pronto.delete(x)
    
  for y in dados:
    tree_pesquisar_pedido_pronto.insert("", "end", values=y)
  pesquisar_p.pack_forget()
  frame_arvore_pesquisar_pedido_pronto.pack(expand=True)

def pesquisar_pedido_button_by_em_preparo():
  cursor.execute(f'SELECT * FROM pedidos WHERE status = "EM PREPARO"')
  dados = cursor.fetchall()
  for x in tree_pesquisar_pedido_em_preparo.get_children():
    tree_pesquisar_pedido_em_preparo.delete(x)
    
  for y in dados:
    tree_pesquisar_pedido_em_preparo.insert("", "end", values=y)
  pesquisar_p.pack_forget()
  frame_arvore_pesquisar_pedido_em_preparo.pack(expand=True)

def pesquisar_pedido_button_by_tudo():
  cursor.execute(f'SELECT * FROM pedidos')
  dados = cursor.fetchall()
  for x in tree_pesquisar_pedido_tudo.get_children():
    tree_pesquisar_pedido_tudo.delete(x)
    
  for y in dados:
    tree_pesquisar_pedido_tudo.insert("", "end", values=y)
  pesquisar_p.pack_forget()
  frame_arvore_pesquisar_pedido_tudo.pack(expand=True)

def adicionar_funcionario_button():
  id = id_funcionario_entrada_adicionar.get()
  nome = nome_funcionario_entrada_adicionar.get().title().strip()
  cargo = cargo_funcionario_entrada_adicionar.get().lower().strip()
  if cargo in ["administrador", "garçom", "cozinheiro", "recepcionista"]:
    if id != "" or nome != "":
      cursor.execute(f'SELECT * FROM funcionarios WHERE id = {id}')
      select = cursor.fetchall()
      if len(select) > 0:
        messagebox.showwarning(title = "ERR0", message= "Já possui algo com esse ID!")
      else:
        cursor.execute(f'INSERT INTO funcionarios(id, nome, cargo) VALUES({id},"{nome}", "{cargo}")')
        conexao_banco.commit()
        id_funcionario_entrada_adicionar.delete(0, END)
        nome_funcionario_entrada_adicionar.delete(0, END)
        cargo_funcionario_entrada_adicionar.delete(0, END)
        adicionar_f.pack_forget()
        frameADM.pack(expand=True)
    else:
      messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")
  else:
    messagebox.showwarning(title = "ERR0", message= "As opções de cargo são: administrador, garçom, cozinheiro e recepcionista!")

def alterar_funcionario_button():
  id = id_funcionario_entrada_alterar.get()
  cargo = cargo_funcionario_entrada_alterar.get().lower().strip()
  if cargo in ["administrador", "garçom", "cozinheiro", "recepcionista"]:
    if id != "":
      cursor.execute(f'SELECT * FROM funcionarios WHERE id = {id}')
      select = cursor.fetchall()
      if len(select) > 0:
        cursor.execute(f'UPDATE funcionarios SET cargo = "{cargo}" WHERE id = {id}')
        conexao_banco.commit()
        id_funcionario_entrada_alterar.delete(0, END)
        cargo_funcionario_entrada_alterar.delete(0, END)
        alterar_f.pack_forget()
        frameADM.pack(expand=True)
      else:
        messagebox.showwarning(title = "ERR0", message= "Não possui nada com esse ID!")
    else:
      messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")
  else:
    messagebox.showwarning(title = "ERR0", message= "As opções de cargo são: administrador, garçom, cozinheiro e recepcionista!")

def excluir_funcionario_button():
  id = id_funcionario_entrada_excluir.get()
  if id != "":
    cursor.execute(f'SELECT * FROM funcionarios WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Esse ID não está registrado!")
    else:
      cursor.execute(f'DELETE FROM funcionarios WHERE id = {id}')
      conexao_banco.commit()
      id_funcionario_entrada_excluir.delete(0, END)
      excluir_f.pack_forget()
      frameADM.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "As opções de cargo são: administrador, garçom, cozinheiro e recepcionista!")


def pesquisar_funcionario_button_by_administrador():
  cursor.execute(f'SELECT * FROM funcionarios WHERE cargo = "administrador"')
  dados = cursor.fetchall()
  for x in tree_pesquisar_funcionario_adm.get_children():
    tree_pesquisar_funcionario_adm.delete(x)
    
  for y in dados:
    tree_pesquisar_funcionario_adm.insert("", "end", values=y)
  pesquisar_f.pack_forget()
  frame_arvore_pesquisar_funcionario_adm.pack(expand=True)
  


def pesquisar_funcionario_button_by_garcom():
  cursor.execute(f'SELECT * FROM funcionarios WHERE cargo = "garçom"')
  dados = cursor.fetchall()
  for x in tree_pesquisar_funcionario_garcom.get_children():
    tree_pesquisar_funcionario_garcom.delete(x)
    
  for y in dados:
    tree_pesquisar_funcionario_garcom.insert("", "end", values=y)
  pesquisar_f.pack_forget()
  frame_arvore_pesquisar_funcionario_garcom.pack(expand=True)


def adicionar_mesa_button():
  id = id_mesa_entrada_adicionar.get()
  if id != "":
    cursor.execute(f'SELECT * FROM mesas WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) > 0:
      messagebox.showwarning(title = "ERR0", message= "Já possui algo com esse ID!")
    else:
      cursor.execute(f'INSERT INTO mesas(id, disponibilidade) VALUES({id}, "DISPONIVEL")')
      conexao_banco.commit()
      id_mesa_entrada_adicionar.delete(0, END)
      adicionar_m.pack_forget()
      frameADM.pack(expand=True)
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")


def pesquisar_funcionario_button_by_recepcionista():
  cursor.execute(f'SELECT * FROM funcionarios WHERE cargo = "recepcionista"')
  dados = cursor.fetchall()
  for x in tree_pesquisar_funcionario_recepcionista.get_children():
    tree_pesquisar_funcionario_recepcionista.delete(x)
    
  for y in dados:
    tree_pesquisar_funcionario_recepcionista.insert("", "end", values=y)
  pesquisar_f.pack_forget()
  frame_arvore_pesquisar_funcionario_recepcionista.pack(expand=True)


def alterar_disponivel_adm():
  id = id_mesa_entry_adm.get()
  if id != "":
    cursor.execute(f'SELECT * FROM mesas WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Não possui esta mesa no sistema!")
    else:
      cursor.execute(f'UPDATE mesas SET disponibilidade = "DISPONIVEL" WHERE id = {id}')
      conexao_banco.commit()
      id_mesa_entry_adm.delete(0, END)
      alterar_m_adm.pack_forget()
      frameADM.pack(expand=True)

def alterar_indisponivel_adm():
  id = id_mesa_entry_adm.get()
  if id != "":
    cursor.execute(f'SELECT * FROM mesas WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) <= 0:
      messagebox.showwarning(title = "ERR0", message= "Não possui esta mesa no sistema!")
    else:
      cursor.execute(f'UPDATE mesas SET disponibilidade = "INDISPONIVEL" WHERE id = {id}')
      conexao_banco.commit()
      id_mesa_entry_adm.delete(0, END)
      alterar_m_adm.pack_forget()
      frameADM.pack(expand=True)


def pesquisar_funcionario_button_by_cozinheiro():
  cursor.execute(f'SELECT * FROM funcionarios WHERE cargo = "cozinheiro"')
  dados = cursor.fetchall()
  for x in tree_pesquisar_funcionario_cozinheiro.get_children():
    tree_pesquisar_funcionario_cozinheiro.delete(x)
    
  for y in dados:
    tree_pesquisar_funcionario_cozinheiro.insert("", "end", values=y)
  pesquisar_f.pack_forget()
  frame_arvore_pesquisar_funcionario_cozinheiro.pack(expand=True)


def excluir_mesa_button():
  id = id_mesa_entrada_excluir.get()
  if id != "":
    cursor.execute(f'SELECT * FROM mesas WHERE id = {id}')
    select = cursor.fetchall()
    if len(select) > 0:
      cursor.execute(f'DELETE FROM mesas WHERE id = "{id}"')
      conexao_banco.commit()
      id_mesa_entrada_excluir.delete(0, END)
      excluir_m.pack_forget()
      frameADM.pack(expand=True)
    else:
      messagebox.showwarning(title = "ERR0", message= "Este ID não está cadastrado!")
  else:
    messagebox.showwarning(title = "ERR0", message= "Preecha os campos corretamente!")


def pesquisar_mesa_button_by_disponivel():
  cursor.execute(f'SELECT * FROM mesas WHERE disponibilidade = "DISPONIVEL"')
  dados = cursor.fetchall()
  for x in tree_pesquisar_mesa_disponivel.get_children():
    tree_pesquisar_mesa_disponivel.delete(x)
    
  for y in dados:
    tree_pesquisar_mesa_disponivel.insert("", "end", values=y)
  pesquisar_m.pack_forget()
  frame_arvore_pesquisar_mesa_disponivel.pack(expand=True)



def pesquisar_mesa_button_by_indisponivel():
  cursor.execute(f'SELECT * FROM mesas WHERE disponibilidade = "INDISPONIVEL"')
  dados = cursor.fetchall()
  for x in tree_pesquisar_mesa_indisponivel.get_children():
    tree_pesquisar_mesa_indisponivel.delete(x)
    
  for y in dados:
    tree_pesquisar_mesa_indisponivel.insert("", "end", values=y)
  pesquisar_m.pack_forget()
  frame_arvore_pesquisar_mesa_indisponivel.pack(expand=True)
  


def pesquisar_mesa_button_by_tudo():
  cursor.execute(f'SELECT * FROM mesas')
  dados = cursor.fetchall()
  for x in tree_pesquisar_mesa_tudo.get_children():
    tree_pesquisar_mesa_tudo.delete(x)
    
  for y in dados:
    tree_pesquisar_mesa_tudo.insert("", "end", values=y)
  pesquisar_m.pack_forget()
  frame_arvore_pesquisar_mesa_tudo.pack(expand=True)



#inicio
home = Tk()

home.title("Escolha")

home.resizable(False, False)

home.config(bg=tema)

home.attributes('-fullscreen',True)

homep = Frame(home)
homep.pack(expand=True)

homep.config(bg=tema)

empty = Label(homep, text="")
empty.grid(row=0)

label = Label(homep, text="Escolha como quer entrar", font=("Arial", 40, "bold"))
label.grid(row=0, column=1)

empty = Label(homep, text="")
empty.grid(row=2)

label_adm = Label(homep, text = "Adminstrador:", font=("Arial", 30))
label_adm.grid(row=3, column=0, padx=(20, 0), pady=10)

botao_adm = Button(homep, text="Clique", bg=tema, fg=tema_text, command=adm, font=("Arial", 15), width=10, height=1)
botao_adm.grid(row=4, column=0, padx=(15, 0), pady=10)

label_garcom = Label(homep, text= "Garçom:", font="Arial, 30")
label_garcom.grid(row=3, column=1)

botao_garcom = Button(homep, text="Clique", bg=tema, fg=tema_text, command=garcom, font=("Arial", 15), width=10, height=1)
botao_garcom.grid(row=4, column=1)

label_cozinheiro = Label(homep, text= "Cozinheiro:", font="Arial, 30")
label_cozinheiro.grid(row=3, column=2,padx=(0, 20), pady=10)

botao_cozinheiro = Button(homep, text="Clique", bg=tema, fg=tema_text, command=cozinheiro, font=("Arial", 15), width=10, height=1)
botao_cozinheiro.grid(row=4, column=2,padx=(0, 20), pady=10)

empty = Label(homep, text="")
empty.grid(row=5, columnspan=3)

label_recepcionista = Label(homep, text= "Recepcionista:", font="Arial, 30")
label_recepcionista.grid(row=6, column=1, pady=0)

botao_recepcionista = Button(homep, text="Clique", bg=tema, fg=tema_text, command=recepcionista, font=("Arial", 15), width=10, height=1)
botao_recepcionista.grid(row=7, column=1, pady=10)





#login adm
frame_adm = Frame(home,bg=tema)

title_label = Label(frame_adm, text="Digite seu usuário de administrador!", font = 'Arial 40 bold' ,bg=tema, fg=tema_text)
title_label.grid(row=0, column=0, columnspan=2, pady=40,padx=100)

usuario_id = Label(frame_adm, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
usuario_id.grid(row=1, column=0, padx=10, pady=5, sticky="e")

usuario_id_entrada1 = Entry(frame_adm, width=25, font=("Arial, 24"))
usuario_id_entrada1.grid(row=1, column=1, padx=10, pady=5, sticky="w")

senha_label = Label(frame_adm, text="Senha: ",bg=tema, fg=tema_text, font=("Arial, 30"))
senha_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

senha_entrada1 = Entry(frame_adm, show="*", width=25, font=("Arial, 24"))
senha_entrada1.grid(row=2, column=1, padx=10, pady=5, sticky="w")

botao_cadastro = Button(frame_adm, text="CADASTRAR", command=entrarADM, font=("Arial", 15), width=15, height=1)
botao_cadastro.grid(row=3, column=0, columnspan=2, pady=20)

label_voltar = Label(frame_adm, text= "Voltar:", font = 'Arial 20',bg=tema, fg=tema_text, pady=10)
label_voltar.grid(row=4, column=1)

botao_voltar = Button(frame_adm, text="Clique", bg=tema, fg=tema_text, command=voltar_adm, font=("Arial", 15), width=10, height=1)
botao_voltar.grid(row=5, column=1)

empty = Label(frame_adm, text="", bg=tema)
empty.grid(row=6)

frame_adm.config(bg=tema)

frame_adm.pack_forget()




#login garçom
frame_garcom = Frame(home, bg=tema)

title_label = Label(frame_garcom, text="Digite seu usuário de garçom!", font = 'Arial 40 bold' ,bg=tema, fg=tema_text)
title_label.grid(row=0, column=0, columnspan=2, pady=40,padx=100)

usuario_id = Label(frame_garcom, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
usuario_id.grid(row=1, column=0, padx=10, pady=5, sticky="e")

usuario_id_entrada2 = Entry(frame_garcom, width=25, font=("Arial, 24"))
usuario_id_entrada2.grid(row=1, column=1, padx=10, pady=5, sticky="w")

senha_label = Label(frame_garcom, text="Senha: ",bg=tema, fg=tema_text, font=("Arial, 30"))
senha_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

senha_entrada2 = Entry(frame_garcom, show="*", width=25, font=("Arial, 24"))
senha_entrada2.grid(row=2, column=1, padx=10, pady=5, sticky="w")

botao_cadastro = Button(frame_garcom, text="CADASTRAR", command=entrarGARCOM, font=("Arial", 15), width=15, height=1)
botao_cadastro.grid(row=3, column=0, columnspan=2, pady=20)

label_voltar = Label(frame_garcom, text= "Voltar:", font = 'Arial 20',bg=tema, fg=tema_text, pady=10)
label_voltar.grid(row=4, column=1)

botao_voltar = Button(frame_garcom, text="Clique", bg=tema, fg=tema_text, command=voltar_garcom, font=("Arial", 15), width=10, height=1)
botao_voltar.grid(row=5, column=1)

empty = Label(frame_garcom, text="", bg=tema)
empty.grid(row=6)

frame_garcom.config(bg=tema)

frame_garcom.pack_forget()




#login cozinheiro
frame_cozinheiro = Frame(home, bg=tema)

title_label = Label(frame_cozinheiro, text="Digite seu usuário de cozinheiro!", font = 'Arial 40 bold' ,bg=tema, fg=tema_text)
title_label.grid(row=0, column=0, columnspan=2, pady=40,padx=100)

usuario_id = Label(frame_cozinheiro, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
usuario_id.grid(row=1, column=0, padx=10, pady=5, sticky="e")

usuario_id_entrada3 = Entry(frame_cozinheiro, width=25, font=("Arial, 24"))
usuario_id_entrada3.grid(row=1, column=1, padx=10, pady=5, sticky="w")

senha_label = Label(frame_cozinheiro, text="Senha: ",bg=tema, fg=tema_text, font=("Arial, 30"))
senha_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

senha_entrada3 = Entry(frame_cozinheiro, show="*", width=25, font=("Arial, 24"))
senha_entrada3.grid(row=2, column=1, padx=10, pady=5, sticky="w")

botao_cadastro = Button(frame_cozinheiro, text="CADASTRAR", command=entrarCOZINHEIRO, font=("Arial", 15), width=15, height=1)
botao_cadastro.grid(row=3, column=0, columnspan=2, pady=20)

label_voltar = Label(frame_cozinheiro, text= "Voltar:", font = 'Arial 20',bg=tema, fg=tema_text, pady=10)
label_voltar.grid(row=4, column=1)

botao_voltar = Button(frame_cozinheiro, text="Clique", bg=tema, fg=tema_text, command=voltar_cozinheiro, font=("Arial", 15), width=10, height=1)
botao_voltar.grid(row=5, column=1)

empty = Label(frame_cozinheiro, text="", bg=tema)
empty.grid(row=6)

frame_cozinheiro.config(bg=tema)

frame_cozinheiro.pack_forget()




#login recpcionista
frame_recepcionista = Frame(home, bg=tema)

title_label = Label(frame_recepcionista, text="Digite seu usuário de recepcionista!", font = 'Arial 40 bold' ,bg=tema, fg=tema_text)
title_label.grid(row=0, column=0, columnspan=2, pady=40,padx=100)

usuario_id = Label(frame_recepcionista, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
usuario_id.grid(row=1, column=0, padx=10, pady=5, sticky="e")

usuario_id_entrada4 = Entry(frame_recepcionista, width=25, font=("Arial, 24"))
usuario_id_entrada4.grid(row=1, column=1, padx=10, pady=5, sticky="w")

senha_label = Label(frame_recepcionista, text="Senha: ",bg=tema, fg=tema_text, font=("Arial, 30"))
senha_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

senha_entrada4 = Entry(frame_recepcionista, show="*", width=25, font=("Arial, 24"))
senha_entrada4.grid(row=2, column=1, padx=10, pady=5, sticky="w")

botao_cadastro = Button(frame_recepcionista, text="CADASTRAR", command=entrarRECEPCIONISTA, font=("Arial", 15), width=15, height=1)
botao_cadastro.grid(row=3, column=0, columnspan=2, pady=20)

label_voltar = Label(frame_recepcionista, text= "Voltar:", font = 'Arial 20',bg=tema, fg=tema_text, pady=10)
label_voltar.grid(row=4, column=1)

botao_voltar = Button(frame_recepcionista, text="Clique", bg=tema, fg=tema_text, command=voltar_recepcionista, font=("Arial", 15), width=10, height=1)
botao_voltar.grid(row=5, column=1)

empty = Label(frame_recepcionista, text="", bg=tema)
empty.grid(row=6)



#funções garçom
frameGARCOM = Frame(home, bg=tema)

title_label = Label(frameGARCOM, text="Pedidos:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_label.grid(row=0, column=1, pady=50)

adicionar_pedido_botao = Button(frameGARCOM, text = "ADICIONAR PEDIDO", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command=adicionar_pedido)
adicionar_pedido_botao.grid(row = 1, column = 0)

alterar_pedido_botao = Button(frameGARCOM, text = "ALTERAR PEDIDO", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command=alterar_pedido)
alterar_pedido_botao.grid(row = 1, column = 1, padx=10)

cancelar_pedido_botao = Button(frameGARCOM, text = "CANCELAR PEDIDO", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command= excluir_pedido)
cancelar_pedido_botao.grid(row = 1, column = 2, padx=(0,10))

title_label = Label(frameGARCOM, text="Mesas:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_label.grid(row=2, column=1, pady=50)

alterar_mesa_botao = Button(frameGARCOM, text = "ALTERAR MESA", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command=alterar_mesa)
alterar_mesa_botao.grid(row = 3, column = 1, padx=10)

voltar_menu_pedido = Button(frameGARCOM, text = "VOLTAR MENU", font=("Arial", 18, "bold"), bg=tema, fg=tema_text, height=1, width=15, command = voltar_pedido_menu)
voltar_menu_pedido.grid(row=4, column = 1, pady = (100,0))


#adicionar pedido garçom
adicionar_p = Frame(home, bg=tema)

title_addp = Label(adicionar_p, text="Adicionar Pedido:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_addp.grid(row=0, column=1)
  

id_pedido = Label(adicionar_p, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_pedido.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_pedido_entrada = Entry(adicionar_p, width=25, font=("Arial, 24"))
id_pedido_entrada.grid(row=1, column=1, padx=10, pady=5, sticky="w")

pratos_pedido = Label(adicionar_p, text="PRATOS: ",bg=tema, fg=tema_text, font=("Arial, 30"))
pratos_pedido.grid(row=2, column=0, padx=10, pady=5, sticky="e")

pratos_pedido_entrada = Entry(adicionar_p, width=25, font=("Arial, 24"))
pratos_pedido_entrada.grid(row=2, column=1, padx=10, pady=5, sticky="w")

observacoes_pedido = Label(adicionar_p, text="OBSERVAÇÕES: ",bg=tema, fg=tema_text, font=("Arial, 30"))
observacoes_pedido.grid(row=3, column=0, padx=10, pady=5, sticky="e")

observacoes_pedido_entrada = Entry(adicionar_p, width=25, font=("Arial, 24"))
observacoes_pedido_entrada.grid(row=3, column=1, padx=10, pady=5, sticky="w")

cadastrar_pedido_botao = Button(adicionar_p, text = "CADASTRAR", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = adicionar_pedidu )
cadastrar_pedido_botao.grid(row = 4, column = 1, padx=(0,10))


#alterar pedido garçom
alterar_p = Frame(home, bg=tema)

title_altp = Label(alterar_p, text="Alterar Pedido:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_altp.grid(row=0, column=1)

label = Label(alterar_p, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_pedido_alterar_garcom = Entry(alterar_p, width=25, font=("Arial, 24"))
id_pedido_alterar_garcom.grid(row=1, column=1, padx=10, pady=5, sticky="w")

pratos_pedido_alterar = Label(alterar_p, text="PRATOS: ",bg=tema, fg=tema_text, font=("Arial, 30"))
pratos_pedido_alterar.grid(row=2, column=0, padx=10, pady=5, sticky="e")

pratos_pedido_alterar_entry = Entry(alterar_p, width=25, font=("Arial, 24"))
pratos_pedido_alterar_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

observacoes_pedido_alterar = Label(alterar_p, text="OBSERVAÇÕES: ",bg=tema, fg=tema_text, font=("Arial, 30"))
observacoes_pedido_alterar.grid(row=3, column=0, padx=10, pady=5, sticky="e")

observacoes_pedido_alterar_entry = Entry(alterar_p, width=25, font=("Arial, 24"))
observacoes_pedido_alterar_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

alterar_pedido_botao = Button(alterar_p, text = "ALTERAR", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = alterar_pedidu)
alterar_pedido_botao.grid(row = 4, column = 1, padx=(0,10))


#excluir pedido garçom
excluir_p = Frame(home, bg=tema)

title_exctp = Label(excluir_p, text="Excluir Pedido:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_exctp.grid(row=0, column=1)

id_pedido_excluir_garcom_name = Label(excluir_p, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_pedido_excluir_garcom_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_pedido_excluir_garcom = Entry(excluir_p, width=25, font=("Arial, 24"))
id_pedido_excluir_garcom.grid(row=1, column=1, padx=10, pady=5, sticky="w")

excluir_pedido_botao = Button(excluir_p, text = "EXCLUIR", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = excluir_pedidu)
excluir_pedido_botao.grid(row = 2, column = 1, padx=(0,10))



#alterar status mesa garçom
alterar_m = Frame(home, bg=tema)

title_alt = Label(alterar_m, text="Alterar Status Mesa:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_alt.grid(row=0, column=0)

id_mesa = Label(alterar_m, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_mesa.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_mesa_entry = Entry(alterar_m, width=25, font=("Arial, 24"))
id_mesa_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")

alterar_mesa1_botao = Button(alterar_m, text = "DISPONIVEL", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = alterar_disponivel)
alterar_mesa1_botao.grid(row = 2, column = 0, padx=(0,10),pady=30)

alterar_mesa2_botao = Button(alterar_m, text = "INDISPONIVEL", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = alterar_indisponivel)
alterar_mesa2_botao.grid(row = 3, column = 0, padx=(0,10))



#funções cozinheiro
cozinheiro_MENU = Frame(home, bg=tema)

title_coz = Label(cozinheiro_MENU, text="Alteração Pedidos:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_coz.grid(row=0, column=0)

cozinheiro_status = Button(cozinheiro_MENU, text = "STATUS PEDIDO", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = cozinheiro_alterar_status_pedido)
cozinheiro_status.grid(row = 1, column = 0, padx=(0,10),pady=30,sticky="e")

cozinheiro_pesquisa = Button(cozinheiro_MENU, text = "PESQUISAR PEDIDO", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_pedido)
cozinheiro_pesquisa.grid(row = 2, column = 0, padx=(0,10),sticky="w")

voltar_menu_total = Button(cozinheiro_MENU, text = "VOLTAR", font=("Arial", 18, "bold"), bg=tema, fg=tema_text, height=1, width=15, command = voltar_adm_menu)
voltar_menu_total.grid(row=3, column = 0, pady = (100,0))


#aslterar status pedido cozinheiro
status_pedido_coz = Frame(home, bg=tema)

title_cozi = Label(status_pedido_coz, text="Alteração de Status:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_cozi.grid(row=0, column=1)

id_status_pedido = Label(status_pedido_coz, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_status_pedido.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_pedido_entry_coz = Entry(status_pedido_coz, width=25, font=("Arial, 24"))
id_pedido_entry_coz.grid(row=1, column=1, padx=10, pady=5, sticky="w")

pronto_pedido_botao = Button(status_pedido_coz, text = "ALT. PRONTO", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = alteracao_status)
pronto_pedido_botao.grid(row = 2, column = 1)


#pesquisar pedido cozinheiro
pesquisa_pedido = Frame(home, bg=tema)

title_pesq = Label(pesquisa_pedido, text="Pesquisa de Pedidos:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_pesq.grid(row=0, column=1,pady=(0,30))

tudo_pesq_but = Button(pesquisa_pedido, text = "PESQUISA TUDO", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = tudo_pesq_tabela)
tudo_pesq_but.grid(row = 2, column = 0,padx=30)

status_pesq_but = Button(pesquisa_pedido, text = "PESQUISA STATUS", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_tabela_status)
status_pesq_but.grid(row = 2, column = 1)

prato_pesq_but = Button(pesquisa_pedido, text = "PESQUISA PRATO", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = ir_pratos)
prato_pesq_but.grid(row = 2, column = 2)


#Pesquisar todos pedidos cozinheiro
frame_arvore_total = Frame(home, bg=tema)

todos_ped = Label(frame_arvore_total, text="Todos Pedidos:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped.grid(row=0, column=0,pady=(0,20))

treee = ttk.Treeview(frame_arvore_total, columns=("ID", "HORÁRIO", "STATUS", "PRATOS", "OBSERVAÇÕES"), show="headings")  
treee.heading("ID", text="ID")
treee.heading("HORÁRIO", text="Nome")
treee.heading("STATUS", text="Status")
treee.heading("PRATOS", text="Pratos")  
treee.heading("OBSERVAÇÕES", text="Observações")  
treee.grid(row=1, column=0, padx=10, pady=10)

voltar_menu_coz = Button(frame_arvore_total, text = "VOLTAR", font=("Arial", 18, "bold"), bg=tema, fg=tema_text, height=1, width=15, command = voltar_coz_menu)
voltar_menu_coz.grid(row=4, column = 0, pady = (100,0))




#Pesquisar status cozinheiro
frame_status_coz = Frame(home, bg=tema)

status_ped = Label(frame_status_coz, text="Pesquisar Por:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
status_ped.grid(row=0, column=0,pady=(0,20))

por_pronto = Button(frame_status_coz, text = "PRONTO", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = status_pesq_tabela_pronto)
por_pronto.grid(row = 1, column = 0, pady=(0,30))

por_em_preparo = Button(frame_status_coz, text = "EM PREPARO", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = status_pesq_tabela_em_preparo)
por_em_preparo.grid(row = 2, column = 0)

#Pesquisar status pronto cozinheiro
frame_arvore_status = Frame(home, bg=tema)

todos_ped_stat = Label(frame_arvore_status, text="Pedidos Prontos:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped_stat.grid(row=0, column=0,pady=(0,20))

tree = ttk.Treeview(frame_arvore_status, columns=("ID", "HORÁRIO", "STATUS", "PRATOS", "OBSERVAÇÕES"), show="headings")  
tree.heading("ID", text="ID")
tree.heading("HORÁRIO", text="Horário")
tree.heading("STATUS", text="Status")
tree.heading("PRATOS", text="Pratos")  
tree.heading("OBSERVAÇÕES", text="Observações")  
tree.grid(row=1, column=0, padx=10, pady=10)

voltar_menu_coz_stat = Button(frame_arvore_status, text = "VOLTAR", font=("Arial", 18, "bold"), bg=tema, fg=tema_text, height=1, width=15, command = voltar_coz_menu)
voltar_menu_coz_stat.grid(row=4, column = 0, pady = (100,0))

#Pesquisar status em preparo cozinheiro
frame_arvore_em_preparo = Frame(home, bg=tema)

todos_ped = Label(frame_arvore_em_preparo, text="Pedidos Em Preparo:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped.grid(row=0, column=0,pady=(0,20))

treeee = ttk.Treeview(frame_arvore_em_preparo, columns=("ID", "HORÁRIO", "STATUS", "PRATOS", "OBSERVAÇÕES"), show="headings")  
treeee.heading("ID", text="ID")
treeee.heading("HORÁRIO", text="Horário")
treeee.heading("STATUS", text="Status")
treeee.heading("PRATOS", text="Pratos")  
treeee.heading("OBSERVAÇÕES", text="Observações")  
treeee.grid(row=1, column=0, padx=10, pady=10)

voltar_menu_coz_preparo = Button(frame_arvore_em_preparo, text = "VOLTAR", font=("Arial", 18, "bold"), bg=tema, fg=tema_text, height=1, width=15, command = voltar_coz_menu)
voltar_menu_coz_preparo.grid(row=4, column = 0, pady = (100,0))


#Pesquisar pedidos com base em pratos
frame_pratos = Frame(home, bg=tema)

title_pratos_pesq = Label(frame_pratos, text="Alteração de Status:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_pratos_pesq.grid(row=0, column=1)

id_status_prato = Label(frame_pratos, text="PRATOS: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_status_prato.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_pedido_entry_prato = Entry(frame_pratos, width=25, font=("Arial, 24"))
id_pedido_entry_prato.grid(row=1, column=1, padx=10, pady=5, sticky="w")

ver_tabela_prato = Button(frame_pratos, text = "VER TABELA", font=("Arial", 18, "bold"), bg=tema, fg=tema_text, height=1, width=15, command = verificar_id_prato)
ver_tabela_prato.grid(row=2, column = 1, pady = (20,0))

#Pesquisado por pratos cozinheiro
frame_arvore_pratos = Frame(home, bg=tema)

title_pratos_tabel = Label(frame_arvore_pratos, text="Tabela Por Pratos:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_pratos_tabel.grid(row=0, column=0)

treeeee = ttk.Treeview(frame_arvore_pratos, columns=("ID", "HORÁRIO", "STATUS", "PRATOS", "OBSERVAÇÕES"), show="headings")  
treeeee.heading("ID", text="ID")
treeeee.heading("HORÁRIO", text="Horário")
treeeee.heading("STATUS", text="Status")
treeeee.heading("PRATOS", text="Pratos")  
treeeee.heading("OBSERVAÇÕES", text="Observações")  
treeeee.grid(row=1, column=0, padx=10, pady=10)

voltar_menu_coz_prato = Button(frame_arvore_pratos, text = "VOLTAR", font=("Arial", 18, "bold"), bg=tema, fg=tema_text, height=1, width=15, command = voltar_coz_menu)
voltar_menu_coz_prato.grid(row=2, column = 0, pady = (100,0))



#Funções Recepcionista
frame_recepcionsta_menu = Frame(home, bg=tema) 
  
title_menu_recepc = Label(frame_recepcionsta_menu, text="Menu Recepcionista:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_menu_recepc.grid(row=0, column=0,pady=(0,30))

but_alterar_sts_mesa = Button(frame_recepcionsta_menu, text = "ALTERAR MESA", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = ir_status_mesa)
but_alterar_sts_mesa.grid(row = 1, column = 0,pady=(0,30))

but_pesquiasr_mesa = Button(frame_recepcionsta_menu, text = "PESQUISAR MESA", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = ir_pesquisar_mesa_la)
but_pesquiasr_mesa.grid(row = 2, column = 0)

voltar_menu_rec_menu = Button(frame_recepcionsta_menu, text = "VOLTAR", font=("Arial", 18, "bold"), bg=tema, fg=tema_text, height=1, width=15, command = voltar_para_menu_depois_do_rec)
voltar_menu_rec_menu.grid(row=3, column = 0, pady = (100,0))

#Alterar status da mesa recepcionista
frame_status_mesa = Frame(home, bg=tema) 

title_status_mesa = Label(frame_status_mesa, text="Alterar Para:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_status_mesa.grid(row=0, column=1,pady=(0,30))

id_status_mesa = Label(frame_status_mesa, text="MESA: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_status_mesa.grid(row=1, column=0,pady=5, sticky="e")

id_pedido_entry_mesa = Entry(frame_status_mesa, width=25, font=("Arial, 24"))
id_pedido_entry_mesa.grid(row=1, column=1, padx=(10,0), pady=5, sticky="w", columnspan=1)

but_disponivel = Button(frame_status_mesa, text = "DISPONIVEL", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = alterar_mesa_disponivel)
but_disponivel.grid(row = 2, column = 1, pady=(0,20))

but_indisponivel = Button(frame_status_mesa, text = "INDISPONIVEL", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = alterar_mesa_indisponivel)
but_indisponivel.grid(row = 3, column = 1)



#Pesquisar mesa recepcionista
frame_pesquisar_mesa = Frame(home, bg=tema) 

title_pesquisa_mesa = Label(frame_pesquisar_mesa, text="Ver Mesa:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_pesquisa_mesa.grid(row=0, column=1,pady=(0,30))

id_pesquisa_mesa = Label(frame_pesquisar_mesa, text="MESA: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_pesquisa_mesa.grid(row=1, column=0,pady=5, sticky="e")

id_pedido_entry_mesa_pesquisa = Entry(frame_pesquisar_mesa, width=25, font=("Arial, 24"))
id_pedido_entry_mesa_pesquisa.grid(row=1, column=1, padx=(10,0), pady=5, sticky="w", columnspan=1)

but_pesquisar_mesas = Button(frame_pesquisar_mesa, text = "VER TABELA", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesq_mesa)
but_pesquisar_mesas.grid(row = 2, column = 1, pady=(0,20))

#Pesquisado mesas recepcionista
frame_arvore_mesa_pesq = Frame(home, bg=tema)

title_mesas_tabel = Label(frame_arvore_mesa_pesq, text="Tabela Por Mesa:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_mesas_tabel.grid(row=0, column=0)


treeeeee = ttk.Treeview(frame_arvore_mesa_pesq, columns=("ID", "DISPONIBILIDADE"), show="headings")  
treeeeee.heading("ID", text="ID")
treeeeee.heading("DISPONIBILIDADE", text="Disponibilidade")
treeeeee.grid(row=1, column=0, padx=10, pady=10)

voltar_pesq_coz_mesa = Button(frame_arvore_mesa_pesq, text = "VOLTAR", font=("Arial", 18, "bold"), bg=tema, fg=tema_text, height=1, width=15, command = voltar_rec_menu)
voltar_pesq_coz_mesa.grid(row=2, column = 0, pady = (100,0))





#Funções adm
frameADM = Frame(home, bg=tema)

title_label = Label(frameADM, text="Funções ADM:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=0, column=1, columnspan=2, pady=20)

title_label = Label(frameADM, text="Funcionários:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_label.grid(row=1, column=1, columnspan=2, pady=50)

adicionar_funcionario_botao = Button(frameADM, text = "ADICIONAR FUNCIO", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command=adicionar_funcionario)
adicionar_funcionario_botao.grid(row = 2, column = 0, padx=10)

alterar_funcionario_botao = Button(frameADM, text = "ALTERAR FUNCIO", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command=alterar_funcionario)
alterar_funcionario_botao.grid(row = 2, column = 1, padx=10)

excluir_funcionario_botao = Button(frameADM, text = "EXCLUIR FUNCIO", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command=excluir_funcionario)
excluir_funcionario_botao.grid(row = 2, column = 2, padx=10)

pesquisar_funcionario_botao = Button(frameADM, text = "PESQUISAR FUNCIO", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command=pesquisar_funcionario)
pesquisar_funcionario_botao.grid(row = 2, column = 3, padx=10)

title_label = Label(frameADM, text="Pedidos:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=3, column=1, columnspan=2, pady=50)

adicionar_pedido_botao = Button(frameADM, text = "ADICIONAR PEDIDO", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command=adicionar_p_adm)
adicionar_pedido_botao.grid(row = 4, column = 0)

alterar_pedido_botao = Button(frameADM, text = "ALTERAR PEDIDO", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command=alterar_p_adm)
alterar_pedido_botao.grid(row = 4, column = 1, padx=10, sticky = "e")

cancelar_pedido_botao = Button(frameADM, text = "CANCELAR PEDIDO", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command= excluir_p_adm)
cancelar_pedido_botao.grid(row = 4, column = 2, padx=(0,10), sticky = "w")

pesquisar_pedido_botao = Button(frameADM, text = "PESQUISAR PEDIDO", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command= pesquisar_p_adm)
pesquisar_pedido_botao.grid(row = 4, column = 3, padx=(0,10))

title_label = Label(frameADM, text="Mesas:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=5, column=1, columnspan=2, pady=50)

adicionar_mesa_botao = Button(frameADM, text = "ADICIONAR MESA", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command=adicionar_mesa)
adicionar_mesa_botao.grid(row = 6, column = 0)

alterar_mesa_botao = Button(frameADM, text = "ALTERAR MESA", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command=alterar_mesa_adm)
alterar_mesa_botao.grid(row = 6, column = 1, padx=10, sticky = "e")

cancelar_mesa_botao = Button(frameADM, text = "EXCLUIR MESA", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command= excluir_mesa)
cancelar_mesa_botao.grid(row = 6, column = 2, padx=(0,10), sticky = "w")

pesquisar_mesa_botao = Button(frameADM, text = "PESQUISAR MESA", font=("Arial", 25, "bold"), bg=tema, fg=tema_text, height=1,width=18, command= pesquisar_mesa)
pesquisar_mesa_botao.grid(row = 6, column = 3, padx=(0,10))

voltar_menu_pedido = Button(frameADM, text = "VOLTAR MENU", font=("Arial", 18, "bold"), bg=tema, fg=tema_text, height=1, width=15, command = voltar_pedido_menu)
voltar_menu_pedido.grid(row = 7, column = 3, pady = (100,0))






#Adicionar pedido adm
adicionar_pedido_adm = Frame(home, bg=tema)

title_addp = Label(adicionar_pedido_adm, text="Adicionar Pedido:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_addp.grid(row=0, column=1)
  

id_pedido = Label(adicionar_pedido_adm, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_pedido.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_pedido_entrada_adicionar = Entry(adicionar_pedido_adm, width=25, font=("Arial, 24"))
id_pedido_entrada_adicionar.grid(row=1, column=1, padx=10, pady=5, sticky="w")

pratos_pedido = Label(adicionar_pedido_adm, text="PRATOS: ",bg=tema, fg=tema_text, font=("Arial, 30"))
pratos_pedido.grid(row=2, column=0, padx=10, pady=5, sticky="e")

pratos_pedido_entrada_adicionar = Entry(adicionar_pedido_adm, width=25, font=("Arial, 24"))
pratos_pedido_entrada_adicionar.grid(row=2, column=1, padx=10, pady=5, sticky="w")

observacoes_pedido = Label(adicionar_pedido_adm, text="OBSERVAÇÕES: ",bg=tema, fg=tema_text, font=("Arial, 30"))
observacoes_pedido.grid(row=3, column=0, padx=10, pady=5, sticky="e")

observacoes_pedido_entrada_adicionar = Entry(adicionar_pedido_adm, width=25, font=("Arial, 24"))
observacoes_pedido_entrada_adicionar.grid(row=3, column=1, padx=10, pady=5, sticky="w")

cadastrar_pedido_botao = Button(adicionar_pedido_adm, text = "CADASTRAR", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = adicionar_p_adm_button)
cadastrar_pedido_botao.grid(row = 4, column = 1, padx=(0,10))

botao_voltar_adm = Button(adicionar_pedido_adm, text="Voltar", bg=tema, fg=tema_text, command=voltar_adicionar_pedido_adm, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=5, column=2)




#Alterar pedido adm
alterar_pedido_adm = Frame(home, bg=tema)

title_altp = Label(alterar_pedido_adm, text="Alterar Pedido:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_altp.grid(row=0, column=1)

id_pedido_alterar = Label(alterar_pedido_adm, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_pedido_alterar.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_pedido_entrada_alterar = Entry(alterar_pedido_adm, width=25, font=("Arial, 24"))
id_pedido_entrada_alterar.grid(row=1, column=1, padx=10, pady=5, sticky="w")

pratos_pedido_alterar = Label(alterar_pedido_adm, text="PRATOS: ",bg=tema, fg=tema_text, font=("Arial, 30"))
pratos_pedido_alterar.grid(row=2, column=0, padx=10, pady=5, sticky="e")

pratos_pedido_entrada_alterar = Entry(alterar_pedido_adm, width=25, font=("Arial, 24"))
pratos_pedido_entrada_alterar.grid(row=2, column=1, padx=10, pady=5, sticky="w")

observacoes_pedido_alterar = Label(alterar_pedido_adm, text="OBSERVAÇÕES: ",bg=tema, fg=tema_text, font=("Arial, 30"))
observacoes_pedido_alterar.grid(row=3, column=0, padx=10, pady=5, sticky="e")

observacoes_pedido_entrada_alterar = Entry(alterar_pedido_adm, width=25, font=("Arial, 24"))
observacoes_pedido_entrada_alterar.grid(row=3, column=1, padx=10, pady=5, sticky="w")

alterar_pedido_botao = Button(alterar_pedido_adm, text = "ALTERAR", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = alterar_p_adm_button)
alterar_pedido_botao.grid(row=4, column=1, padx=10, pady=5)

botao_voltar_adm = Button(alterar_pedido_adm, text="Voltar", bg=tema, fg=tema_text, command=voltar_alterar_pedido_adm, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=5, column=2)




#Excluir pedido adm
excluir_pedido_adm = Frame(home, bg=tema)

title_altp = Label(excluir_pedido_adm, text="Excluir Pedido:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
title_altp.grid(row=0, column=1)

id_pedido_excluir = Label(excluir_pedido_adm, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_pedido_excluir.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_pedido_entrada_excluir = Entry(excluir_pedido_adm, width=25, font=("Arial, 24"))
id_pedido_entrada_excluir.grid(row=1, column=1, padx=10, pady=5, sticky="w")

excluir_pedido_botao = Button(excluir_pedido_adm, text = "EXCLUIR", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = excluir_p_adm_button)
excluir_pedido_botao.grid(row=2, column=1, padx=10, pady=5)

botao_voltar_adm = Button(excluir_pedido_adm, text="Voltar", bg=tema, fg=tema_text, command=voltar_excluir_pedido_adm, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=3, column=2)






#Pesquisar pedido pronto adm
frame_arvore_pesquisar_pedido_pronto = Frame(home, bg=tema)

todos_ped_stat = Label(frame_arvore_pesquisar_pedido_pronto, text="Pedidos Prontos:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped_stat.grid(row=0, column=1,pady=(0,20))

tree_pesquisar_pedido_pronto = ttk.Treeview(frame_arvore_pesquisar_pedido_pronto, columns=("ID", "HORÁRIO", "STATUS", "PRATOS", "OBSERVACOES"), show="headings")  
tree_pesquisar_pedido_pronto.heading("ID", text="ID")
tree_pesquisar_pedido_pronto.heading("HORÁRIO", text="Horario")
tree_pesquisar_pedido_pronto.heading("STATUS", text="Status") 
tree_pesquisar_pedido_pronto.heading("PRATOS", text="Pratos") 
tree_pesquisar_pedido_pronto.heading("OBSERVACOES", text="Observacoes") 
tree_pesquisar_pedido_pronto.grid(row=1, column=1, padx=10, pady=10)

botao_voltar_adm = Button(frame_arvore_pesquisar_pedido_pronto, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_pedido, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=2, column=2)

  
#Pesquisar pedidos em preparo adm
frame_arvore_pesquisar_pedido_em_preparo = Frame(home, bg=tema)

todos_ped_stat = Label(frame_arvore_pesquisar_pedido_em_preparo, text="Pedidos Em Preparo:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped_stat.grid(row=0, column=1,pady=(0,20))

tree_pesquisar_pedido_em_preparo = ttk.Treeview(frame_arvore_pesquisar_pedido_em_preparo, columns=("ID", "HORÁRIO", "STATUS", "PRATOS", "OBSERVACOES"), show="headings")  
tree_pesquisar_pedido_em_preparo.heading("ID", text="ID")
tree_pesquisar_pedido_em_preparo.heading("HORÁRIO", text="Horario")
tree_pesquisar_pedido_em_preparo.heading("STATUS", text="Status") 
tree_pesquisar_pedido_em_preparo.heading("PRATOS", text="Pratos") 
tree_pesquisar_pedido_em_preparo.heading("OBSERVACOES", text="Observacoes") 
tree_pesquisar_pedido_em_preparo.grid(row=1, column=1, padx=10, pady=10)

botao_voltar_adm = Button(frame_arvore_pesquisar_pedido_em_preparo, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_pedido, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=2, column=2)


#Pesquisar todos pedidos adm
frame_arvore_pesquisar_pedido_tudo = Frame(home, bg=tema)

todos_ped_stat = Label(frame_arvore_pesquisar_pedido_tudo, text="Todos os Pedidos:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped_stat.grid(row=0, column=1,pady=(0,20))

tree_pesquisar_pedido_tudo = ttk.Treeview(frame_arvore_pesquisar_pedido_tudo, columns=("ID", "HORÁRIO", "STATUS", "PRATOS", "OBSERVACOES"), show="headings")  
tree_pesquisar_pedido_tudo.heading("ID", text="ID")
tree_pesquisar_pedido_tudo.heading("HORÁRIO", text="Horario")
tree_pesquisar_pedido_tudo.heading("STATUS", text="Status") 
tree_pesquisar_pedido_tudo.heading("PRATOS", text="Pratos") 
tree_pesquisar_pedido_tudo.heading("OBSERVACOES", text="Observacoes") 
tree_pesquisar_pedido_tudo.grid(row=1, column=1, padx=10, pady=10)

botao_voltar_adm = Button(frame_arvore_pesquisar_pedido_tudo, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_pedido, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=2, column=2)



#Tipo de pesquisa de pedido adm
pesquisar_p = Frame(home, bg=tema)

title_label = Label(pesquisar_p, text="Pesquisar Pedidos:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=0, column=1, columnspan=2, pady=20)

title_label = Label(pesquisar_p, text="Status", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=1, column=1, columnspan=2, pady=20)

botao = Button(pesquisar_p, text = "Pronto", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_pedido_button_by_pronto)
botao.grid(row = 2, column = 1, padx=(0,10))

botao = Button(pesquisar_p, text = "Em Preparo", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_pedido_button_by_em_preparo)
botao.grid(row = 2, column = 2, padx=(0,10))

botao = Button(pesquisar_p, text = "Todos", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_pedido_button_by_tudo)
botao.grid(row = 3, column = 1, columnspan=2, padx=(0,10), pady=20)

botao_voltar_adm = Button(pesquisar_p, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_pedido_adm, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=4, column=3)


#Adicionar funcionário adm
adicionar_f = Frame(home, bg=tema)

title_label = Label(adicionar_f, text="Adicionar Funcionário:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=0, column=1, columnspan=2, pady=20)

id_funcionario = Label(adicionar_f, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_funcionario.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_funcionario_entrada_adicionar = Entry(adicionar_f, width=25, font=("Arial, 24"))
id_funcionario_entrada_adicionar.grid(row=1, column=1, padx=10, pady=5, sticky="w")

nome_funcionario = Label(adicionar_f, text="NOME: ",bg=tema, fg=tema_text, font=("Arial, 30"))
nome_funcionario.grid(row=2, column=0, padx=10, pady=5, sticky="e")

nome_funcionario_entrada_adicionar = Entry(adicionar_f, width=25, font=("Arial, 24"))
nome_funcionario_entrada_adicionar.grid(row=2, column=1, padx=10, pady=5, sticky="w")

cargo_funcionario = Label(adicionar_f, text="CARGO: ",bg=tema, fg=tema_text, font=("Arial, 30"))
cargo_funcionario.grid(row=3, column=0, padx=10, pady=5, sticky="e")

cargo_funcionario_entrada_adicionar = Entry(adicionar_f, width=25, font=("Arial, 24"))
cargo_funcionario_entrada_adicionar.grid(row=3, column=1, padx=10, pady=5, sticky="w")

botao = Button(adicionar_f, text = "CADASTRAR", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = adicionar_funcionario_button)
botao.grid(row = 4, column = 1, padx=(0,10))

botao_voltar_adm = Button(adicionar_f, text="Voltar", bg=tema, fg=tema_text, command=voltar_adicionar_funcionario_adm, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=5, column=2)


#Alterar funcionário adm
alterar_f = Frame(home, bg=tema)

title_label = Label(alterar_f, text="Alterar Funcionário:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=0, column=1, columnspan=2, pady=20)

id_funcionario = Label(alterar_f, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_funcionario.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_funcionario_entrada_alterar = Entry(alterar_f, width=25, font=("Arial, 24"))
id_funcionario_entrada_alterar.grid(row=1, column=1, padx=10, pady=5, sticky="w")

cargo_funcionario = Label(alterar_f, text="NOVO CARGO: ",bg=tema, fg=tema_text, font=("Arial, 30"))
cargo_funcionario.grid(row=3, column=0, padx=10, pady=5, sticky="e")

cargo_funcionario_entrada_alterar = Entry(alterar_f, width=25, font=("Arial, 24"))
cargo_funcionario_entrada_alterar.grid(row=3, column=1, padx=10, pady=5, sticky="w")

botao = Button(alterar_f, text = "ALTERAR", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = alterar_funcionario_button)
botao.grid(row = 4, column = 1, padx=(0,10))

botao_voltar_adm = Button(alterar_f, text="Voltar", bg=tema, fg=tema_text, command=voltar_alterar_funcionario_adm, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=5, column=2)


#Excluir funcionário adm
excluir_f = Frame(home, bg=tema)

title_label = Label(excluir_f, text="Excluir Funcionário:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=0, column=1, columnspan=2, pady=20)

id_funcionario = Label(excluir_f, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_funcionario.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_funcionario_entrada_excluir = Entry(excluir_f, width=25, font=("Arial, 24"))
id_funcionario_entrada_excluir.grid(row=1, column=1, padx=10, pady=5, sticky="w")

botao = Button(excluir_f, text = "EXCLUIR", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = excluir_funcionario_button)
botao.grid(row = 4, column = 1, padx=(0,10))

botao_voltar_adm = Button(excluir_f, text="Voltar", bg=tema, fg=tema_text, command=voltar_excluir_funcionario_adm, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=5, column=2)


#Pesquisar adm adm
frame_arvore_pesquisar_funcionario_adm = Frame(home, bg=tema)

todos_ped_stat = Label(frame_arvore_pesquisar_funcionario_adm, text="Funcionários Administradores:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped_stat.grid(row=0, column=1,pady=(0,20))

tree_pesquisar_funcionario_adm = ttk.Treeview(frame_arvore_pesquisar_funcionario_adm, columns=("ID", "NOME", "CARGO"), show="headings")  
tree_pesquisar_funcionario_adm.heading("ID", text="ID")
tree_pesquisar_funcionario_adm.heading("NOME", text="Nome")
tree_pesquisar_funcionario_adm.heading("CARGO", text="Cargo") 
tree_pesquisar_funcionario_adm.grid(row=1, column=1, padx=10, pady=10)

botao_voltar_adm = Button(frame_arvore_pesquisar_funcionario_adm, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_funcionario, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=2, column=2)



#Pesquisar garçom adm
frame_arvore_pesquisar_funcionario_garcom = Frame(home, bg=tema)

todos_ped_stat = Label(frame_arvore_pesquisar_funcionario_garcom, text="Funcionários Garçons:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped_stat.grid(row=0, column=1,pady=(0,20))

tree_pesquisar_funcionario_garcom = ttk.Treeview(frame_arvore_pesquisar_funcionario_garcom, columns=("ID", "NOME", "CARGO"), show="headings")  
tree_pesquisar_funcionario_garcom.heading("ID", text="ID")
tree_pesquisar_funcionario_garcom.heading("NOME", text="Nome")
tree_pesquisar_funcionario_garcom.heading("CARGO", text="Cargo") 
tree_pesquisar_funcionario_garcom.grid(row=1, column=1, padx=10, pady=10)

botao_voltar_adm = Button(frame_arvore_pesquisar_funcionario_garcom, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_funcionario, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=2, column=2)



#Pesquisar recepcionista adm
frame_arvore_pesquisar_funcionario_recepcionista = Frame(home, bg=tema)

todos_ped_stat = Label(frame_arvore_pesquisar_funcionario_recepcionista, text="Funcionários Recepcionistas:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped_stat.grid(row=0, column=1,pady=(0,20))

tree_pesquisar_funcionario_recepcionista = ttk.Treeview(frame_arvore_pesquisar_funcionario_recepcionista, columns=("ID", "NOME", "CARGO"), show="headings")  
tree_pesquisar_funcionario_recepcionista.heading("ID", text="ID")
tree_pesquisar_funcionario_recepcionista.heading("NOME", text="Nome")
tree_pesquisar_funcionario_recepcionista.heading("CARGO", text="Cargo") 
tree_pesquisar_funcionario_recepcionista.grid(row=1, column=1, padx=10, pady=10)

botao_voltar_adm = Button(frame_arvore_pesquisar_funcionario_recepcionista, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_funcionario, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=2, column=2)




#Pesquisar cozinheiro adm
frame_arvore_pesquisar_funcionario_cozinheiro = Frame(home, bg=tema)

todos_ped_stat = Label(frame_arvore_pesquisar_funcionario_cozinheiro, text="Funcionários Cozinheiros:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped_stat.grid(row=0, column=1,pady=(0,20))

tree_pesquisar_funcionario_cozinheiro = ttk.Treeview(frame_arvore_pesquisar_funcionario_cozinheiro, columns=("ID", "NOME", "CARGO"), show="headings")  
tree_pesquisar_funcionario_cozinheiro.heading("ID", text="ID")
tree_pesquisar_funcionario_cozinheiro.heading("NOME", text="Nome")
tree_pesquisar_funcionario_cozinheiro.heading("CARGO", text="Cargo") 
tree_pesquisar_funcionario_cozinheiro.grid(row=1, column=1, padx=10, pady=10)

botao_voltar_adm = Button(frame_arvore_pesquisar_funcionario_cozinheiro, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_funcionario, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=2, column=2)


#Pesquisar todos funcionários adm
frame_arvore_pesquisar_funcionario_tudo = Frame(home, bg=tema)

todos_ped_stat = Label(frame_arvore_pesquisar_funcionario_tudo, text="Todos os Funcionários", font = 'Arial 30 bold', bg=tema, fg=tema_text)
todos_ped_stat.grid(row=0, column=1,pady=(0,20))

tree_pesquisar_funcionario_tudo = ttk.Treeview(frame_arvore_pesquisar_funcionario_tudo, columns=("ID", "NOME", "CARGO"), show="headings")  
tree_pesquisar_funcionario_tudo.heading("ID", text="ID")
tree_pesquisar_funcionario_tudo.heading("NOME", text="Nome")
tree_pesquisar_funcionario_tudo.heading("CARGO", text="Cargo") 
tree_pesquisar_funcionario_tudo.grid(row=1, column=1, padx=10, pady=10)

botao_voltar_adm = Button(frame_arvore_pesquisar_funcionario_tudo, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_funcionario, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=2, column=2)


#Tipos de pesquisar funcionário adm
pesquisar_f = Frame(home, bg=tema)

title_label = Label(pesquisar_f, text="Pesquisar Funcionário:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=0, column=1, columnspan=2, pady=20)

title_label = Label(pesquisar_f, text="Cargo", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=1, column=1, columnspan=2, pady=20)

botao = Button(pesquisar_f, text = "Administrador", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_funcionario_button_by_administrador)
botao.grid(row = 2, column = 0, padx=(0,10))

botao = Button(pesquisar_f, text = "Garçom", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_funcionario_button_by_garcom)
botao.grid(row = 2, column = 1, padx=(0,10))

botao = Button(pesquisar_f, text = "Recepcionista", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_funcionario_button_by_recepcionista)
botao.grid(row = 2, column = 2, padx=(0,10))

botao = Button(pesquisar_f, text = "Cozinheiro", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_funcionario_button_by_cozinheiro)
botao.grid(row = 2, column = 3, padx=(0,10))

botao = Button(pesquisar_f, text = "Todos", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_funcionario_button_by_tudo)
botao.grid(row = 3, column = 1, columnspan=2, padx=(0,10), pady=20)

botao_voltar_adm = Button(pesquisar_f, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_funcionario_adm, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=4, column=3)



#Adicionar mesa adm
adicionar_m = Frame(home, bg=tema)

title_label = Label(adicionar_m, text="Adicionar mesa:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=0, column=1, pady=20)

id_mesa = Label(adicionar_m, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_mesa.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_mesa_entrada_adicionar = Entry(adicionar_m, width=25, font=("Arial, 24"))
id_mesa_entrada_adicionar.grid(row=1, column=1, padx=10, pady=5, sticky="w")

botao = Button(adicionar_m, text = "CADASTRAR", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = adicionar_mesa_button)
botao.grid(row = 2, column = 1, padx=(0,10))

botao_voltar_adm = Button(adicionar_m, text="Voltar", bg=tema, fg=tema_text, command = voltar_adicionar_mesa_adm, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=3, column=2)



#Alterar status mesa adm
alterar_m_adm = Frame(home, bg=tema)

title_alt = Label(alterar_m_adm, text="Alterar Status Mesa:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_alt.grid(row=0, column=1)

id_mesa = Label(alterar_m_adm, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_mesa.grid(row=1, column=1, padx=10, pady=5, sticky="e")

id_mesa_entry_adm = Entry(alterar_m_adm, width=25, font=("Arial, 24"))
id_mesa_entry_adm.grid(row=1, column=1, padx=10, pady=5, sticky="w")

alterar_mesa1_botao = Button(alterar_m_adm, text = "DISPONIVEL", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = alterar_disponivel_adm)
alterar_mesa1_botao.grid(row = 2, column = 1, padx=(0,10),pady=30)

alterar_mesa2_botao = Button(alterar_m_adm, text = "INDISPONIVEL", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = alterar_indisponivel_adm)
alterar_mesa2_botao.grid(row = 3, column = 1, padx=(0,10))

botao_voltar_adm = Button(alterar_m_adm, text="Voltar", bg=tema, fg=tema_text, command = voltar_alterar_mesa_adm, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=4, column=2)


#Excluir mesa adm
excluir_m = Frame(home, bg=tema)

title_label = Label(excluir_m, text="Excluir mesa:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=0, column=1, pady=20)

id_mesa = Label(excluir_m, text="ID: ",bg=tema, fg=tema_text, font=("Arial, 30"))
id_mesa.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_mesa_entrada_excluir = Entry(excluir_m, width=25, font=("Arial, 24"))
id_mesa_entrada_excluir.grid(row=1, column=1, padx=10, pady=5, sticky="w")

botao = Button(excluir_m, text = "CADASTRAR", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = excluir_mesa_button)
botao.grid(row = 2, column = 1, padx=(0,10))

botao_voltar_adm = Button(excluir_m, text="Voltar", bg=tema, fg=tema_text, command=voltar_excluir_mesa_adm, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=3, column=2)





#Pesquisar mesa disponivel adm
frame_arvore_pesquisar_mesa_disponivel = Frame(home, bg=tema)

todos_ped_stat = Label(frame_arvore_pesquisar_mesa_disponivel, text="Mesas Disponiveis:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped_stat.grid(row=0, column=1,pady=(0,20))

tree_pesquisar_mesa_disponivel = ttk.Treeview(frame_arvore_pesquisar_mesa_disponivel, columns=("ID", "DISPONIBILIDADE"), show="headings")  
tree_pesquisar_mesa_disponivel.heading("ID", text="ID")
tree_pesquisar_mesa_disponivel.heading("DISPONIBILIDADE", text="Disponibilidade")
tree_pesquisar_mesa_disponivel.grid(row=1, column=1, padx=10, pady=10)

botao_voltar_adm = Button(frame_arvore_pesquisar_mesa_disponivel, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_mesa, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=2, column=2)


#Pesquisar mesa indisponível adm
frame_arvore_pesquisar_mesa_indisponivel = Frame(home, bg=tema)

todos_ped_stat = Label(frame_arvore_pesquisar_mesa_indisponivel, text="Mesas Indisponiveis:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped_stat.grid(row=0, column=1,pady=(0,20))

tree_pesquisar_mesa_indisponivel = ttk.Treeview(frame_arvore_pesquisar_mesa_indisponivel, columns=("ID", "DISPONIBILIDADE"), show="headings")  
tree_pesquisar_mesa_indisponivel.heading("ID", text="ID")
tree_pesquisar_mesa_indisponivel.heading("DISPONIBILIDADE", text="Disponibilidade")

tree_pesquisar_mesa_indisponivel.grid(row=1, column=1, padx=10, pady=10)

botao_voltar_adm = Button(frame_arvore_pesquisar_mesa_indisponivel, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_mesa, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=2, column=2)




#Pesquisar todas as mesas adm  
frame_arvore_pesquisar_mesa_tudo = Frame(home, bg=tema)

todos_ped_stat = Label(frame_arvore_pesquisar_mesa_tudo, text="Todos os Mesas:", font = 'Arial 30 bold' ,bg=tema, fg=tema_text)
todos_ped_stat.grid(row=0, column=1,pady=(0,20))

tree_pesquisar_mesa_tudo = ttk.Treeview(frame_arvore_pesquisar_mesa_tudo, columns=("ID", "DISPONIBILIDADE"), show="headings")  
tree_pesquisar_mesa_tudo.heading("ID", text="ID")
tree_pesquisar_mesa_tudo.heading("DISPONIBILIDADE", text="Disponibilidade")
tree_pesquisar_mesa_tudo.grid(row=1, column=1, padx=10, pady=10)

botao_voltar_adm = Button(frame_arvore_pesquisar_mesa_tudo, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_mesa, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=2, column=2)


#Tipos de pesquisar mesa adm
pesquisar_m = Frame(home, bg=tema)

title_label = Label(pesquisar_m, text="Pesquisar Mesas:", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=0, column=1, columnspan=2, pady=20)

title_label = Label(pesquisar_m, text="Status", font = 'Arial 30 bold', bg=tema, fg=tema_text)
title_label.grid(row=1, column=1, columnspan=2, pady=20)

botao = Button(pesquisar_m, text = "Disponível", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_mesa_button_by_disponivel)
botao.grid(row = 2, column = 1, padx=(0,10))

botao = Button(pesquisar_m, text = "Indisponível", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_mesa_button_by_indisponivel)
botao.grid(row = 2, column = 2, padx=(0,10))

botao = Button(pesquisar_m, text = "Todos", font=("Arial", 24, "bold"), bg=tema, fg=tema_text, height=1,width=18, command = pesquisar_mesa_button_by_tudo)
botao.grid(row = 3, column = 1, columnspan=2, padx=(0,10), pady=20)

botao_voltar_adm = Button(pesquisar_m, text="Voltar", bg=tema, fg=tema_text, command=voltar_pesquisar_mesa_adm, font=("Arial", 15), width=10, height=1)
botao_voltar_adm.grid(row=4, column=3)





home.mainloop()


