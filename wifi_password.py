import tkinter as tk
from tkinter import messagebox
import pyautogui
import time

def verificar_senha():
    senha_digitada = entrada_senha.get()
    if senha_digitada == "bruteforce":  # Substitua "senha123" pela sua senha desejada
        janela_principal.deiconify()  # Mostra a janela principal
        janela_login.withdraw()  # Esconde a janela de login
        executar_comandos()
    else:
        messagebox.showerror("Erro", "Senha incorreta!")

def executar_comandos():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('cmd')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('color a ')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('netsh wlan show profiles')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('netsh wlan show profiles #SEDUC_TABLET key=clear')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.write('exit')
    pyautogui.press('enter')

# Cria a janela principal
janela_principal = tk.Tk()
janela_principal.title("Minha Janela")
janela_principal.geometry("400x300")

# Cria a janela de login
janela_login = tk.Toplevel(janela_principal)
janela_login.title("Login")
janela_login.geometry("200x100")
janela_login.attributes('-topmost', True)  # Mantém a janela de login na frente

# Adiciona um campo de senha e um botão de login na janela de login
tk.Label(janela_login, text="Senha:").pack()
entrada_senha = tk.Entry(janela_login, show="*")
entrada_senha.pack()
botao_login = tk.Button(janela_login, text="Login", command=verificar_senha)
botao_login.pack()

# Esconde a janela principal
janela_principal.withdraw()

# Inicia o loop principal da aplicação
janela_principal.mainloop()
