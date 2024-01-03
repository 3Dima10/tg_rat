import subprocess
import time


def run_in_background(command):
    # Запускаем процесс в скрытом режиме
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE

    process = subprocess.Popen(command, startupinfo=startupinfo)

    # Минимальная задержка, чтобы процесс успел запуститься
    time.sleep(1)

    # Скрываем окно после запуска
    process_handle = process._handle
    subprocess.run(["taskkill", "/F", "/T", "/PID", str(process_handle)])


if __name__ == "__main__":
    # Замените "your_script.py" на имя вашего скрипта
    run_in_background(["python", "tg_main.py"])
