//Dada uma lista de números, crie um novo array contendo apenas os números que são pares.

const numeros = [8, 27, 1, 5, 2, 8]

const numerosPares = numeros.filter(num => num % 2 === 0)

console.log(numerosPares)