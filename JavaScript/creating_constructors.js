// Constructor

function CreateShoes (brand, color, size) {
    this.Shoesbrand = brand;
    this.Shoescolor = color;
    this.Shoessize = size;
}

const allstar = new CreateShoes ('Converse', 'Blue', 41)

allstar.year = 1975

// Fiz um teste para ver se é possível criar um parâmetro novo dentro de um constructor

console.log(allstar)

function CreatePerson (name, age, country, hobby) {
    this.personname = name;
    this.personage = age;
    this.personcountry = country;
    this.personhobby = hobby;
}

const Andrew = new CreatePerson ('Andrew', 22, 'Canada', 'Reading')

console.log(Andrew)

const Andressa = new CreatePerson ('Andressa', 26, 'Brazil', 'Cooking')

Andressa.favoritecolor = 'Pink'

console.log(Andressa)