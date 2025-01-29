//Somar todos os números de um array

const numeros = [8, 27, 1, 5, 2, 8]

const somaNumeros = numeros.reduce((acc, num) => acc + num, 0)

console.log(somaNumeros)