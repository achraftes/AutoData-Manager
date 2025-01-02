import tkinter as tk
from tkinter import messagebox, filedialog

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

    def __str__(self):
        return (f"Marque: {self.marque}\n"
                f"Modèle: {self.modele}\n"
                f"Année: {self.annee}\n"
                f"Prix HT: {self.prix_ht:.2f} €\n"
                f"Remise: {self.remise} %\n"
                f"Couleur: {self.couleur}\n"
                f"Carburant: {self.carburant}\n"
                f"Prix TTC: {self.prix_ttc():.2f} €\n"
                "-----------------------------")

def ajouter_voiture():
    v = Voiture()
    v.saisir()
    voitures.append(v)
    messagebox.showinfo("Voiture ajoutée", "Voiture ajoutée avec succès")
    afficher_voitures()

def afficher_voitures():
    text_area.delete(1.0, tk.END)
    if voitures:
        for v in voitures:
            text_area.insert(tk.END, str(v) + "\n")
    else:
        text_area.insert(tk.END, "Aucune voiture dans la liste")

def supprimer_voiture():
    nom = modele_entry.get()
    for v in voitures:
        if v.modele == nom:
            voitures.remove(v)
            messagebox.showinfo("Voiture supprimée", "Voiture supprimée avec succès")
            afficher_voitures()
            return
    messagebox.showinfo("Voiture non trouvée", "Voiture non trouvée")

def modifier_voiture():
    nom = modele_entry.get()
    for v in voitures:
        if v.modele == nom:
            v.saisir()
            messagebox.showinfo("Voiture modifiée", "Voiture modifiée avec succès")
            afficher_voitures()
            return
    messagebox.showinfo("Voiture non trouvée", "Voiture non trouvée")

def rechercher_voitures():
    carburant = carburant_entry.get()
    result = [v for v in voitures if v.carburant == carburant]
    text_area.delete(1.0, tk.END)
    if result:
        for v in result:
            text_area.insert(tk.END, str(v) + "\n")
    else:
        text_area.insert(tk.END, "Aucune voiture correspondante")

def calculer_moyenne():
    total = sum(v.prix_ttc() for v in voitures)
    nb_voitures = len(voitures)
    if nb_voitures > 0:
        moyenne = total / nb_voitures
        messagebox.showinfo("Moyenne des prix TTC", f"Moyenne des prix TTC après remise : {moyenne:.2f} €")
    else:
        messagebox.showinfo("Aucune voiture", "Aucune voiture dans la liste")

def sauvegarder_voitures():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, "w") as f:
            for v in voitures:
                f.write(str(v) + "\n")
        messagebox.showinfo("Enregistrement", "Vos données sont enregistrées.")

def quitter():
    root.destroy()

voitures = []

root = tk.Tk()
root.title("Gestion des Voitures")
root.geometry('400x500')

# Centrer la fenêtre
window_width = 400
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Création des champs de saisie
fields = ["Marque", "Modèle", "Année", "Prix HT", "Remise (%)", "Couleur", "Carburant"]
entries = []
for i, field in enumerate(fields):
    label = tk.Label(root, text=field + ":")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
    entries.append(entry)

marque_entry, modele_entry, annee_entry, prix_ht_entry, remise_entry, couleur_entry, carburant_entry = entries

# Zone de texte pour afficher les voitures
text_area = tk.Text(root, height=10, width=50)
text_area.grid(row=len(fields), column=0, columnspan=2, padx=10, pady=10)

# Boutons
buttons = [
    ("Ajouter", ajouter_voiture),
    ("Afficher", afficher_voitures),
    ("Supprimer", supprimer_voiture),
    ("Modifier", modifier_voiture),
    ("Rechercher", rechercher_voitures),
    ("Calculer", calculer_moyenne),
    ("Enregistrer", sauvegarder_voitures),
    ("Quitter", quitter)
]

for i, (text, command) in enumerate(buttons):
    button = tk.Button(root, text=text, command=command)
    button.grid(row=len(fields) + 1 + i // 2, column=i % 2, padx=10, pady=5)

root.mainloop()