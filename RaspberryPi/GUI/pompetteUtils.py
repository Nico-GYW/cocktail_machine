from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

def clear_grid_layout(grid_layout):
    """Efface tous les widgets d'un QGridLayout."""
    while grid_layout.count():
        item = grid_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()

class PompetteMessageBox(QMessageBox):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        
        # Définir le titre de la boîte de message
        self.setWindowTitle("Erreur")
        
        # Définir le texte (message) de la boîte de message
        self.setText(message)
        
        # Charger et définir l'icône personnalisée
        customIcon = QPixmap("ressources/generic/pompette_noir.png")
        self.setIconPixmap(customIcon.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))