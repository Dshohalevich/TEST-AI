# iOS-style Engineering Calculator (Windows, Go)

Приложение написано на Go и запускается как локальный калькулятор через встроенный HTTP-сервер.
Интерфейс стилизован под классический iOS-калькулятор и содержит инженерные функции (`sin`, `cos`, `tan`, `ln`, `log`, `sqrt`, `x^y`, `π`, `e`, `ANS`).

## Что уже готово

- Исходный код: `main.go` + `web/index.html`
- Бинарники не хранятся в git (чтобы не ломать создание PR).

## Сборка Windows `.exe`

Соберите бинарник локально:

```bash
GOOS=windows GOARCH=amd64 go build -o ios_engineering_calculator.exe .
```

После сборки файл `ios_engineering_calculator.exe` появится в корне проекта.

## Быстрый запуск на Windows 11 (если «не запускается»)

1. Скопируйте `ios_engineering_calculator.exe` на ПК с Windows 11.
2. Запустите двойным кликом.
3. Если браузер не открылся автоматически — откройте вручную:
   - `http://127.0.0.1:8080`
4. Если Windows SmartScreen блокирует запуск:
   - нажмите **More info** → **Run anyway**.

## Типичные проблемы и решение

- **Пустая страница / не открывается**
  - Убедитесь, что открываете именно `http://127.0.0.1:8080`.
- **Порт занят**
  - Закройте процесс, который использует `8080`, либо измените порт в `main.go`.
- **Антивирус блокирует `.exe`**
  - Добавьте файл в исключения или подпишите бинарник сертификатом.

## Публикация на GitHub

### Вариант 1 (через сайт GitHub)

1. Создайте новый пустой репозиторий на GitHub (без README).
2. Выполните:

```bash
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin work
```

### Вариант 2 (через GitHub CLI)

```bash
gh repo create <repo-name> --public --source=. --remote=origin --push
```

## Пересборка

```bash
go build -o ios_engineering_calculator.exe .
```

или кросс-компиляция из Linux/macOS:

```bash
GOOS=windows GOARCH=amd64 go build -o ios_engineering_calculator.exe .
```
