from avanzadas import OperacionesAvanzadas

if __name__ == "__main__":
    op = OperacionesAvanzadas()
    op.leerNumeros()
    resultado = op.elevarPotencia()
    print(f"El resultado de {op.num1} elevado a {op.num2} es: {resultado}")