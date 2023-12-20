# Используем базовый образ Python
FROM python:3.8

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущего каталога в рабочую директорию
COPY . .

# Команда для выполнения приложения
CMD ["pytest"]
