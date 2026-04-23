from src.models.data_model import DataModel
from src.views.main_window import MainWindow


class MainController:
    def __init__(self, view: MainWindow, model: DataModel):
        self.view = view
        
        # Подключаем сигналы
        self.view.loader_requested.connect(self.load_csv)
        self.model.data_loaded.connect(self.on_data_loaded)
        
    def load_csv(self, path: str):
        try:
            self.model.load_csv(path)
            self.view.show_massage("Успех", f"Загружен файл: {path}")
        except Exception as e:
            self.view.show_error("Ошибка", str(e))
            
    def on_data_loaded(self, df):
        self.view.update_table(df)
        # Временно отобразить график (просто значения)
        self.view.clear_plot()
        x = range(len(df))
        y = df['value'].values
        self.view.plot_series(x, y, color='b', name='Исходные')
        