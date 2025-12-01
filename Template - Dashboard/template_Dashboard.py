import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QStackedWidget, QFrame,
    QGridLayout, QLineEdit, QProgressBar, QDial, QTabWidget, QTableWidget,
    QTableWidgetItem, QCalendarWidget, QGroupBox, QScrollArea, QFormLayout, QCheckBox, QComboBox
)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve

class DashboardCard(QFrame):
    def __init__(self, title, value, trend=None):
        super().__init__()
        self.setObjectName("card")
        layout = QVBoxLayout(self)
        title_lbl = QLabel(title)
        title_lbl.setObjectName("cardTitle")
        value_lbl = QLabel(value)
        value_lbl.setObjectName("cardValue")
        layout.addWidget(title_lbl)
        layout.addWidget(value_lbl)
        if trend:
            trend_lbl = QLabel(trend)
            trend_lbl.setObjectName("cardTrend")
            layout.addWidget(trend_lbl)
        layout.addStretch()

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search...")
        layout.addWidget(search_bar)
        cards_layout = QGridLayout()
        cards_layout.addWidget(DashboardCard("Users", "1,245", "+5%"), 0, 0)
        cards_layout.addWidget(DashboardCard("Revenue", "$8,320", "+12%"), 0, 1)
        cards_layout.addWidget(DashboardCard("Errors", "12", "-3%"), 1, 0)
        cards_layout.addWidget(DashboardCard("Alerts", "3", "+1"), 1, 1)
        layout.addLayout(cards_layout)
        chart_tabs = QTabWidget()
        chart_tabs.addTab(QLabel("[Line Chart Placeholder]"), "Line Chart")
        chart_tabs.addTab(QLabel("[Bar Chart Placeholder]"), "Bar Chart")
        chart_tabs.addTab(QLabel("[Pie Chart Placeholder]"), "Pie Chart")
        layout.addWidget(chart_tabs)
        bottom_layout = QHBoxLayout()
        progress = QProgressBar()
        progress.setValue(70)
        progress.setFormat("Server Load: %p%")
        dial = QDial()
        dial.setValue(45)
        bottom_layout.addWidget(progress)
        bottom_layout.addWidget(dial)
        layout.addLayout(bottom_layout)
        table = QTableWidget(5, 3)
        for i in range(5):
            for j in range(3):
                table.setItem(i, j, QTableWidgetItem(f"Cell {i+1},{j+1}"))
        layout.addWidget(table)
        calendar = QCalendarWidget()
        layout.addWidget(calendar)

class ReportsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        tab_widget = QTabWidget()
        tab_widget.addTab(QLabel("[Monthly Report Placeholder]"), "Monthly")
        tab_widget.addTab(QLabel("[Quarterly Report Placeholder]"), "Quarterly")
        tab_widget.addTab(QLabel("[Annual Report Placeholder]"), "Annual")
        layout.addWidget(tab_widget)
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search Reports...")
        layout.addWidget(search_bar)
        table = QTableWidget(10, 5)
        for i in range(10):
            for j in range(5):
                table.setItem(i, j, QTableWidgetItem(f"Item {i+1},{j+1}"))
        layout.addWidget(table)

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        account_group = QGroupBox("Account Settings")
        account_form = QFormLayout(account_group)
        self.username_edit = QLineEdit("JohnDoe")
        self.email_edit = QLineEdit("john.doe@example.com")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        change_pw_btn = QPushButton("Change Password")
        account_form.addRow("Username:", self.username_edit)
        account_form.addRow("Email:", self.email_edit)
        account_form.addRow("New Password:", self.password_edit)
        account_form.addRow("", change_pw_btn)
        layout.addWidget(account_group)
        app_group = QGroupBox("Application Settings")
        app_form = QFormLayout(app_group)
        self.notif_check = QCheckBox("Enable Notifications")
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Light", "Dark", "System Default"])
        export_btn = QPushButton("Export Data")
        import_btn = QPushButton("Import Data")
        app_form.addRow(self.notif_check)
        app_form.addRow("Theme:", self.theme_combo)
        app_form.addRow(export_btn, import_btn)
        layout.addWidget(app_group)
        prefs_group = QGroupBox("Preferences")
        prefs_layout = QVBoxLayout(prefs_group)
        self.autosave_check = QCheckBox("Enable Autosave")
        self.notifications_check = QCheckBox("Desktop Notifications")
        prefs_layout.addWidget(self.autosave_check)
        prefs_layout.addWidget(self.notifications_check)
        layout.addWidget(prefs_group)
        layout.addStretch()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analytics Dashboard Template")
        self.resize(1300, 800)
        container = QWidget()
        main_layout = QHBoxLayout(container)
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(220)
        sidebar_layout = QVBoxLayout(self.sidebar)
        self.toggle_btn = QPushButton("⮜ Collapse")
        self.toggle_btn.clicked.connect(self.toggle_sidebar)
        self.nav_list = QListWidget()
        self.nav_list.addItems(["Dashboard", "Reports", "Settings"])
        self.nav_list.currentRowChanged.connect(self.switch_page)
        sidebar_layout.addWidget(self.toggle_btn)
        sidebar_layout.addWidget(self.nav_list)
        sidebar_layout.addStretch()
        self.pages = QStackedWidget()
        self.pages.addWidget(DashboardPage())
        self.pages.addWidget(ReportsPage())
        self.pages.addWidget(SettingsPage())
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.pages, 1)
        self.setCentralWidget(container)
        self.anim = QPropertyAnimation(self.sidebar, b"maximumWidth")
        self.anim.setDuration(250)
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.is_collapsed = False
        self.apply_theme()

    def switch_page(self, index):
        self.pages.setCurrentIndex(index)

    def toggle_sidebar(self):
        if not self.is_collapsed:
            self.anim.setStartValue(self.sidebar.width())
            self.anim.setEndValue(60)
            self.anim.start()
            self.toggle_btn.setText("⮞ Expand")
            self.nav_list.hide()
            self.is_collapsed = True
        else:
            self.anim.setStartValue(self.sidebar.width())
            self.anim.setEndValue(220)
            self.anim.start()
            self.toggle_btn.setText("⮜ Collapse")
            self.nav_list.show()
            self.is_collapsed = False

    def apply_theme(self):
        self.setStyleSheet("""
            QWidget { background-color: #1e1e2f; font-family: 'Segoe UI'; color: #e0e0e0; }
            #sidebar { background-color: #2a2a40; border-right: 1px solid #3a3a55; }
            QListWidget { background-color: transparent; border: none; color: #e0e0e0; font-size: 14px; }
            QListWidget::item:selected { background-color: #4b7bec; color: white; border-radius: 4px; }
            QPushButton { background-color: #4b7bec; color: white; border: none; padding: 6px; border-radius: 6px; font-weight: 500; }
            QPushButton:hover { background-color: #3a65c0; }
            #card { background-color: #2c2c50; border-radius: 10px; padding: 14px; }
            #cardTitle { font-size: 14px; color: #c0c0c0; }
            #cardValue { font-size: 28px; font-weight: bold; color: #ffffff; }
            #cardTrend { font-size: 12px; color: #7bed9f; }
            #chartPlaceholder { background-color: #2c2c50; border-radius: 10px; border: 1px solid #3a3a55; color: #ffffff; }
            QLineEdit { padding: 6px; border: 1px solid #555; border-radius: 6px; background-color: #2c2c50; color: #e0e0e0; }
            QCheckBox { padding: 4px; }
            QComboBox { padding: 4px; background-color: #2c2c50; color: #e0e0e0; border: 1px solid #555; border-radius: 4px; }
            QGroupBox { border: 1px solid #3a3a55; border-radius: 6px; margin-top: 6px; padding: 10px; }
            QTabWidget::pane { border: 1px solid #3a3a55; border-radius: 6px; }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())