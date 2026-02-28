import sys
from PySide6.QtWidgets import ( 
    QApplication, QMainWindow, QLabel, QPushButton, QComboBox,
    QRadioButton, QTextEdit, QSlider, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QHBoxLayout, QWidget, QDateEdit
)
from PySide6.QtCore import Qt


class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Theme Demo")
        self.resize(800, 900)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # ==========================================================
        # TOP THEME BUTTONS
        # ==========================================================
        theme_bar = QHBoxLayout()

        self.btn_dark = QPushButton("Dark")
        self.btn_neon = QPushButton("Cyberpunk")
        self.btn_macos = QPushButton("macOS")
        self.btn_material = QPushButton("Material")

        theme_bar.addWidget(self.btn_dark)
        theme_bar.addWidget(self.btn_neon)
        theme_bar.addWidget(self.btn_macos)
        theme_bar.addWidget(self.btn_material)

        main_layout.addLayout(theme_bar)

        # Connect theme buttons
        self.btn_dark.clicked.connect(lambda: self.apply_theme("Dark"))
        self.btn_neon.clicked.connect(lambda: self.apply_theme("Neon"))
        self.btn_macos.clicked.connect(lambda: self.apply_theme("macOS"))
        self.btn_material.clicked.connect(lambda: self.apply_theme("Material"))

        # ==========================================================

        def add_row(layout, widget, label):
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(label))
            hbox.addWidget(widget)
            layout.addLayout(hbox)

        # LABEL
        self.label = QLabel("Hello PySide6!")
        add_row(main_layout, self.label, "QLabel:")

        # BUTTON
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_button_clicked)
        add_row(main_layout, self.button, "QPushButton:")

        # COMBOBOX
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Option 1", "Option 2", "Option 3"])
        add_row(main_layout, self.combo_box, "QComboBox:")

        # DATE PICKER
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        add_row(main_layout, self.date_edit, "QDateEdit:")

        # RADIO BUTTON
        self.radio_button = QRadioButton("Select me")
        add_row(main_layout, self.radio_button, "QRadioButton:")

        # TEXT EDIT
        self.text_edit = QTextEdit()
        add_row(main_layout, self.text_edit, "QTextEdit:")

        # SLIDER
        self.slider = QSlider(Qt.Horizontal)
        add_row(main_layout, self.slider, "QSlider:")

        # SPINBOX
        self.spin_box = QSpinBox()
        add_row(main_layout, self.spin_box, "QSpinBox:")

        # TABLE
        self.table_widget = QTableWidget(5, 3)
        for i in range(5):
            for j in range(3):
                self.table_widget.setItem(i, j, QTableWidgetItem(f"Cell {i+1},{j+1}"))
        add_row(main_layout, self.table_widget, "QTableWidget:")

        # Apply default theme
        self.apply_theme("Dark")

    # BUTTON ACTION
    def on_button_clicked(self):
        self.label.setText("Button Clicked!")

    # ==========================================================
    # THEME SWITCHER
    # ==========================================================
    def apply_theme(self, theme_name):

        if theme_name == "Dark":
            self.setStyleSheet(self.theme_dark())

        elif theme_name == "Neon":
            self.setStyleSheet(self.theme_cyberpunk())

        elif theme_name == "macOS":
            self.setStyleSheet(self.theme_macos())

        elif theme_name == "Material":
            self.setStyleSheet(self.theme_material())

    # ==========================================================
    # THEMES
    # ==========================================================

    def theme_dark(self):
        return """
            QWidget { background-color: #1e1e1e; color: white; }
            QComboBox, QTextEdit, QSpinBox, QDateEdit, QTableWidget {
                background: #2a2a2a; color: white; border: 1px solid #555;
            }
            QPushButton {
                background: #333; color: white; padding: 6px; border-radius: 6px;
            }
            QPushButton:hover { background: #444; }

            QRadioButton::indicator {
                width: 16px; height: 16px; border-radius: 8px;
                border: 2px solid #888; background: #222;
            }
            QRadioButton::indicator:checked { background: #00ccff; }
        """

    def theme_cyberpunk(self):
        return """
            QWidget { background-color: #0a0014; color: #00ffff; }

            QPushButton {
                background: #ff00cc; color: black; font-weight: bold;
                padding: 6px; border-radius: 6px;
            }
            QPushButton:hover { background: #ff33dd; }

            QComboBox, QTextEdit, QSpinBox, QDateEdit, QTableWidget {
                background: #1a0033; color: cyan; border: 1px solid magenta;
            }

            QRadioButton::indicator {
                width: 16px; height: 16px; border-radius: 8px;
                border: 2px solid magenta; background: #0a0014;
            }
            QRadioButton::indicator:checked { background: #00ffff; }
        """

    def theme_macos(self):
        return """
            QWidget { background-color: #f0f0f0; color: black; }

            QPushButton {
                background: #e0e0e0; color: black;
                padding: 6px; border-radius: 8px;
            }
            QPushButton:hover { background: #d0d0d0; }

            QComboBox, QTextEdit, QSpinBox, QDateEdit, QTableWidget {
                background: white; border: 1px solid #ccc; color: black;
            }

            QRadioButton::indicator {
                width: 16px; height: 16px; border-radius: 8px;
                border: 1px solid #777; background: white;
            }
            QRadioButton::indicator:checked { background: #007aff; }
        """

    def theme_material(self):
        return """
            QWidget { background-color: #263238; color: #eceff1; }

            QPushButton {
                background: #00acc1; color: white; font-weight: bold;
                padding: 6px; border-radius: 6px;
            }
            QPushButton:hover { background: #26c6da; }

            QComboBox, QTextEdit, QSpinBox, QDateEdit, QTableWidget {
                background: #37474f; color: white; border: 1px solid #00acc1;
            }

            QRadioButton::indicator {
                width: 16px; height: 16px; border-radius: 8px;
                border: 2px solid #00acc1; background: #263238;
            }
            QRadioButton::indicator:checked { background: #26c6da; }
        """


app = QApplication(sys.argv)
window = DemoWindow()
window.show()
sys.exit(app.exec())

