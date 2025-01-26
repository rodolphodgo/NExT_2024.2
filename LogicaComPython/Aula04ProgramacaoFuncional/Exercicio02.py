'''Filtrar palavras que começam com uma letra específica

Dada a lista palavras = ["python", "java", "javascript", "c++", "c#", "ruby", "go"], use filter para obter as palavras que começam com a letra "j".

'''

palavras = ["python", "java", "javascript", "c++", "c#", "ruby", "go"]

filtradas = list(filter(lambda p: p[0] == "j", palavras))

print(filtradas)