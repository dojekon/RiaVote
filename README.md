## ПРИНИМАЮТСЯ ISSUE'S - НЕОБХОДИМА ПОМОЩЬ С БАЙПАСОМ РЕКАПЧИ ИЛИ ПОЛУЧЕНИЕМ НОВОГО ТОКЕНА ПЕРЕД ОТПРАВКОЙ ЗАПРОСА
Рекомендуется использовать свои ключи для рекапчи!
## Инструкция по запуску голосования на компьютерах под управлением Windows и Linux

### Windows

1. **Установка Python:**
   - Убедитесь, что на вашем компьютере установлен Python. Если нет, скачайте и установите Python с [официального сайта](https://www.python.org/).

2. **Скачивание кода:**
   - Скачайте код с репозитория или скопируйте его в текстовый файл с расширением `.py`.

3. **Создание конфигурационного файла:**
   - Создайте файл `config.ini` и добавьте в него следующий содержимый, заменив `...` на ваш реальный ключ `g_recaptcha_response`:
     ```ini
     [Vote]
     vote_id = 1911654209
     g_recaptcha_response = ...
     ```

4. **Открытие командной строки:**
   - Откройте командную строку (cmd).

5. **Переход в папку с кодом:**
   - Перейдите в папку, содержащую файл с кодом и `config.ini` с помощью команды `cd путь_к_папке`.

6. **Установка зависимостей:**
   - Выполните команду `pip install requests` для установки библиотеки `requests`.

7. **Запуск кода:**
   - Выполните команду `python ваш_файл.py`, где `ваш_файл.py` - это имя вашего файла с кодом.

### Linux

1. **Установка Python:**
   - Убедитесь, что на вашем компьютере установлен Python. В большинстве случаев, Python предустановлен. Если нет, установите его через менеджер пакетов вашего дистрибутива (например, `sudo apt-get install python3` на Ubuntu).

2. **Скачивание кода:**
   - Скачайте код с репозитория или скопируйте его в текстовый файл с расширением `.py`.

3. **Создание конфигурационного файла:**
   - Создайте файл `config.ini` и добавьте в него следующий содержимый, заменив `...` на ваш реальный ключ `g_recaptcha_response`:
     ```ini
     [Vote]
     vote_id = 1911654209
     g_recaptcha_response = ...
     ```

4. **Открытие терминала:**
   - Откройте терминал.

5. **Переход в папку с кодом:**
   - Перейдите в папку, содержащую файл с кодом и `config.ini` с помощью команды `cd путь_к_папке`.

6. **Установка зависимостей:**
   - Выполните команду `pip install requests` для установки библиотеки `requests`. Если `pip` не установлен, установите его с помощью `sudo apt-get install python3-pip`.

7. **Запуск кода:**
   - Выполните команду `python3 ваш_файл.py`, где `ваш_файл.py` - это имя вашего файла с кодом.

**Примечание:** В случае возникновения проблем с выполнением команды `pip`, попробуйте использовать `pip3` вместо `pip` на Linux.



# Голосование в конкурсе с использованием Python

Этот код представляет собой простой скрипт на языке Python, предназначенный для автоматизированного голосования в конкурсе с использованием веб-запросов.

## Описание файла `config.ini`

Файл `config.ini` используется для хранения параметров, необходимых для голосования. В данном случае, параметры `vote_id` и `g_recaptcha_response` читаются из этого файла. Пример содержимого файла:

```ini
[Vote]
vote_id = 1911654209
g_recaptcha_response = 03AFcWeA4TF1JtU1A8CK6XP657NC2EQ2B_RN19LYrmubfeJIoENEuBeEYurfnjuR2Ol1f3tUb-JhTD0ZPKnmfxLdQG_3o1Rf-kpZO6CGPyQ0RAiXP_cgGNfFymLcwwKdEwWNW2CoUZyRAioUiNIwoX_7t8hVDZp4T7MLmGQc7ZU-wo_R3agTA2bCuHRM9742hGlZxvrKJfMn7O4nxdHf3jVsJdmF1Kv0ADl5u9gEG5FLD5Yy4cxMitIseOf5y72Dj09AATYMN4i9wZwXQiEYWuViDUD0RSnQDDrXIALdrS_bdueWHCLmJJLIs2MrQVWKdQYOutzrD1OYNJSpvA4Q1MhPA4sz7XEOCypY6_8sHOFUD7FtFuMpiKTutuIuvdSUsuyXuK_GST1U6kY4DCIeCoxJHxbwFP5mH6PUj4kmSKAbon8ZFglDU3CMXzjSpOftBKJQWpG2en3UIf15ZcRqKmcsI9ucRqe_eN8yoZPMwMoeKBnKHTptLedn2S7rXE9kipMTPHWGR_H2Zqm8PD8KDpiF-b8l3FSRV_Tg20aw-Za-fnPijLoFDHYTCnuFkioWjbHYJ8v8YennmK
```

## Описание кода

### Функция `read_config`

```python
def read_config(filename='config.ini'):
    # ...
```

Функция `read_config` отвечает за чтение параметров из файла конфигурации (`config.ini`). В данном случае, она возвращает `vote_id` и `g_recaptcha_response`.

### Функция `vote`

```python
def vote(vote_id, g_recaptcha_response):
    # ...
```

Функция `vote` отправляет веб-запрос для голосования с использованием предоставленных параметров `vote_id` и `g_recaptcha_response`.

### Функция `vote_in_thread`

```python
def vote_in_thread(vote_id, g_recaptcha_response, thread_number):
    # ...
```

Функция `vote_in_thread` представляет потоковую логику. Она вызывает функцию `vote` в бесконечном цикле с интервалом в 10 секунд. Результат голосования выводится в лог.

### Запуск 10 потоков

```python
# ...
for i in range(10):
    thread = threading.Thread(target=vote_in_thread, args=(vote_id, g_recaptcha_response, i + 1))
    threads.append(thread)
    thread.start()
# ...
```

Код создает 10 потоков, каждый из которых выполняет функцию `vote_in_thread`. Каждый поток имеет уникальный номер.

### Ожидание завершения потоков

```python
# ...
for thread in threads:
    thread.join()
# ...
```

После запуска потоков происходит ожидание их завершения, чтобы гарантировать корректное завершение программы.
