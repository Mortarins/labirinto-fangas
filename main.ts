namespace SpriteKind {
    export const Sphinx = SpriteKind.create()
}
// Quiz
function quiz () {
    resposta = game.askForString("Quem é o deus do trovão? (a) Zeus (b) Hades")
    if (resposta.toLowerCase() == "a" || resposta.toLowerCase() == "zeus") {
        game.splash("Correto! Você venceu a Esfinge!")
        game.over(true)
    } else {
        game.splash("Errado! A Esfinge devorou você...")
        hero.destroy(effects.disintegrate, 500)
        pause(1000)
        game.over(false)
    }
}
// Evento: tocar a esfinge
sprites.onOverlap(SpriteKind.Player, SpriteKind.Sphinx, function (sprite, other) {
    game.splash("A Esfinge fala:", "Responda e prove seu valor!")
    quiz()
})
let hero: Sprite = null
// Aqui:
// 
// - "#" = parede sólida (automático, não atravessa)
// 
// - "." = caminho livre
let resposta = ""
// Personagem
hero = sprites.create(img`
    ....................
    ....................
    ....................
    ....................
    ....................
    ....................
    .......22222........
    ......2222222.......
    ......2222222.......
    .....22222222.......
    .....222222222......
    ....b222555222b.....
    ....22222222222.....
    ....22112221122.....
    ....21d222.1d2......
    ....21d2...1d1......
    .....1d1...1d1......
    .....111...111......
    ......f.....f.......
    ....................
    `, SpriteKind.Player)
controller.moveSprite(hero, 100, 100)
scene.cameraFollowSprite(hero)
// --- LABIRINTO PRONTO EM CÓDIGO ---
tiles.setTilemap(tilemap`labirinto de pimpas0`)
// Coloca herói na entrada
tiles.placeOnTile(hero, tiles.getTileLocation(10, 1))
// Esfinge
let sphinx = sprites.create(img`
    . . . . f f f f f f . . . . 
    . . . f e e e e e e f . . . 
    . . f e e e e e e e e f . . 
    . . f e e e e e e e e f . . 
    . . f e e f f f f e e f . . 
    . . f e e f e e f e e f . . 
    . . f e e e e e e e e f . . 
    . . . f e e e e e e f . . . 
    . . . . f f e e f f . . . . 
    . . . . . . f f . . . . . . 
    `, SpriteKind.Sphinx)
tiles.placeOnTile(sphinx, tiles.getTileLocation(2, 24))
