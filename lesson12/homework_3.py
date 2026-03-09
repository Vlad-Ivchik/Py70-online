# 3.	Создайте класс LogReader, который читает строки из источника данных и является итерируемым объектом.
# Класс должен:
# -	поддерживать перебор через for
# -	пропускать пустые строки
# -	возвращать строки по одной без загрузки всех данных в память


class LogReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        """Делает класс итерируемым, открывая файл при начале цикла."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.strip()
                # Пропускаем пустые строки
                if cleaned_line:
                    yield cleaned_line

# --- Пример использования ---
# Создадим временный лог-файл
with open('test_log.log', 'w') as f:
    f.write("INFO: Start\n\nERROR: Something wrong\n\nDEBUG: End")

# Использование класса
reader = LogReader('test_log.log')
for log_entry in reader:
    print(log_entry)
