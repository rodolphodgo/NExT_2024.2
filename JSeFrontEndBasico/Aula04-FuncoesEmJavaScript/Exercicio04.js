//Crie uma função que receba um array de números e retorne um novo array contendo apenas os números pares 

function soPares(numeros){
    return numeros.filter(numero => numero % 2 === 0)
}

listaNumeros = [5, 2, 0, 7, 20, 15]

console.log(soPares(listaNumeros))