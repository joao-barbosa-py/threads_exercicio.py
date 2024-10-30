import webbrowser
import threading
import time

def comentar(site):
    print(f"Entrando no site: {site}")
    time.sleep(5)
    print(f"Dados processados no sit: {site}")
threads = []

for site in range(100):
    nova_thread = threading.Thread(target=comentar, args=(site,))
    threads.append(nova_thread)

for thread in threads:
    thread.start()
    # Print iniciando {thread.name}

for thread in threads:
    thread.join()
    # print(f"Finalizando {thread.name}")