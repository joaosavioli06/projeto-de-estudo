const mouse = {
    marca: 'Redragon',
    cor: 'Branca',
    modelo: 'Cobra',
    dataCompra: 2022,
    siteCompra: 'Kabum',
    avaliacao: '5 out of 5',
}

console.log(mouse)

for (i in mouse){
    console.log(i, mouse[i])
}

const mesa = {
    livros: 12,
    monitor: 'LG',
    azulejo: 'Red Hot Chili Peppers',
    funko: 'Ginger bread',
    portaCanetas: {
        canetas: 9,
        lapis: 5,
        cola: 1,
    }
}

console.log(mesa)