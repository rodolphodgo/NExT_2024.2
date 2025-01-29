//Crie uma função chamada ehPar que receba um número como parâmetro e retorne true se o número for par, ou false caso contrário. 

function ehPar(numero) {
    return numero % 2 === 0 ? 'É par' : 'É ímpar'
}

console.log(ehPar(5))
console.log(ehPar(6))