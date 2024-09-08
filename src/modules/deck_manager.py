from file_operations import save_decks, load_decks

decks = load_decks()

def create_deck():
    deck_name = input("Ingrese el nombre del nuevo mazo: ")
    if deck_name not in decks:
        decks[deck_name] = []
        save_decks(decks)
        print(f"Mazo '{deck_name}' creado exitosamente.")
    else:
        print("El mazo ya existe.")

def list_decks():
    print("Mazos disponibles:")
    for deck_name in decks:
        print(f"- {deck_name}")