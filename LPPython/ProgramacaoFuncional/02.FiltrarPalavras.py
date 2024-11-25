palavras = ["python", "java", "javascript", "c++", "c#", "ruby", "go"]

filtradas = list(filter(lambda p: p[0] == "j", palavras))

print(filtradas)