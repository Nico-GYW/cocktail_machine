from PySide6.QtWidgets import QWidget, QStackedWidget

class LandingPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        stacked_widget = self.parent()
        while stacked_widget is not None and not isinstance(stacked_widget, QStackedWidget):
            stacked_widget = stacked_widget.parent()
        if stacked_widget is not None:
            stacked_widget.setCurrentIndex(1)

