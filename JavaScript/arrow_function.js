const shoes = [
    {id: 1, shoesModel: 'Nike SB'},
    {id: 2, shoesModel: 'OUS'},
    {id: 3, shoesModel: 'Vans'}
]

console.log(shoes.find(shoe => shoe.shoesModel == 'Nike SB'))

const cookies = [
    {id:1 , browser: 'Firefox'},
    {id:2 , browser: 'Vivaldi'},
    {id:3 , browser: 'Chrome'},
]

console.log(cookies.find(findCookie => findCookie.browser == 'Chrome'))