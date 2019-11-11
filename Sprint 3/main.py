import tkinter as tk


def interface_gui():
    window = tk.Tk()
    liste_numero = []
    dict_numero = {}

    # Affichage de l'écriture de chiffre
    affichage_numero_pad = tk.Label(window, relief="ridge", padx=70)
    affichage_numero_pad.grid(row=1, column=2)
    numero = affichage_numero_pad.cget("text")
    affichage_numero_pad["text"] = numero

    def add_char(char):
        affichage_numero_pad["text"] = ""
        liste_numero.append(char)
        for position_char in range(len(liste_numero)):
            affichage_numero_pad["text"] += str(liste_numero[position_char])

    def delete_char():
        del liste_numero[-1]
        affichage_numero_pad["text"] = ""
        for position_char in range(len(liste_numero)):
            affichage_numero_pad["text"] += str(liste_numero[position_char])

    def enregistrer():
        def callback():
            dict_numero[affichage_numero_pad["text"]] = nom.get()
            window_name.destroy()

        window_name = tk.Toplevel(window)
        nom_label = tk.Label(window_name, text="Veuillez entrer le nom du nouveau contact :")
        nom_label.grid(row=1, column=1)
        nom = tk.Entry(window_name)
        nom.grid(row=2, column=1)
        enter = tk.Button(window_name, text="Enregistrer", command=callback)
        enter.grid(row=3, column=1)

    def supprimer():
        print(dict_numero)

    def affichage_contact():
        print("oui")

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
    supp_char = tk.Button(window, text="<-", padx=20, command=delete_char)
    supp_char.grid(row=6, column=1)

    # Bouton pour appeler
    appeler = tk.Button(window, text="Appeler", padx=50)
    appeler.grid(row=6, column=2)

    # Affichage des contacts
    afficher_contact = tk.Label(window, text="Afficher contacts", relief="groove")
    afficher_contact.grid(row=2, column=4)

    # Naviguer dans les contacts enregistrés
    fleche_up = tk.Button(window, text="up")
    fleche_up.grid(row=2, column=5)
    fleche_down = tk.Button(window, text="down")
    fleche_down.grid(row=2, column=6)

    # Actions
    supprimer_contact = tk.Button(window, text="Supprimer ce contact", command=supprimer)
    supprimer_contact.grid(row=3, column=4)

    enregistrer = tk.Button(window, text="Enregistrer ce numéro", command=enregistrer)
    enregistrer.grid(row=4, column=4)

    boite_vocale = tk.Button(window, text="Ecouter messages")
    boite_vocale.grid(row=5, column=4)

    historique = tk.Button(window, text="Voir historique appels")
    historique.grid(row=6, column=4)
    window.mainloop()


if __name__ == '__main__':
    interface_gui()
