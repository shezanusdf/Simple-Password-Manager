import sys
from PySide6.QtWidgets import (
    QApplication, 
    QWidget,
    QListWidget,
    QPushButton,
    QLineEdit,
    QFormLayout,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)
from storage import load_records, dump_records

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Vault")
        self.resize(700,420)

        self.passwords = load_records()

        self.site_input = QLineEdit()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.list_widget = QListWidget()
        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")
        self.show_button = QPushButton("Show")

        form_layout = QFormLayout()
        form_layout.addRow("Website: ", self.site_input)
        form_layout.addRow("Username: ", self.username_input)

        password_row = QHBoxLayout()
        password_row.addWidget(self.password_input)
        password_row.addWidget(self.show_button)
        form_layout.addRow("Password: ", password_row)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)

        right_layout = QVBoxLayout()
        right_layout.addLayout(form_layout)
        right_layout.addLayout(button_layout)
        right_layout.addStretch()

        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.list_widget, 2)
        main_layout.addLayout(right_layout, 2)

        self.add_button.clicked.connect(self.add_entry)
        self.delete_button.clicked.connect(self.delete_entry)
        self.show_button.clicked.connect(self.toggle_password_visibility)
        self.list_widget.itemSelectionChanged.connect(self.load_selected_entry)

        self.refresh_list()
    def refresh_list(self):
        self.list_widget.clear()
        for website in sorted(self.passwords):
            self.list_widget.addItem(website)

    def load_selected_entry(self):
        item = self.list_widget.currentItem()
        if not item:
            return
        website = item.text()
        record = self.passwords.get(website, {})
        self.site_input.setText(website)
        self.username_input.setText(record.get("username", ""))
        self.password_input.setText(record.get("password", ""))

    def add_entry(self):
        website = self.site_input.text().strip()
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        if not website or not username or not password:
            QMessageBox.warning(self, "Missing Data", "Enter Website, username and password.")
            return

        if website in self.passwords:
            QMessageBox.warning(self, "Duplicate", "That website already exists!")
            return
        self.passwords[website] = {"username": username, "password": password}
        dump_records(self.passwords)
        self.refresh_list()
        self.clear_inputs()

    def delete_entry(self):
        item = self.list_widget.currentItem()
        if not item:
            QMessageBox.warning(self, "No Selection", "Select a website to delte.")
            return
        website = item.text()
        self.passwords.pop(website, None)
        dump_records(self.passwords)
        self.refresh_list()
        self.clear_inputs()

    def toggle_password_visibility(self):
        if self.password_input.echoMode() == QLineEdit.Password:
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.show_button.setText("Hide")
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.show_button.setText("Show")

    def clear_inputs(self):
        self.site_input.clear()
        self.username_input.clear()
        self.password_input.clear()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
