# Api_YaMDB

![example workflow](https://github.com/Victor23rus/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

## Запуск проекта

Клонировать репозиторий, открыть проект и создать виртуальное окружение:
```bash
git clone https://github.com/themasterid/infra_sp2
cd infra_sp2
cd api_yamdb

Создать и активировать виртуальное окружение

python -m venv venv
source venv/Scripts/activate
```
Установить зависимости:

```bash
pip install -r requirements.txt
```

Переходим в папку с файлом docker-compose.yaml:

```bash
cd infra
```

Поднимаем контейнеры (infra_db_1, infra_web_1, infra_nginx_1):

```bash
docker-compose up -d --build
```

Выполняем миграции:

```bash
docker-compose exec web python manage.py migrate
```

Создаем суперпользователя:

```bash
docker-compose exec web python manage.py createsuperuser
```

Србираем статику:

```bash
docker-compose exec web python manage.py collectstatic --no-input
```

Создаем дамп базы данных (нет в текущем репозитории):

```bash
docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json
```

Останавливаем контейнеры:

```bash
docker-compose down -v
```
Сервер будет доступен по адресу: http://localhost/api/v1/

Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
