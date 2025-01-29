/*Spread Operator - Combine e clone arrays
Crie um único array chamado combined que contenha todos os elementos dos dois arrays, e crie um array chamado clonedArray que seja uma cópia do array1.*/

const array1 = [1, 2, 3];
const array2 = [4, 5, 6];

const combined = [...array1, ...array2]
const ClonedArray = [...array1]

console.log(combined)
console.log(ClonedArray)