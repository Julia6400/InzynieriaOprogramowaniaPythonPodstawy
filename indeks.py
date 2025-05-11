import re
from collections import defaultdict, Counter

def index_documents(documents: list[str], queries: list[str]) -> list[list[int]]:
    """
    Przetwarza dokumenty i zapytania, zwracając listy indeksów dokumentów,
    w których występuje zapytanie, posortowane według częstości wystąpienia
    danego wyrazu (malejąco), a w przypadku równych częstości - malejąco wg numeru dokumentu.

    Args:
        documents (list[str]): Lista dokumentów (każdy dokument to ciąg znaków).
        queries (list[str]): Lista zapytań (każdy zapytanie to pojedynczy wyraz).

    Returns:
        list[list[int]]: Lista wyników dla kolejnych zapytań.
    """
    # Przetwarzanie dokumentów: usuwanie interpunkcji, zamiana na małe litery, liczenie słów
    doc_word_counts = []
    for doc in documents:
        words = re.findall(r'\b\w+\b', doc.lower())
        counter = Counter(words)
        doc_word_counts.append(counter)

    results = []
    for query in queries:
        query = query.lower()
        freq_list = []
        for i, counter in enumerate(doc_word_counts):
            count = counter.get(query, 0)
            if count > 0:
                freq_list.append((count, -i))  # -i bo sortujemy malejąco wg numeru dokumentu w razie remisu
        # Sortowanie: najpierw po częstości malejąco, potem po indeksie dokumentu malejąco
        freq_list.sort(reverse=True)
        sorted_doc_ids = [-idx for _, idx in freq_list]
        results.append(sorted_doc_ids)
    return results


# Przykładowe wywołanie:
if __name__ == "__main__":
    # Pobranie liczby dokumentów
    n = int(input("Podaj liczbę dokumentów: "))
    documents = []
    print("Wprowadź kolejne dokumenty:")
    for _ in range(n):
        documents.append(input())

    # Pobranie liczby zapytań
    m = int(input("Podaj liczbę zapytań: "))
    queries = []
    print("Wprowadź kolejne zapytania:")
    for _ in range(m):
        queries.append(input().strip())

    # Przetworzenie zapytań
    results = index_documents(documents, queries)

    # Wypisanie wyników
    print("Wyniki:")
    for res in results:
        print(res)
