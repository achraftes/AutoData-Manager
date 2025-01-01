import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from functools import partial


class Voiture:
    def __init__(self, ma="", mo="", ane=0, p=0, r=0, co="", ca=""):
        self.marque = ma
        self.modele = mo
        self.annee = ane
        self.prix_ht = p
        self.remise = r
        self.couleur = co
        self.carburant = ca

    def prix_ttc(self):
        return self.prix_ht * 1.2 * (1 - self.remise / 100)

    def saisir(self):
        self.marque = marque_entry.get()
        self.modele = modele_entry.get()
        self.annee = int(annee_entry.get())
        self.prix_ht = float(prix_ht_entry.get())
        self.remise = float(remise_entry.get())
        self.couleur = couleur_entry.get()
        self.carburant = carburant_entry.get()

    def sauvegarder(self, filename):
        with open(filename, "w") as f:
            for voiture in voitures:
                f.write(f"Marque: {voiture.marque}\n")
                f.write(f"Modèle: {voiture.modele}\n")
                f.write(f"Année: {voiture.annee}\n")
                f.write(f"Prix HT: {voiture.prix_ht}\n")
                f.write(f"Remise: {voiture.remise}\n")
                f.write(f"Couleur: {voiture.couleur}\n")
                f.write(f"Carburant: {voiture.carburant}\n")
                f.write(f"Prix TTC: {voiture.prix_ttc()}\n")
        messagebox.showinfo("Sauvegarde", f"Data saved to {filename} successfully")

    def __str__(self):
        return "marque:" + self.marque + ",modele:" + self.modele + ",annee:" + str(self.annee) + ",couleur:" + self.couleur + ",carburant:" + self.carburant + ",prix_ttc:" + str(self.prix_ttc())


def ajouter_voiture():
    v = Voiture()
    v.saisir()
    voitures.append(v)
    messagebox.showinfo("Voiture ajoutée", "Voiture ajoutée avec succès")


def afficher_voitures():
    if len(voitures) == 0:
        messagebox.showinfo("Aucune voiture", "Aucune voiture dans la liste")
    else:
        messagebox.showinfo("Voitures", "\n".join(str(v) for v in voitures))


def supprimer_voiture():
    nom = modele_entry.get()
    for v in voitures:
        if v.modele == nom:
            voitures.remove(v)
            messagebox.showinfo("Voiture supprimée", "Voiture supprimée avec succès")
            return
    messagebox.showinfo("Voiture non trouvée", "Voiture non trouvée")


def modifier_voiture():
    nom = modele_entry.get()
    for v in voitures:
        if v.modele == nom:
            v.saisir()
            messagebox.showinfo("Voiture modifiée", "Voiture modifiée avec succès")
            return
    messagebox.showinfo("Voiture non trouvée", "Voiture non trouvée")


def rechercher_voitures():
    carburant = carburant_entry.get()
    result = []
    for v in voitures:
        if v.carburant == carburant:
            result.append(str(v))
    if len(result) > 0:
        messagebox.showinfo("Voitures trouvées", "\n".join(result))
    else:
        messagebox.showinfo("Aucune voiture", "Aucune voiture correspondante")


def calculer_moyenne():
    total = 0
    nb_voitures = len(voitures)
    for v in voitures:
        total += v.prix_ttc()
    if nb_voitures > 0:
        moyenne = total / nb_voitures
        messagebox.showinfo("Moyenne des prix TTC", f"Moyenne des prix TTC après remise : {moyenne:.2f} €")
    else:
        messagebox.showinfo("Aucune voiture", "Aucune voiture dans la liste")


       

def sauvegarder_voitures():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filename:
        for v in voitures:
            v.sauvegarder(filename)
        messagebox.showinfo("Enregistrement", "Vos données sont enregistrées.")

def quitter():
    root.destroy()


choix = None
voitures = []

root = tk.Tk()
root.title("Formulaire Voiture")
root.geometry('302x325')


marque_label = tk.Label(root, text="Marque:")
modele_label = tk.Label(root, text="Modèle:")
annee_label = tk.Label(root, text="Année:")
prix_ht_label = tk.Label(root, text="Prix HT:")
remise_label = tk.Label(root, text="Remise (%):")
couleur_label = tk.Label(root, text="Couleur:")
carburant_label = tk.Label(root, text="Carburant:")

marque_label.grid(row=0, column=0)
modele_label.grid(row=1, column=0)
annee_label.grid(row=2, column=0)
prix_ht_label.grid(row=3, column=0)
remise_label.grid(row=4, column=0)
couleur_label.grid(row=5, column=0)
carburant_label.grid(row=6, column=0)

marque_entry = tk.Entry(root,bg="cyan")
modele_entry = tk.Entry(root,bg="cyan")
annee_entry = tk.Entry(root,bg="cyan")
prix_ht_entry = tk.Entry(root,bg="cyan")
remise_entry = tk.Entry(root,bg="cyan")
couleur_entry = tk.Entry(root,bg="cyan")
carburant_entry = tk.Entry(root,bg="cyan")

marque_entry.grid(row=0, column=1)
modele_entry.grid(row=1, column=1)
annee_entry.grid(row=2, column=1)
prix_ht_entry.grid(row=3, column=1)
remise_entry.grid(row=4, column=1)
couleur_entry.grid(row=5, column=1)
carburant_entry.grid(row=6, column=1)


ajouter_button = tk.Button(root, text="Ajouter", command=ajouter_voiture)
afficher_button = tk.Button(root, text="Afficher", command=afficher_voitures)
supprimer_button = tk.Button(root, text="Supprimer", command=supprimer_voiture)
modifier_button = tk.Button(root, text="Modifier", command=modifier_voiture)
rechercher_button = tk.Button(root, text="Rechercher", command=rechercher_voitures)
calculer_button = tk.Button(root, text="Calculer", command=calculer_moyenne)
enregistrer_button = tk.Button(root, text="Enregistrer", command=sauvegarder_voitures)
quitter_button = tk.Button(root, text="Quitter", command=quitter)

ajouter_button.grid(row=7, column=0)
afficher_button.grid(row=7, column=1)
supprimer_button.grid(row=8,column=0)
modifier_button.grid(row=8, column=1)
rechercher_button.grid(row=9, column=0)
calculer_button.grid(row=9, column=1)
enregistrer_button.grid(row=10, column=1)
quitter_button.grid(row=10, column=0, )

root.mainloop()
