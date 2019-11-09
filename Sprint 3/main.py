import tkinter as tk


def interface_gui():
    window = tk.Tk()
    liste_numero = []

    # Affichage de l'écriture de chiffre
    affichage_numero = tk.Label(window, relief="ridge", padx=70)
    affichage_numero.grid(row=1, column=2)
    numero = affichage_numero.cget("text")
    affichage_numero["text"] = numero

    def add_char(char):
        affichage_numero["text"] = ""
        liste_numero.append(char)
        for position_char in range(len(liste_numero)):
            affichage_numero["text"] += str(liste_numero[position_char])

    # Affichage des chiffres
    chiffre_1 = tk.Button(window, text="1", padx=20, command=lambda: add_char("1"))
    chiffre_1.grid(row=2, column=1)
    chiffre_2 = tk.Button(window, text="2", padx=20, command=lambda: add_char("2"))
    chiffre_2.grid(row=2, column=2)
    chiffre_3 = tk.Button(window, text="3", padx=20, command=lambda: add_char("3"))
    chiffre_3.grid(row=2, column=3)
    chiffre_4 = tk.Button(window, text="4", padx=20, command=lambda: add_char("4"))
    chiffre_4.grid(row=3, column=1)
    chiffre_5 = tk.Button(window, text="5", padx=20, command=lambda: add_char("5"))
    chiffre_5.grid(row=3, column=2)
    chiffre_6 = tk.Button(window, text="6", padx=20, command=lambda: add_char("6"))
    chiffre_6.grid(row=3, column=3)
    chiffre_7 = tk.Button(window, text="7", padx=20, command=lambda: add_char("7"))
    chiffre_7.grid(row=4, column=1)
    chiffre_8 = tk.Button(window, text="8", padx=20, command=lambda: add_char("8"))
    chiffre_8.grid(row=4, column=2)
    chiffre_9 = tk.Button(window, text="9", padx=20, command=lambda: add_char("9"))
    chiffre_9.grid(row=4, column=3)
    chiffre_0 = tk.Button(window, text="0", padx=20, command=lambda: add_char("0"))
    chiffre_0.grid(row=5, column=2)
    etoile = tk.Button(window, text="*", padx=20, command=lambda: add_char("*"))
    etoile.grid(row=5, column=1)
    diese = tk.Button(window, text="#", padx=20, command=lambda: add_char("#"))
    diese.grid(row=5, column=3)

    # Bouton pour appeler
    appeler = tk.Button(window, text="Appeler", padx=50)
    appeler.grid(row=6, column=2)

    # Affichage des contacts
    afficher_contact = tk.Label(window, text="Afficher contacts", relief="groove")
    afficher_contact.grid(row=2, column=4)

    # Naviguer dans les contacts enregistrés
    fleche_up = tk.Button(window, text="up")
    fleche_up.grid(row=3, column=4)
    fleche_down = tk.Button(window, text="down")
    fleche_down.grid(row=4, column=4)

    # Actions
    boite_vocale = tk.Button(window, text="Ecouter messages")
    boite_vocale.grid(row=5, column=4)

    window.mainloop()


if __name__ == '__main__':
    interface_gui()
