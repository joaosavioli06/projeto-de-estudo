let e = ['e']

let verifyE = e.every (function (E) {
    return E == 'e'
})

console.log(verifyE)

let positiveNum = [-1, 0, 1, 2, 3, 4, 5]

let verifyNum = positiveNum.every(function (positive) {
    return positive >= 0
})

console.log(verifyNum)