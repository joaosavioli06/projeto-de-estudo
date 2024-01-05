// Criação de objeto simples e factory

table = {
    wood: true,
    size: 'small',
    year: 2022,
    situation: 'Perfect'
}

console.log(table)

function Createbook (author, year, pages) {
    book = {
        Bookauthor: author,
        Bookyear: year,
        Bookpages: pages
    } 
    return book
}

const Firstbook = Createbook ('John', 2003, 212)
console.log(Firstbook)

