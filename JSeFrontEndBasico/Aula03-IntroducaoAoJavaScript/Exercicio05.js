//Crie uma nova variável chamada productName que armazene o nome do produto e um objeto batata que contenha todas as outras propriedades do produto.

const product = {
    id: 1,
    name: 'Notebook',
    price: 1500,
    category: 'Electronics',
};
  
const { name: productName, ...batata } = product

console.log(productName)
console.log(batata)