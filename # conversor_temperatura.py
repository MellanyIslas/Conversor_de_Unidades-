# conversor_temperatura.py

def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.
    Fórmula: (Celsius * 9/5) + 32
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == "__main__":
    print("--- Conversor de Temperatura: Celsius a Fahrenheit ---")
    try:
        grados_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
        grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)
        print(f"\n{grados_celsius}°C equivale a {grados_fahrenheit:.2f}°F")
    except ValueError:
        print("\nError: Por favor, introduce un valor numérico válido.")