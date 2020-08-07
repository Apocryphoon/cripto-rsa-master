import random
from tqdm import tqdm
from time import sleep


def prime(n):
    if (n <= 1):
        return (False)
    elif (n <= 3):
        return (True)

    if (n % 2 == 0 or n % 3 == 0):
        return (False)

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return (False)

        i += 6

    return (True)


def totient(number):
    if (prime(number)):
        return (number - 1)

    else:
        return (False)


def mdc(n1, n2):
    rest = 1

    while (n2 != 0):
        rest = n1 % n2
        n1 = n2
        n2 = rest

    return (n1)


def generate_E(num):
    e = random.randrange(2, num)
    if (mdc(num, e) == 1):
        return (e)
    return (e)


def generate_prime():
    while True:
        x = random.randrange(1, 100)

        if (prime(x) == True):
            return (x)


def mod(a, b):
    if (a < b):
        return (a)
    else:
        c = a % b
        return (c)


# d = 0
# Ele estava dando 0 na primeira vez que tu rodava o código pq tu estava declarando ela como 0 aqui

def calculate_private_key(toti, e):
    d = 0

    while True:

        d = random.randrange(1, 1000)

        if (prime(d) == True):
            return (d)

    return (d)


# private = d
# Ele nunca dava certo pq tu não entrava na função do calculate_private_key pq tu não chamava, então foi só adicionar 1 linhas de código na parte de descriptar

def cipher(words, e, n):
    tam = len(words)
    lista = []

    for i in range(tam):
        letter = words[i]
        k = ord(letter)
        k = k ** e
        d = mod(k, n)
        lista.append(d)

    return (lista)


def descifra(cifra, n, d):
    lista = []
    tam = len(cifra)

    for i in range(tam):
        result = cifra[i] ** d
        texto = mod(result, n)
        letra = chr(texto)
        lista.append(letra)

    return (lista)


# if __name__ == "__main__":
# Retirei isso pq estava criando um escopo que zerava após a primeira vez que o while rodava, isso não é necessário

p = generate_prime()  # generates random P
q = generate_prime()  # generates random Q
n = p * q  # compute N
y = totient(p)  # compute the totient of P
x = totient(q)  # compute the totient of Q
totient_de_N = x * y  # compute the totient of N
e = generate_E(totient_de_N)  # generate E
d = calculate_private_key(totient_de_N, e)  # Adicionei essa linha para gerar a chave privada
public_key = (n, e)

while True:
    print('''
[ 1 ] Criptografar
[ 2 ] Descriptografar
[ 3 ] Sair
        ''')

    opcao = int(input("Qual é a sua opção?"))
    opcao != 3

    if opcao == 1:
        text = input("Digite a menssagem a ser encriptada: ")

        print("=-= " * 15)
        print("Processo de encriptação em andamento, aguarde!")

        for i in tqdm(range(len(text))):
            ...
            sleep(0.01)
        print("=-= " * 15)

        # Cifra um texto

        print('Sua chave publica é:', public_key)
        text_cipher = cipher(text, e, n)
        print('Sua chave privada é:', d)
        print('Sua menssagem encriptada:', text_cipher)
        print("=-= " * 15)


    elif opcao == 2:

        valor = int(input('Informe a chave privada:'))

        if valor != d:

            print('Chave incorreta!')

        else:

            print('Chave informada corretamente!')
            print('Desencriptando')

            for i in tqdm(range(len(text))):
                ...
                sleep(0.01)

    elif opcao == 3:
        break