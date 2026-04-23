from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableView
from PySide6.QtCore import Signal
from .ui_main_window import Ui_MainWindow
import pyqtgraph as pg

class MainWindow(QMainWindow, Ui_MainWindow):
    # Сигналы для контроллера
    load_requested = Signal(str)  # путь к файлу
    method_changed = Signal(str)
    horizon_changed = Signal(int)
    alpha_changed = Signal(float)
    window_changed = Signal(int)
    calculate_requested = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Настройка pyqtgraph виджета
        self.graph_widget = pg.PlotWidget()
        layout = self.graph_container.layout()
        if layout is None:
            from PySide6.QtWidgets import QVBoxLayout
            layout = QVBoxLayout(self.graph_container)
        layout.addWidget(self.graph_widget)

        # Подключение сигналов UI к сигналам окна
        self.btn_load.clicked.connect(self.on_load_clicked)
        self.combo_method.currentTextChanged.connect(self.method_changed.emit)
        self.spin_horizon.valueChanged.connect(self.horizon_changed.emit)
        self.slider_alpha.valueChanged.connect(self._emit_alpha)
        self.spin_window.valueChanged.connect(self.window_changed.emit)
        self.btn_calc.clicked.connect(self.calculate_requested.emit)

        # Дополнительная настройка
        self.slider_alpha.setRange(5, 95)  # от 0.05 до 0.95
        self.slider_alpha.setValue(30)     # 0.3
        self.spin_window.setEnabled(False)  # сначала активен метод сглаживания

    def _emit_alpha(self, value):
        alpha = value / 100.0
        self.alpha_changed.emit(alpha)

    def on_load_clicked(self):
        path, _ = QFileDialog.getOpenFileName(self, "Выберите CSV", "", "CSV files (*.csv)")
        if path:
            self.load_requested.emit(path)

    def update_table(self, dataframe):
        """Отображает DataFrame в QTableView (упрощённо)"""
        from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

        class PandasModel(QAbstractTableModel):
            def __init__(self, data):
                super().__init__()
                self._data = data

            def rowCount(self, parent=QModelIndex()):
                return len(self._data)

            def columnCount(self, parent=QModelIndex()):
                return len(self._data.columns)

            def data(self, index, role=Qt.DisplayRole):
                if role == Qt.DisplayRole:
                    value = self._data.iloc[index.row(), index.column()]
                    return str(value)
                return None

            def headerData(self, section, orientation, role):
                if role == Qt.DisplayRole:
                    if orientation == Qt.Horizontal:
                        return str(self._data.columns[section])
                    else:
                        return str(self._data.index[section])
                return None

        model = PandasModel(dataframe)
        self.data_view.setModel(model)

    def plot_series(self, x, y, color='b', name=''):
        self.graph_widget.plot(x, y, pen=color, name=name)

    def clear_plot(self):
        self.graph_widget.clear()

    def show_message(self, title, text, icon=QMessageBox.Information):
        QMessageBox.information(self, title, text)

    def show_error(self, title, text):
        QMessageBox.critical(self, title, text)