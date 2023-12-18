let canGo = false
let idade = 11

if (canGo == true && idade <= 17){
    console.log ('Sua mãe até deixou você ir, mas você não tem idade para isso, não vamos te levar')
} else if (canGo == false && idade >= 18) {
    console.log('Sua mãe não deixou você ir, mas você já tem idade, vamos nessa!')
} else if (canGo == true && idade >= 18) {
    console.log ('Sua mãe deixou e você já tem idade para isso, você tem sorte!')
} else {
    console.log('Você não pode ir mesmo maninho...')
}

