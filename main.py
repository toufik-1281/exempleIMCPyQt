import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
 
class IMCApp(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle('Calculateur \'IMC')
 
        # Layout principal en grille
        layout = QGridLayout()
 
        # Label et champ de saisie pour le poids
        self.poids_label = QLabel('Entrez votre poids (en kg):')
        self.poids_input = QLineEdit()
        layout.addWidget(self.poids_label, 0, 0)  # Ajouter le label à la première ligne, première colonne
        layout.addWidget(self.poids_input, 0, 1)  # Ajouter le champ de saisie à la première ligne, deuxième colonne
 
        # Label et champ de saisie pour la taille
        self.taille_label = QLabel('Entrez votre taille (en metre):')
        self.taille_input = QLineEdit()
        layout.addWidget(self.taille_label, 1, 0)  # Deuxième ligne, première colonne
        layout.addWidget(self.taille_input, 1, 1)  # Deuxième ligne, deuxième colonne
 
        # Bouton pour calculer l'IMC
        self.calc_button = QPushButton('Calculer IMC')
        self.calc_button.clicked.connect(self.calculer_imc)
        layout.addWidget(self.calc_button, 2, 0, 1, 2)  # Troisième ligne, occupe les deux colonnes
 
        # Label pour afficher le résultat de l'IMC
        self.result_label = QLabel('')
        layout.addWidget(self.result_label, 3, 0, 1, 2)  # Quatrième ligne, occupe les deux colonnes
 
        # Définir le layout pour la fenêtre
        self.setLayout(layout)
 
    def calculer_imc(self):
        try:
            poids = float(self.poids_input.text())
            taille = float(self.taille_input.text())
            if taille = 0:
                raise ValueError("La taille doit être positive.")
            imc = poids / (taille ** 2)
            self.afficher_resultat(imc)
        except ValueError:
            self.result_label.setText('Veuillez entrer des valeurs valides pour le poids et la taille.')
 
    def afficher_resultat(self, imc):
        self.result_label.setText(f'Votre IMC est de {imc:.2f}')
 
# Création de l'application
app = QApplication(sys.argv)
 
# Création de la fenêtre principale
fenetre = IMCApp()
fenetre.show()
 
# Exécution de l'application
sys.exit(app.exec())
