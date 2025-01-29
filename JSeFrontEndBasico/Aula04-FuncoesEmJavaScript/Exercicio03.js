//Crie uma função de seta que receba um array de nomes de alunos e depois imprima todos os nomes em maiúsculo (uppercase). 

const upperCase = (listaNomes) => {
    for (let i = 0; i < listaNomes.length; i++) {
        console.log(listaNomes[i].toUpperCase())
    }
}

upperCase(['Pessoa 1', 'Pessoa 2', 'Pessoa 3', 'Pessoa ...'])