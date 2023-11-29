let maca = 1
let banana = 2
let melancia = 3
let pera = 4


let banca = 7

if (banca >= 10) {
    console.log('Você pode comprar todas as frutas!')
    banca -= maca + banana + melancia + pera
} else {
    console.log('Você não pode comprar todas as frutas')
}


console.log('Sobrou R$',banca, 'Reais')