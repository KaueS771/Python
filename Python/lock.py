
# Este código cria um lock,
# adquire-o antes de executar uma seção crítica (neste caso, apenas uma instrução `print`),
# e garante que o lock seja liberado após a execução,
# independentemente de erros. Os locks são úteis para sincronizar o acesso a recursos compartilhados em programas multithreaded.
import threading
some_lock = threading.Lock()


some_lock.acquire()
try:
    print('Look at me: I design coastline.\n'
          'I got an award for Norway'
    )
finally:
    some_lock.release()