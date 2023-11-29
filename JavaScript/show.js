idade = 29
ticket = false

if (idade >= 18)
    console.log('Você pode entrar no show sem os responsáveis')
else if (idade <= 17 && ticket ==true)
    console.log('Você pode entrar sozinho, mesmo sendo menor de idade')
else 
    console.log('Você precisa entrar com seus pais')