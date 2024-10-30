import webbrowser
import threading
import time

def extrair_precos(site, produto):
    print(f"navegando até o site {site} e pesquisando sobre {produto}")
    time.sleep(3)
    print(f"{produto} processado com sucesso")

threads = []
produtos = ["Câmera", "Secador de cabelo", "Samsung galaxy S24", "Acer aspire 3", "Joystick"]

for i in range(5):
    nova_thread = threading.Thread(
        target=extrair_precos, args= ("https://www.mercadoexemplo.com", produtos[i])
    )
    threads.append(nova_thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()