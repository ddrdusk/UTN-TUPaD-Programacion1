def mostrar_resultados(num1, num2):
    print(f"\nNúmeros ingresados:")
    print(f" Número 1: {num1} -> Binario: {bin(num1)}")
    print(f" Número 2: {num2} -> Binario: {bin(num2)}")

    and_result = num1 & num2
    or_result = num1 | num2
    xor_result = num1 ^ num2

    print("\nResultados de operaciones bit a bit:")
    print(f" AND : {and_result} -> Binario: {bin(and_result)}")
    print(f" OR : {or_result} -> Binario: {bin(or_result)}")
    print(f" XOR : {xor_result} -> Binario: {bin(xor_result)}")

def main():
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        mostrar_resultados(num1, num2)
    except ValueError:
        print("⚠️ Por favor, ingrese solo números enteros válidos.")

if __name__ == "__main__":
    main()