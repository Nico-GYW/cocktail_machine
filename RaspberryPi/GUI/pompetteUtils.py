def clear_grid_layout(grid_layout):
    """Efface tous les widgets d'un QGridLayout."""
    while grid_layout.count():
        item = grid_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
