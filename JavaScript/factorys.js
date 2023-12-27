function Tshirt (size, price, brand) {
    camiseta = {
        tamanho: size,
        preco: price,
        marca: brand,
    }
    return camiseta
} 

const camisetaL = Tshirt('M', 250, 'Lacoste')
console.log(camisetaL);

function lanche (sabor, tamanho, validade, Lugarfabricacao) {
    lanche = {
        sabor: sabor,
        tamanho: tamanho,
        validade: validade,
        Lugarfabricacao: Lugarfabricacao,
    }
    return lanche
}

const Bigmac = lanche('Carne', 'Médio', '3 dias', 'MC Donalds')
console.log(Bigmac)