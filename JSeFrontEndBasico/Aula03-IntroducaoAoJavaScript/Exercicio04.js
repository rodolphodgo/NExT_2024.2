//Crie um objeto user com age 25 para atualizar para 30 e adicione uma nova propriedade isStudent: true sem modificar o objeto original.
const user = {
    name: 'Alice',
    age: 25,
    location: 'New York',
  };
  
  console.log(user)
  
  const updatedUser = { ...user, age: 30, isStudent: true }

  console.log(updatedUser)
  