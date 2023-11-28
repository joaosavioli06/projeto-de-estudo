const idade = 69
const carteirinha = true

const adulta = idade >=18 && idade <= 60 

if (idade <18 || idade > 60 || adulta && carteirinha == true){
    console.log('Você pode pagar MEIA')
}else{
    console.log('Você deve pagar INTEIRA')
}