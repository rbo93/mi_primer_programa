pokemon_elegido = input("Contra que pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ").lower()
while pokemon_elegido != "squirtle" and pokemon_elegido != "charmander" and pokemon_elegido != "bulbasaur":
    print("Elige una opcion correcta")
    pokemon_elegido = input("Contra que pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ").lower()

vida_pikachu = 100
vida_enemigo = 0
dano_recibido = 0

if pokemon_elegido == "squirtle":
    vida_enemigo = 90
    dano_recibido = 8

elif pokemon_elegido == "charmander":
    vida_enemigo = 80
    dano_recibido = 7

elif pokemon_elegido == "bulbasaur":
    vida_enemigo = 100
    dano_recibido = 10

print("Que comience el combate!!")
print("Vida inicial de {} : {}".format(pokemon_elegido, vida_enemigo))
print("Vida inicial de Pikachu: 100")

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("Que ataque deseas usar? (Chispazo / Bola voltio): ").lower()
    while ataque_elegido != "chispazo" and ataque_elegido != "bola voltio":
        print("Elige una opcion correcta")
        ataque_elegido = input("Que ataque deseas usar? (Chispazo / Bola voltio): ").lower()
    if ataque_elegido == "chispazo":
        vida_enemigo -= 10
        print("Has inflingido 10 de daño")
    elif ataque_elegido == "bola voltio":
        vida_enemigo -= 12
        print("Has inflingido 12 de daño")
    vida_pikachu -= dano_recibido
    print("{} te ha hecho {} de daño".format(pokemon_elegido,dano_recibido))
    if vida_pikachu < 0 :
        vida_pikachu = 0
    elif vida_enemigo < 0 :
        vida_enemigo = 0

    print("Vida Pikachu: {}: ".format(vida_pikachu))
    print("Vida {} : {} ".format(pokemon_elegido, vida_enemigo))

print ("Combate finalizado!")
if vida_pikachu == 0:
    print("El enemigo te ha derrotado")
else:
    print("Has ganado el combate!!")

