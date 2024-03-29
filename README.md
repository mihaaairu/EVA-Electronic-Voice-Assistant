EVA - Electronic Vocie Assistant
================================
Данный проект является прототипом голосового ассистента с открытым исходным кодом. Подразумевается самостоятельное добавление необходимого функционала пользователем. Ассистент работает как в режиме чата, так и в голосовом режиме.
Все необъодимые инструкции по работе с ассистентом описаны в файле [***EVA - инструкция.pdf***](https://github.com/MikhailChertkov/EVA-Electronic-Voice-Assistant/blob/main/EVA%20-%20инструкция.pdf).  

**1) Для установки необходимых библиотек (зависимостей), создайте виртуальное окружение.**
        
        python -m venv venv
**2) Активируйте виртуальное окружение.**

        venv\Scripts\activate
**3) Установите зависимости.**
        
        pip install -r requirements.txt
**4) Установите библиотеку *'PyAudio'* с помощью модуля *'pipwin'*, установленного на шаге 3.**
        
        pipwin install PyAudio
**5) Скачайте [архив с голосовой моделью VOSK](https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip).**
        
**6) Распакуйте архив в папку *'EVA\back_end'* и присвойте распакованной папке имя *'vosk_small_model_ru'*.**

**7) В папке *'EVA\user_interface'* распакуйте архив *'icons.zip'*.**

Демонстрация работоспособности системы: 
=======================================        
**Окна чата с ассистентом:**

![Chat](https://user-images.githubusercontent.com/78261302/176164380-f3a2d487-c74c-4ef4-bfc3-d7015e50c522.png)

**Окно настроек ассистента:**

![Settings](https://user-images.githubusercontent.com/78261302/176164386-ec65c9df-4b6f-4dd6-befc-89456d153715.png)

**А также [видеодемонстрация](https://youtu.be/fySAufW8Gqk).**

