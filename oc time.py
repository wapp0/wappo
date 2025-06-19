import time

def bootloader():
    print("Загрузчик ОС: Инициализация...")
    time.sleep(1)
    print("Загрузка завершена.\n")

def show_help():
    print("Доступные команды:")
    print("  time  - показать текущее время")
    print("  help  - показать список команд")
    print("  exit  - выйти из системы")

def main_loop():
    while True:
        cmd = input(">>> ").strip().lower()
        if cmd == "time":
            print("Текущее время:", time.strftime("%H:%M:%S"))
        elif cmd == "help":
            show_help()
        elif cmd == "exit":
            print("Выход из системы...")
            break
        elif cmd == "":
            continue
        else:
            print(f"Неизвестная команда: {cmd}. Введите 'help' для списка команд.")

if __name__ == "__main__":
    bootloader()
    print("Добро пожаловать в простую ОС!")
    show_help()
    main_loop()
