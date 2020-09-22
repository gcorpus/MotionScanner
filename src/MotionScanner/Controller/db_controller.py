from PySide2.QtWidgets import *
from MotionScanner.Lib.Widgets import ICombobox, ITableView
from MotionScanner.Lib.Catalogs import DBCollectionCatalog
from MotionScanner.Controller import DBCollectionController
from MotionScanner.Lib import DBQueryLib


class DBController(QDialog):

    def __init__(self, parent=None):
        super(DBController, self).__init__(parent)

        self.setStyleSheet("""font-family:Helvetica;color:black;font-size:12px;""")

        self._header = []
        self._data = []
        self._table_view = None

        self._setupUI()
        self._initialize()

    def _setupUI(self):
        self.setWindowTitle("Feed Database")

        self._main_layout = QHBoxLayout(self)
        self._submain_layout = QVBoxLayout()
        self._form_layout = QVBoxLayout()
        self._table_layout = QVBoxLayout()

        self._collection_combobox = ICombobox(label='Collection', items=DBCollectionCatalog.Tags)
        self._controller = QGroupBox()
        self._table_view = ITableView()

        self._form_layout.addWidget(self._controller)

        self._table_layout.addItem(QSpacerItem(700, 1, QSizePolicy.Minimum, QSizePolicy.Minimum))
        self._table_layout.addWidget(self._table_view)

        self._submain_layout.addItem(QSpacerItem(500, 1, QSizePolicy.Minimum, QSizePolicy.Minimum))
        self._submain_layout.addWidget(self._collection_combobox)
        self._submain_layout.addLayout(self._form_layout)
        self._submain_layout.addStretch()

        self._main_layout.addLayout(self._submain_layout)
        self._main_layout.addLayout(self._table_layout)

    def _initialize(self):
        self._collection_combobox.Combobox.currentIndexChanged.connect(self._AddCollectionsController)

    def Show(self):
        self.exec_()

    def _AddCollectionsController(self):

        item = self._form_layout.takeAt(0).widget()
        item.deleteLater()

        self._controller = DBCollectionController(combobox=self._collection_combobox.Combobox)

        self._form_layout.addWidget(self._controller)

        self._header = []
        self._data = []

        if self._collection_combobox.Combobox.currentText() == DBCollectionCatalog.USER_TAG:

            self._header = ['Username', 'Birthdate', 'Gender', 'Height', 'Weight', 'Roles', 'Creation_Date', 'Modification_Date']

            users = DBQueryLib.GetAllUsers()
            for u in users:
                self._data.append((u.Name, str(u.Birthdate), u.Gender, u.Height, u.Weight, str(u.Roles),
                                   str(u.CreationDate), str(u.ModificationDate)))

        elif self._collection_combobox.Combobox.currentText() == DBCollectionCatalog.POSE_TAG:

            self._header = ['Name', 'Discipline', 'Level', 'Steps', 'Images', 'Animation', 'Creation_Date','Modification_Date']

            poses = DBQueryLib.GetAllPoses()
            for p in poses:
                self._data.append((p.Name, str(p.Discipline), p.Level, p.Steps, p.Images, p.Animation,
                                   str(p.CreationDate), str(p.ModificationDate)))

        elif self._collection_combobox.Combobox.currentText() == DBCollectionCatalog.MOVEMENT_TAG:

            self._header = ['Name', 'Discipline', 'Level', 'Modification', 'Poses', 'Steps', 'Benefits', 'Tips', 'Images', 'Animation', 'Creation_Date', 'Modification_Date']

            movements = DBQueryLib.GetAllMovements()
            for m in movements:
                self._data.append((m.Name, m.Discipline, m.Level, str(m.Modification), str(m.Poses), m.Steps, m.Benefit, m.Tips,
                                   m.Images, m.Animation, str(m.CreationDate), str(m.ModificationDate)))

        elif self._collection_combobox.Combobox.currentText() == DBCollectionCatalog.SEQUENCE_TAG:

            self._header = ['Name', 'Discipline', 'Level', 'Coach', 'Movements', 'Creation_Date', 'Modification_Date']

            sequences = DBQueryLib.GetAllSequences()
            for s in sequences:
                self._data.append((s.Name, s.Discipline, s.Level, s.Coach, s.Movements, str(s.CreationDate), str(s.ModificationDate)))

        elif self._collection_combobox.Combobox.currentText() == DBCollectionCatalog.DISCIPLINE_TAG:

            self._header = ['Name', 'Description', 'Coaches', 'Routines', 'Creation_Date', 'Modification_Date']

            disciplines = DBQueryLib.GetAllDisciplines()
            for d in disciplines:
                self._data.append((d.Name, d.Description, d.Coaches, d.Routines, str(d.CreationDate), str(d.ModificationDate)))

        item = self._table_layout.takeAt(1).widget()
        item.deleteLater()

        if self._data:
            self._table_view = ITableView(header=self._header, data=self._data)
            self._table_layout.addWidget(self._table_view)
