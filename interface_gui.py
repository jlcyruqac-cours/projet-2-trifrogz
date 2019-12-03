import tkinter as tk
from tkinter import messagebox
import pjsua as pj


LOG_LEVEL=3
current_call = None


def log_cb(level, str, len):
    print(str)


class MyCallCallback(pj.CallCallback):

    def __init__(self, call=None):
        pj.CallCallback.__init__(self, call)

    # Notification when call state has changed
    def on_state(self):
        global current_call
        print("Call with", self.call.info().remote_uri)
        print("is", self.call.info().state_text)
        print("last code =", self.call.info().last_code)
        print("(" + self.call.info().last_reason + ")")

        if self.call.info().state == pj.CallState.DISCONNECTED:
            current_call = None
            print('Current call is', current_call)

    # Notification when call's media state has changed.
    def on_media_state(self):
        if self.call.info().media_state == pj.MediaState.ACTIVE:
            # Connect the call to sound device
            call_slot = self.call.info().conf_slot
            pj.Lib.instance().conf_connect(call_slot, 0)
            pj.Lib.instance().conf_connect(0, call_slot)
            print("Media is now active")
        else:
            print("Media is inactive")


def interface_gui():
    window = tk.Tk()
    window.title("Software softphone")

    class LoginDialog(tk.Toplevel):
        def __init__(self, parent):
            super().__init__(parent)
            self.title("Fenêtre Modale")
            self.resizable(False, False)
            # ---------------------------------------
            tk.Label(self, text="Login : ", font="Arial, 12").pack()
            self.entry_login = tk.Entry(self, font="Arial, 12")
            self.entry_login.insert(0, "defaultlogin")
            self.entry_login.pack()
            # ---------------------------------------
            tk.Label(self, text="Clé : ", font="Arial, 12").pack()
            self.entry_pass = tk.Entry(self, show='*', font="Arial, 12")
            self.entry_pass.insert(0, "defaultpass")
            self.entry_pass.pack()
            # ---------------------------------------
            tk.Button(self, text="Connexion", command=self.connect, font="Arial, 12", background="#F79F1F",
                      activebackground="#12CBC4").pack()

        def connect(self):
            # TODO: obliger la connexion à l'ouverture du logiciel
            connected = False
            key_list = []
            login_list = []
            with open("../login.txt", "r") as f:
                fichier_entier = f.read()
                line = fichier_entier.split("\n")
                for identifiants in line:
                    splited_id = identifiants.split(',')
                    key_file = splited_id[1].replace('\\n', '')
                    login_file = splited_id[0]
                    key_list.append(key_file)
                    login_list.append(login_file)
                while not connected:
                    login = self.entry_login.get().strip()
                    key = self.entry_pass.get().strip()
                    try:
                        key_list.index(key)
                        login_list.index(login)
                    except ValueError:
                        messagebox.showerror("Erreur connexion", "Veuillez rentrer des identifiants valides")
                        break
                    connected = True
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
            window.resizable(False, False)
            self.master.title("Fenêtre principale")
            self.grid(row=1, column=1)
            bouton_new = tk.Button(self, width=10, height=1, text="Connexion", command=connect, font="Arial, 12",
                                   background="#F79F1F", activebackground="#12CBC4")
            bouton_new.grid(row=5, column=5)

            def do_update(caractere):
                add_char(caractere)

            # Affichage des chiffres
            caractere_liste = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#"]
            row = 2
            column = 0
            compteur_row = 0
            for caractere in caractere_liste:
                compteur_row += 1
                if compteur_row == 4:
                    row += 1
                    compteur_row = 1
                if column == 3:
                    column = 1
                else:
                    column += 1
                nom_bouton = tk.Button(window, text=caractere, padx=20,
                                       command=lambda caractere=caractere: do_update(caractere),
                                       background="#1289A7", activebackground="#12CBC4", font="Arial, 12")
                nom_bouton.grid(row=row, column=column)

            supp_char = tk.Button(window, text="<-", padx=20, command=delete_char,
                                  background="#1289A7", activebackground="#12CBC4", font="Arial, 12")
            supp_char.grid(row=6, column=1)

            # Bouton pour appeler
            appeler = tk.Button(window, text="Appeler", padx=50,
                                background="#F79F1F", activebackground="#FFC312", font="Arial, 12")
            appeler.grid(row=6, column=2)

            # Actions
            voir_contact = tk.Button(window, text="Voir les contacts", command=display_contact,
                                     background="#B53471", activebackground="#ED4C67", font="Arial, 12")
            voir_contact.grid(row=2, column=4)

            boite_vocale = tk.Button(window, text="Ecouter messages",
                                     background="#B53471", activebackground="#ED4C67", font="Arial, 12")
            boite_vocale.grid(row=3, column=4)

            historique = tk.Button(window, text="Voir historique appels",
                                   background="#B53471", activebackground="#ED4C67", font="Arial, 12")
            historique.grid(row=4, column=4)
            # ------------------------------
            window.mainloop()

    liste_affichage_numero = []
    liste_nom_contact = []
    liste_numero_contact = []
    dict_numero = {"numero_contact": liste_numero_contact, "nom_contact": liste_nom_contact}

    # Affichage de l'écriture de chiffre
    affichage_numero_pad = tk.Label(window, relief="ridge", padx=70, font="Arial, 12")
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
            numero_contact = numero_entry.get()
            with open("../contacts.txt", "a") as f:
                f.write(nom_contact + "," + numero_contact + "\n")
                f.close()

            window_name.destroy()

        window_name = tk.Toplevel(window)
        window_name.resizable(False, False)
        window_name.title("Création d'un nouveau contact")

        nom_label = tk.Label(window_name, text="Veuillez entrer le nom du nouveau contact : ", font="Arial, 12")
        nom_label.grid(row=1, column=1)
        nom_entry = tk.Entry(window_name, font="Arial, 12")
        nom_entry.grid(row=1, column=2)

        numero_label = tk.Label(window_name, text="Veuillez entrer son numéro : ", font="Arial, 12")
        numero_label.grid(row=2, column=1)
        numero_entry = tk.Entry(window_name, font="Arial, 12")
        numero_entry.grid(row=2, column=2)

        enter = tk.Button(window_name, text="Enregistrer", command=callback)
        enter.grid(row=3, column=1)

    def display_contact():
        def fermer_et_enregistrer():
            window_contact.destroy()
            enregistrer()

        def supprimer(contact_a_supprimer):
            with open("../contacts.txt", "r") as f_read:
                lines = f_read.readlines()
                f_read.close()
            with open("../contacts.txt", "w") as f_write:
                print(lines)
                lines[contact_a_supprimer] = ""
                f_write.close()
                # TODO: fix it (suppression du mauvais élément)
            # del dict_numero["nom_contact"][contact_a_supprimer]
            # del dict_numero["numero_contact"][contact_a_supprimer]

            window_contact.destroy()
            display_contact()

        window_contact = tk.Toplevel()
        window_contact.resizable(False, False)
        window_contact.title("Contacts")

        bouton_enregistrer = tk.Button(window_contact, text="Enregistrer un nouveau contact",
                                       command=fermer_et_enregistrer, background="#F79F1F",
                                       activebackground="#FFC312", font="Arial, 12")
        bouton_enregistrer.grid(row=3, column=1)

        with open("../contacts.txt", "r") as f:
            lines = f.readlines()
            liste_nom_contact = []
            liste_numero_contact = []

            for line in lines:
                splited_line = line.split(",")
                nom_contact, numero_contact = splited_line[0], splited_line[1]

                liste_nom_contact.append(nom_contact)
                dict_numero["nom_contact"] = liste_nom_contact

                liste_numero_contact.append(numero_contact)
                dict_numero["numero_contact"] = liste_numero_contact

        for contact in range(len(dict_numero['numero_contact'])):
            nom_contact = "Nom : " + str(dict_numero["nom_contact"][contact])
            nom_contact_label = tk.Label(window_contact, text=nom_contact, font="Arial, 12")
            nom_contact_label.grid(row=contact, column=1)

            numero_contact = "N° : " + str(dict_numero["numero_contact"][contact])
            numero_contact_label = tk.Label(window_contact, text=numero_contact, font="Arial, 12")
            numero_contact_label.grid(row=contact, column=2)

            appeler_contact_bouton = tk.Button(window_contact, text="Appeler", background="#F79F1F",
                                               activebackground="#FFC312", font="Arial, 12")
            appeler_contact_bouton.grid(row=contact, column=3)

            supprimer_contact_bouton = tk.Button(window_contact, text="Supprimer", command=lambda: supprimer(contact),
                                                 background="#F79F1F", activebackground="#FFC312", font="Arial, 12")
            supprimer_contact_bouton.grid(row=contact, column=4)

    window = Fenetre(window)

if __name__ == '__main__':
    interface_gui()