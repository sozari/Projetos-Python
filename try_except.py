try:
    print("hello"+5)
except NameError:
    print("um NameError ocorreu")
except TypeError:
    print("erro: TypeError")
finally:
    print("O bloco try excepct terminou agora")
