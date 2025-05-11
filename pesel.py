def verify_pesel(pesel: str) -> int:
    """
    Weryfikuje numer PESEL.

    Args:
        pesel (str): Numer PESEL w postaci ciągu 11 znaków.

    Returns:
        int: 1 jeśli numer jest poprawny, 0 jeśli nie.
    """
    if len(pesel) != 11 or not pesel.isdigit():
        print("Błąd: PESEL musi zawierać dokładnie 11 cyfr.")
        return 0

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = sum(int(pesel[i]) * weights[i] for i in range(10))
    kontrolna = (10 - (suma % 10)) % 10
    return 1 if kontrolna == int(pesel[10]) else 0


if __name__ == "__main__":
    pesel_input = input("Podaj numer PESEL (11 cyfr): ")
    wynik = verify_pesel(pesel_input)
    print(wynik)
