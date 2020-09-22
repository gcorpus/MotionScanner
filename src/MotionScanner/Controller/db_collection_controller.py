from PySide2.QtWidgets import *
from MotionScanner.Lib.Widgets import ILineEdit, ICombobox, ITextEdit, ISpinbox, IDateEdit, ITableView, ITableModel
from MotionScanner.Lib.Catalogs import LevelsCatalog, DBCollectionCatalog, GenderCatalog
from MotionScanner.Lib import DBQueryLib
from PySide2.QtCore import *
from PySide2.QtGui import *
import operator


class DBCollectionController(QGroupBox):

    def __init__(self, combobox,  parent=None):
        super(DBCollectionController, self).__init__(parent)

        self._combobox = combobox

        self._setupUI()

    def _setupUI(self):
        self._main_layout = QVBoxLayout(self)

        self._fields_layout = QVBoxLayout()
        self._table_layout = QVBoxLayout()

        if self._combobox.currentText() == DBCollectionCatalog.USER_TAG:

            self._layer_01 = QVBoxLayout()
            self._layer_02 = QHBoxLayout()
            self._layer_03 = QHBoxLayout()
            self._layer_04 = QVBoxLayout()

            self._username_lineedit = ILineEdit(label='Username')
            self._layer_01.addWidget(self._username_lineedit)

            self._birthdate_calendar = IDateEdit(label='Birthdate')
            self._gender_combobox = ICombobox(label='Gender', items=GenderCatalog.Tags)
            self._layer_02.addWidget(self._birthdate_calendar)
            self._layer_02.addWidget(self._gender_combobox)

            self._height_spinbox = ISpinbox(label='Height', measure='mts.')
            self._weight_spinbox = ISpinbox(label='Weight', measure='kg.')
            self._layer_03.addWidget(self._height_spinbox)
            self._layer_03.addWidget(self._weight_spinbox)

            self._roles_widget = QLabel('Roles')
            self._layer_04.addWidget(self._roles_widget)

            self._fields_layout.addLayout(self._layer_01)
            self._fields_layout.addLayout(self._layer_02)
            self._fields_layout.addLayout(self._layer_03)
            self._fields_layout.addLayout(self._layer_04)

        elif self._combobox.currentText() == DBCollectionCatalog.POSE_TAG:

            self._layer_01 = QHBoxLayout()
            self._layer_02 = QHBoxLayout()
            self._layer_03 = QVBoxLayout()

            self._name_lineedit = ILineEdit(label='Name')
            self._layer_01.addWidget(self._name_lineedit)

            self._discipline_combobox = ICombobox(label='Discipline', items=DBQueryLib.GetDisciplineTags())
            self._level_combobox = ICombobox(label='Level', items=LevelsCatalog.Tags)
            self._layer_02.addWidget(self._discipline_combobox)
            self._layer_02.addWidget(self._level_combobox)

            self._steps_textedit = ITextEdit(label='Steps')
            self._images_textedit = ITextEdit(label='Images')
            self._animation_lineedit = ILineEdit(label='Animation')
            self._layer_03.addWidget(self._steps_textedit)
            self._layer_03.addWidget(self._images_textedit)
            self._layer_03.addWidget(self._animation_lineedit)

            self._fields_layout.addLayout(self._layer_01)
            self._fields_layout.addLayout(self._layer_02)
            self._fields_layout.addLayout(self._layer_03)

        elif self._combobox.currentText() == DBCollectionCatalog.MOVEMENT_TAG:

            self._layer_01 = QHBoxLayout()
            self._layer_02 = QHBoxLayout()

            self._name_lineedit = ILineEdit(label='Name')
            self._layer_01.addWidget(self._name_lineedit)

            self._discipline_combobox = ICombobox(label='Discipline', items=DBQueryLib.GetDisciplineTags())
            self._level_combobox = ICombobox(label='Level', items=LevelsCatalog.Tags)
            self._modification_combobox = ICombobox(label='Modification')
            self._poses_combobox = ICombobox(label='Poses')
            self._layer_02.addWidget(self._discipline_combobox)
            self._layer_02.addWidget(self._level_combobox)
            self._layer_02.addWidget(self._modification_combobox)
            self._layer_02.addWidget(self._poses_combobox)

            self._steps_textedit = ITextEdit(label='Steps')
            self._benefits_textedit = ITextEdit(label='Benefits')
            self._tips_textedit = ITextEdit(label='Tips')
            self._images_textedit = ITextEdit(label='Images')
            self._animation_lineedit = ILineEdit(label='Animation')

            self._fields_layout.addLayout(self._layer_01)
            self._fields_layout.addLayout(self._layer_02)
            self._fields_layout.addWidget(self._steps_textedit)
            self._fields_layout.addWidget(self._benefits_textedit)
            self._fields_layout.addWidget(self._tips_textedit)
            self._fields_layout.addWidget(self._images_textedit)
            self._fields_layout.addWidget(self._animation_lineedit)

        elif self._combobox.currentText() == DBCollectionCatalog.SEQUENCE_TAG:

            self._layer_01 = QVBoxLayout()
            self._layer_02 = QHBoxLayout()
            self._layer_03 = QHBoxLayout()
            self._layer_04 = QVBoxLayout()

            self._name_lineedit = ILineEdit(label='Name')
            self._layer_01.addWidget(self._name_lineedit)

            self._discipline_combobox = ICombobox(label='Discipline', items=DBQueryLib.GetDisciplineTags())
            self._level_combobox = ICombobox(label='Level', items=LevelsCatalog.Tags)
            self._layer_02.addWidget(self._discipline_combobox)
            self._layer_02.addWidget(self._level_combobox)

            self._coach_combobox = ICombobox(label='Coach')
            self._layer_03.addWidget(self._coach_combobox)

            self._movements_widget = QLabel('Movement')
            self._layer_04.addWidget(self._movements_widget)

            self._fields_layout.addLayout(self._layer_01)
            self._fields_layout.addLayout(self._layer_02)
            self._fields_layout.addLayout(self._layer_03)
            self._fields_layout.addLayout(self._layer_04)

        elif self._combobox.currentText() == DBCollectionCatalog.DISCIPLINE_TAG:

            self._name_lineedit = ILineEdit(label='Name')
            self._description_textedit = ITextEdit(label='Description')
            self._coaches_widget = QLabel('Coaches')
            self._routines_widget = QLabel('Routines')

            self._fields_layout.addWidget(self._name_lineedit)
            self._fields_layout.addWidget(self._description_textedit)
            self._fields_layout.addWidget(self._coaches_widget)
            self._fields_layout.addWidget(self._routines_widget)

        # self._table_view = ITableView(header=self._header, data=self._data)
        # self._table_layout.addWidget(self._table_view)

        self._button_save = QPushButton('Save')
        self._button_layout = QHBoxLayout()
        self._button_layout.addStretch()
        self._button_layout.addWidget(self._button_save)

        self._main_layout.addLayout(self._fields_layout)
        self._main_layout.addLayout(self._button_layout)


