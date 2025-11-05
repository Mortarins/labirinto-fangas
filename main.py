@namespace
class SpriteKind:
    Sphinx = SpriteKind.create()
# Quiz
def quiz():
    global resposta
    resposta = game.ask_for_string("Quem é o deus do trovão? (a) Zeus (b) Hades")
    if resposta.to_lower_case() == "a" or resposta.to_lower_case() == "zeus":
        game.splash("Correto! Você venceu a Esfinge!")
        game.over(True)
    else:
        game.splash("Errado! A Esfinge devorou você...")
        hero.destroy(effects.disintegrate, 500)
        pause(1000)
        game.over(False)
# Evento: tocar a esfinge

def on_on_overlap(sprite, other):
    game.splash("A Esfinge fala:", "Responda e prove seu valor!")
    quiz()
sprites.on_overlap(SpriteKind.player, SpriteKind.Sphinx, on_on_overlap)

hero: Sprite = None
# Aqui:
# 
# - "#" = parede sólida (automático, não atravessa)
# 
# - "." = caminho livre
resposta = ""
# Personagem
hero = sprites.create(img("""
        . . . . . . . . . . . . . .
        . . . . . . . . . . . . . .
        . . . . . . . 3 3 3 . . . .
        . . . . . . . 3 . 3 . . . .
        . . . . 3 3 3 . . 3 . . . .
        . . 3 3 3 . 3 3 3 3 . . . .
        . . 3 . 3 3 . 3 3 . . . . .
        . . 3 . 3 . 3 3 3 . . . . .
        . . 3 . 3 . . 3 3 3 . . . .
        . . . 3 3 . . . 3 3 . . . .
        . . . . 3 . . . . . . . . .
        . . . . . . . . . . . . . .
        . . . . . . . . . . . . . .
        """),
    SpriteKind.player)
controller.move_sprite(hero, 100, 100)
scene.camera_follow_sprite(hero)
# --- LABIRINTO PRONTO EM CÓDIGO ---
tiles.set_tilemap(tilemap("""
    labirinto de pimpas
    """))
# Coloca herói na entrada
tiles.place_on_tile(hero, tiles.get_tile_location(10, 1))
# Esfinge
sphinx = sprites.create(img("""
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
        """),
    SpriteKind.Sphinx)
tiles.place_on_tile(sphinx, tiles.get_tile_location(14, 13))