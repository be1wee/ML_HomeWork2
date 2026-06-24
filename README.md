# ML_HomeWork2

Бейшеев Абай 972403  
Баженов Артемий 972403

# Локальный запуск:

### Установка Поетри:
pip install poetry

### Установка зависимостей:
poetry install

### Запуск для видео файла:
poetry run ZXCnumber --mode video --source data/input/closeDistance.mp4

### Запуск для стрима:
poetry run ZXCnumber --mode stream --source 0

# Запуск через Docker:

### Сборка образа
docker compose build

### Запуск для видео файла:
docker compose run --rm car-number-detector --mode video --source /app/data/input/closeDistance.mp4 --output /app/data/output/docker_result.mp4

### Запуск для стрима(определение номеров в видеофайле в режиме реального времени):
docker compose run --rm car-number-detector --mode stream --source /app/data/input/closeDistance.mp4

# Результат
data\demo\wdemo.gif

![воч демо](data\demo\wdemo-small.gif)
![воч демо](https://github.com/be1wee/ML_HomeWork2/blob/main/data/demo/wdemo.gif)
