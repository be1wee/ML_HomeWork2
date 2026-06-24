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

![воч демо](https://github.com/be1wee/ML_HomeWork2/blob/main/data/demo/wdemo-small.gif)


# Качество модели

Модель обучена для детекции автомобильных номеров на основе архитектуры **YOLOv8n**

### Итоговые метрики (лучшая модель)

| Метрика | Значение |
|---------|----------|
| **mAP50** | 0.995 |
| **mAP50-95** | 0.895 |
| **Precision (P)** | 0.797 |
| **Recall (R)** | 0.971 |
| **Fitness** | 0.895 |

### Описание датасета

- **Источник:** Собственный датасет, собранный на основе кадров из видео с автомобильными номерами в папке dataset
- **Количество изображений:** 
  - Train: 70 изображения
  - Validation: 3 изображения
  - Test: используется отдельно (не входил в обучение)
- **Количество классов:** 2 (`car number`, `car_number` — фактически один класс, но в разметке были разные названия, случайно создал второй класс)
- **Разметка:** Выполнена вручную с помощью платформы [Roboflow](https://roboflow.com).

### Процесс обучения

- **Среда:** Google Colab (CPU, Intel Xeon @ 2.20GHz)
- **Количество эпох:** 100
- **Время обучения:** ~1.8 часа