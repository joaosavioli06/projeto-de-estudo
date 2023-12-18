let salario = 3000
let horasExtras = 0

if (horasExtras > 0 && horasExtras <= 5){
    console.log (salario += 500)
} else if (horasExtras > 6 && horasExtras <= 10){
    console.log (salario += 700)
} else if (horasExtras >= 11){
    console.log (salario += 950)
} else {
    console.log('Sem ganho de hora extra desta vez')
}

