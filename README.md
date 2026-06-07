# Лаба №1 — CI/CD пайплайн (GitHub Actions + Docker)

Мини-приложение на Flask с автоматическим пайплайном: на каждый push тесты прогоняются, и при успехе собирается Docker-образ и пушится в GitHub Container Registry (GHCR).

## Структура проекта
```
lab1-cicd/
├── app.py                      # Flask-приложение (2 эндпоинта)
├── test_app.py                 # тесты (pytest)
├── requirements.txt            # зависимости
├── Dockerfile                  # как упаковать в контейнер
└── .github/workflows/ci.yml    # сам CI/CD пайплайн
```

## Шаг 1. Проверить локально (опционально, но полезно)
```bash
pip install -r requirements.txt
pytest -v                       # должны пройти 2 теста

# собрать и запустить контейнер
docker build -t lab1 .
docker run -p 8080:8080 lab1
# открой http://localhost:8080  и  http://localhost:8080/health
```

## Шаг 2. Залить на GitHub
```bash
git init
git add .
git commit -m "Lab 1: CI/CD pipeline"
git branch -M main
# создай пустой репозиторий на github.com, затем:
git remote add origin https://github.com/<твой-логин>/<имя-репо>.git
git push -u origin main
```

## Шаг 3. Посмотреть пайплайн
- Открой репозиторий → вкладка **Actions**.
- Увидишь запуск workflow «CI»: сначала job `test`, затем `build-and-push`.
- Зелёная галочка = всё прошло.

## Шаг 4. Найти собранный образ
- Профиль/репо → вкладка **Packages** → там появится образ `ghcr.io/<логин>/<репо>:latest`.

## Проверь, что понял (вопросы к самому себе)
1. Почему `build-and-push` стоит на `needs: test`? Что будет, если тест упадёт?
2. Чем отличается `uses:` от `run:` в шаге?
3. Зачем в Dockerfile `requirements.txt` копируется отдельно ДО остального кода?
4. Почему секрет (`GITHUB_TOKEN`) не пишут прямо в YAML?
5. Jobs бегут параллельно или последовательно? А steps внутри job?

## Идеи «прокачать» (для истории на собесе)
- Добавить шаг линтера (`flake8` / `ruff`) перед тестами.
- Добавить кэш зависимостей (`actions/setup-python` с `cache: pip`).
- Заменить тег `latest` на тег по git-коммиту (`${{ github.sha }}`).
- Заменить запуск `python app.py` на `gunicorn` (прод-вариант).
- Добавить matrix-сборку под несколько версий Python.
