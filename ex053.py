'''Crie um programa que leia uma frase qualquer e diga
se ela é um palindromo, desconsiderando os espaços
EX:
    APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DATA DA MARATONA'''
frase = str(input('Digite uma frase: ')).strip() .upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A frase inversa de "{}" é "{}"'.format(frase, junto))
if inverso == junto:
    print('A frase é um PALINDROMO!')
else:
    print('A frase NÃO é um PALINDROMO!')



