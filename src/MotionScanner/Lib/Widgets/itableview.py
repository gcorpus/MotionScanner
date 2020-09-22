from PySide2.QtWidgets import *
from MotionScanner.Lib.Widgets import ITableModel


class ITableView(QWidget):
    def __init__(self, parent=None, header=[], data=[]):
        super(ITableView, self).__init__(parent)

        self._header = header
        self._data = data

        self._setupUI()

    def _setupUI(self):

        self._main_layout = QVBoxLayout(self)

        self._table_model = ITableModel(self, self._header, self._data)
        self._table_view = QTableView()
        self._table_view.setModel(self._table_model)

        self._main_layout.addWidget(self._table_view)
