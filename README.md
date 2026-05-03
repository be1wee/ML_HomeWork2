# ML_HomeWork2

Бейшеев Абай 972403  
Баженов Артемий 972403

# Локальный запуск:

### Установка зависимостей
pip install poetry

### Запуск для видео файла:
poetry run ZXCnumber --mode video --source ПУТЬ_ДО_ВИДЕО

### Запуск для стрима:
poetry run ZXCnumber --mode stream --source 0

# Запуск через Docker:

### Сборка образа
docker compose build

### Запуск для видео файла:
docker compose run --rm car-number-detector --mode video --source ПУТЬ_ДО_ВИДЕО --output ПУТЬ_КУДА_СОХРАНИТЬ_НАДОБНО

### Запуск для стрима(определение номеров в видеофайле в режиме реального времени):
docker compose run --rm car-number-detector --mode stream --source ПУТЬ_ДО_ВИДЕО

# Результат
![описание](data\demo\wdemo.gif)
