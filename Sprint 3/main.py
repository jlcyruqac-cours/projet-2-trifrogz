import tkinter as tk


def interface_gui():
    window = tk.Tk()
    window.title("Software softphone")

    class LoginDialog(tk.Toplevel):
        def __init__(self, parent):
            super().__init__(parent)
            self.title("Fenêtre Modale")
            # ---------------------------------------
            tk.Label(self, text="Login : ").pack()
            self.entry_login = tk.Entry(self)
            self.entry_login.insert(0, "defaultlogin")
            self.entry_login.pack()
            # ---------------------------------------
            tk.Label(self, text="Clé : ").pack()
            self.entry_pass = tk.Entry(self, show='*')
            self.entry_pass.insert(0, "defaultpass")
            self.entry_pass.pack()
            # ---------------------------------------
            tk.Button(self, text="Connexion", command=self.connect).pack()

        def connect(self):
            login = self.entry_login.get().strip()
            key = self.entry_pass.get().strip()

            self.destroy()

    def connect():
        """ Ouvre une fenêtre modale """
        result = LoginDialog(window)
        result.transient(window)
        result.grab_set()
        window.wait_window(result)

    class Fenetre(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.master.title("Fenêtre principale")
            self.grid(row=1, column=1)
            bouton_new = tk.Button(self, width=10, height=1, text="Connexion", command=connect)
            bouton_new.grid(row=1, column=2)
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

            # Actions
            voir_contact = tk.Button(window, text="Voir les contacts", command=display_contact)
            voir_contact.grid(row=2, column=4)

            boite_vocale = tk.Button(window, text="Ecouter messages")
            boite_vocale.grid(row=3, column=4)

            historique = tk.Button(window, text="Voir historique appels")
            historique.grid(row=4, column=4)
            window.mainloop()

    liste_affichage_numero = []
    liste_nom_contact = []
    liste_numero_contact = []
    dict_numero = {"numero_contact": liste_numero_contact, "nom_contact": liste_nom_contact}

    # Affichage de l'écriture de chiffre
    affichage_numero_pad = tk.Label(window, relief="ridge", padx=70)
    affichage_numero_pad.grid(row=1, column=2)

    affichage_numero_pad["text"] = affichage_numero_pad.cget("text")

    def add_char(char):
        affichage_numero_pad["text"] = ""
        liste_affichage_numero.append(char)
        for position_char in range(len(liste_affichage_numero)):
            affichage_numero_pad["text"] += str(liste_affichage_numero[position_char])

    def delete_char():
        if liste_affichage_numero:
            del liste_affichage_numero[-1]
            affichage_numero_pad["text"] = ""
            for position_char in range(len(liste_affichage_numero)):
                affichage_numero_pad["text"] += str(liste_affichage_numero[position_char])

    def enregistrer():
        def callback():
            nom_contact = nom_entry.get()
            liste_nom_contact.append(nom_contact)
            dict_numero["nom_contact"] = liste_nom_contact

            numero_contact = numero_entry.get()
            liste_numero_contact.append(numero_contact)
            dict_numero["numero_contact"] = liste_numero_contact

            window_name.destroy()

        window_name = tk.Toplevel(window)
        window_name.title("Création d'un nouveau contact")

        nom_label = tk.Label(window_name, text="Veuillez entrer le nom du nouveau contact : ")
        nom_label.grid(row=1, column=1)
        nom_entry = tk.Entry(window_name)
        nom_entry.grid(row=1, column=2)

        numero_label = tk.Label(window_name, text="Veuillez entrer son numéro : ")
        numero_label.grid(row=2, column=1)
        numero_entry = tk.Entry(window_name)
        numero_entry.grid(row=2, column=2)

        enter = tk.Button(window_name, text="Enregistrer", command=callback)
        enter.grid(row=3, column=1)

    def display_contact():
        def fermer_et_enregistrer():
            window_contact.destroy()
            enregistrer()

        def supprimer(contact_a_supprimer):
            del dict_numero["nom_contact"][contact_a_supprimer]
            del dict_numero["numero_contact"][contact_a_supprimer]

            window_contact.destroy()
            display_contact()

        window_contact = tk.Toplevel()
        window_contact.title("Contacts")

        bouton_enregistrer = tk.Button(window_contact, text="Enregistrer un nouveau contact",
                                       command=fermer_et_enregistrer)
        bouton_enregistrer.grid(row=3, column=1)

        for contact in range(len(dict_numero['numero_contact'])):
            nom_contact = "Nom : " + str(dict_numero["nom_contact"][contact])
            nom_contact_label = tk.Label(window_contact, text=nom_contact)
            nom_contact_label.grid(row=contact, column=1)

            numero_contact = "N° : " + str(dict_numero["numero_contact"][contact])
            numero_contact_label = tk.Label(window_contact, text=numero_contact)
            numero_contact_label.grid(row=contact, column=2)

            appeler_contact_bouton = tk.Button(window_contact, text="Appeler")
            appeler_contact_bouton.grid(row=contact, column=3)

            supprimer_contact_bouton = tk.Button(window_contact, text="Supprimer", command=lambda: supprimer(contact))
            supprimer_contact_bouton.grid(row=contact, column=4)

    window = Fenetre(window)


if __name__ == '__main__':
    interface_gui()
