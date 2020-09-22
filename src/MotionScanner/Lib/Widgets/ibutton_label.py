from PySide2.QtWidgets import *

class IButtonLabel(QPushButton):
    def __init__(self, entity, parent=None):
        super(IButtonLabel, self).__init__(parent)

        self._entity_id = entity.getId()
        self._entity_name = entity.Name

        self._setupUI()

    @property
    def Id(self):
        return self._entity_id

    def _setupUI(self):
        self._layout = QHBoxLayout(self)

        self._entity_label = QLabel(self._entity_name)
        self._close_label = QLabel('x')

        self._layout.addStretch()
        self._layout.addWidget(self._entity_label)
        self._layout.addStretch()
        self._layout.addWidget(self._close_label)


if __name__ == '__main__':
    import sys
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create babel
    controller = IButtonLabel()
    controller.show()
    # Run the main Qt loop
    sys.exit(app.exec_())