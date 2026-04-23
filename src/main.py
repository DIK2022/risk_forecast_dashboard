import sys
from pathlib import Path

# Добавляем корень проекта в путь поиска модулей
sys.path.insert(0, str(Path(__file__).parent.parent))

from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
from models.data_model import DataModel
from controllers.main_controller import MainController


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    model = DataModel()
    controller = MainController(window, model)
    window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()
