Данный проект является прототипом голосового ассистента с открытым исходным кодом. Подразумевается самостоятельное добавление необходимого функционала пользователем. Все необъодимые инструкции по работе с ассистентом описаны в файле 'EVA - инструкция.pdf'. 


1) Для установки необходимых библиотек(зависимостей), создайте виртуальное окружение.
    команда:
        python -m venv venv
2) Активируйте виртуальное окружение.
    команда:
        venv\Scripts\activate
3) Установите зависимости.
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



![Chat](https://user-images.githubusercontent.com/78261302/176162777-a2875b90-aace-41ea-bf6a-b0de8ef1dd3d.png)
![Settings](https://user-images.githubusercontent.com/78261302/176162779-fb394309-bc33-4613-be30-9e18e0704003.png)
