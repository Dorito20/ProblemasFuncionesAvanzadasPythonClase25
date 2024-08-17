#Deber: Modifica el programa para que también te permita dividir el total a pagar entre el número de personas que compartirán la cuenta.

def calcular_propina(total_cuenta, porcentaje_propina):
    propina = total_cuenta * (porcentaje_propina / 100)
    total_pagar = total_cuenta + propina
    return propina, total_pagar

# Ejemplo de uso
total_cuenta = float(input("Ingresa el total de la cuenta: "))
porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar: "))

propina, total_pagar = calcular_propina(total_cuenta, porcentaje_propina)

# Añadir número de personas
numero_personas = int(input("Ingresa el número de personas que compartirán la cuenta: "))

# Dividir el total a pagar entre el número de personas
pago_por_persona = total_pagar / numero_personas

print(f"Debes dejar una propina de: ${propina:.2f}")
print(f"El total a pagar es: ${total_pagar:.2f}")
print(f"Cada persona debe pagar: ${pago_por_persona:.2f}")
