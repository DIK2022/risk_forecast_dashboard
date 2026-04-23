import pandas as pd
from PySide6.QtCore import QObject, Signal


class DataModel(QObject):
    data_loaded = Signal(pd.DataFrame) # emits DataFrame
    
    def __init__(self):
        suepr().__init__()
        self._data = None
        
    def load_csv(self, path: str):
        try:
            df = pd.read_csv(path)
            # Проверяем наличие колонок
            if 'value' not in df.columns:
                # Если нет 'value' ищем первую числовую колонку
                numeric_cols = df.select_dtypes(include='number').columns
                if len(numeric_cols) == 0:
                    raise ValueError("Файл не содержит числовых колонок")
                df = df.rename(columns={numeric_cols[0]: 'value'})
            if 'timestamp' not in df.columns:
                # создаем индекс
                df = df.reset_index().rename(columns={'index': 'timestamp'})
            self._data = df[['timestamp', 'value']].copy()
            self.data_loaded.emit(self._data)
        except Exception as e:
            raise RuntimeError(f"ошибка загрузки: {e}")
        
    def get_series(self):
        if self._data is not None:
            return self._data['value']
        return None
    