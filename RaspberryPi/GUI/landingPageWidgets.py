from PySide6.QtWidgets import QWidget

class LandingPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        stacked_widget = self.parent()
        stacked_widget.setCurrentIndex(1)
