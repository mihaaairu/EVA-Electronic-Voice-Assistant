1) Для установки необходимых библиотек(зависимостей), создайте виртуальное окружение (в PyCharm, обычно, создается автоматически, при создании проекта).
    команда:
        python -m venv venv
2) Активируйте виртуальное окружение.
    команда:
        venv\Scripts\activate
3) Установите зависимости (библиотеки).
    команда:
        pip install -r requirements.txt
4) Установите библиотеку 'PyAudio' с помощью модуля 'pipwin', установленного на шаге 3.
    команда:
        pipwin install PyAudio
5) Скачайте архив с голосовой моделью VOSK
    ссылка:
        https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip
6) Распакуйте архив в папку 'EVA\back_end' и присвойте распакованной папке имя 'vosk_small_model_ru'.
7) В папке EVA\user_interface распакуйте архив icons.zip.