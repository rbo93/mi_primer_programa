apetece_helado_input = input("Te apetece un helado? (SI/NO): ").upper()
tiene_dinero_input = input("Tienes dinero para un helado? (SI/NO): ").upper()
esta_heladero_input = input("Esta el heladero? (SI/NO)").upper()
esta_tia_input = input("Esta tu tia? SI/NO").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Solo podias responder SI o NO, lo tomare como un NO")
    apetece_helado = False

puedes_afrontar = tiene_dinero_input == "SI" or esta_tia_input == "SI"
esta_heladero = esta_heladero_input == "SI"

if apetece_helado and puedes_afrontar and esta_heladero:
    print("Compraremos el helado")
else:
    print ("Noc compraremos el helado")
