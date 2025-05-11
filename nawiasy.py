def check_parentheses(s: str) -> bool:
    """
    Sprawdza, czy w ciągu znaków 's' nawiasy okrągłe są poprawnie sparowane.

    Args:
        s (str): Ciąg znaków do analizy.

    Returns:
        bool: True jeśli nawiasy są poprawne, False w przeciwnym wypadku.
    """
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False  # Zbyt wiele nawiasów zamykających
            stack.pop()
    return len(stack) == 0  # True tylko jeśli wszystkie nawiasy zostały zamknięte


# Przykładowe wywołanie:
if __name__ == "__main__":
    examples = [
        "( if ( zero ? x ) max (/ 1 x ))",
        "I told ( that its not ( yet ) done ). (42)",
        ":-)",
        "Czesc (o kurcze, chyba niechcacy zamkne ten nawias dwa razy))",
        "())(("
    ]
    for example in examples:
        print(f"{example} -> {check_parentheses(example)}")
