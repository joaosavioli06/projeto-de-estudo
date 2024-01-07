const games = [
    {id: 1, gameName: 'Minecraft'},
    {id: 2, gameName: 'Fortnite'},
    {id: 3, gameName: 'Castle Crashers'},
    {id: 4, gameName: 'Terraria'},
    {id: 5, gameName: 'Dota 2'},
    {id: 6, gameName: 'Fifa 15'},
    {id: 7, gameName: 'Batman Arkham Asylum'},
    {id: 8, gameName: 'League Of Legends'},
    {id: 9, gameName: 'Overcooked'},
    {id: 10, gameName: 'Fall Guys'},
]

console.log(games.find(function(game) {
    return game.gameName == 'Fifa 15'
} ))