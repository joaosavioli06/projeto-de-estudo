function Createshirt (brand, color, size) { 
    shirt = {
        Shirtbrand: brand,
        Shirtcolor: color,
        Shirtsize: size
    }
    return shirt
}

const shirt1 = Createshirt('Tommy Hilfiger', 'Blue', 'S')
console.log(shirt1)

shirt1.Shirtyear = 2021

console.log(shirt1)