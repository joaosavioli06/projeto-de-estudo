const idade = 11;
const carteirinha = true;

if (idade < 18){
    console.log('Você pode pagar MEIA');
} else if (idade <= 60 ) {
   
    if (carteirinha === true) {
    console.log('Mesmo você sendo adulta, você pode pagar MEIA');
    } else {
    console.log('Você sendo adulto e não tendo carteirinha, vai pagar INTEIRA');
    }    

} else {
    console.log('MEIA');
}






