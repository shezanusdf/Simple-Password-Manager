# PasswordVault

A minimal password manager CRUD app made w/ Python

## Features
- Add / delete website entries (website -> username + password)
- Simple GUI built with PySide6
- uses json for password storage

## Requirements
- Python 3.8+
- pyside6

## Install & run (dev)
```bash
cd "c:\Users\shazeb\Downloads\Simple Password Manager"
python -m venv venv
venv\Scripts\activate
pip install PySide6
python gui.py
```

## Project Layout
- gui.py - PySide6 GUI (main app)
- storage.py - JSON persistence (records.json path respects frozen exe)
- vault.py - optional CLI helper functions
- main.py - CLI Menu (optional)

## Notes
- main.py is optional, you can remove it if you only use the GUI.

