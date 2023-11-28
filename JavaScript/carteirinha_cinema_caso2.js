const idade = 20
const carteirinha = false

const éadulto = idade >= 18 && idade <= 60

if (éadulto && carteirinha == false ) {
    console.log('Você pode entrar no cinema pagando INTEIRA')
} else {
    console.log('Vai entrar pagando MEIA')
}
