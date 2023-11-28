let produto1 = 10.50
let produto2 = 2.75
let produto3 = 12.27 

let compras = 0

if (produto1 <= 11) {
    console.log('Comprei o produto 1')
    compras += produto1 
}

if (produto2 < 4) {
    if (produto2 <= 3.50) {
        console.log('Comprei o produto 2')
        compras += produto2     
    } else 
        console.log('Tem algo de errado com o preço do produto 2')
}

if (produto3 <= 14) {
    console.log('Comprei o produto 3')
    compras += produto3 
}

console.log('No total da compra na padaria, eu gastei', compras, 'reais')





