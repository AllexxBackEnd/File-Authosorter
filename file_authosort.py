import time
import shutil
from pathlib import Path

# HOME directory of the current user.
# Домашняя директория текущего пользователя.
HOME = Path.home()

# Folder to be monitored for new files (default: Downloads).
# Папка, которую нужно мониторить на наличие новых файлов
# (по умолчанию: Downloads).
WATCH_FOLDER = HOME / "Downloads"

# File categories and their corresponding extensions.
# Категории файлов и соответствующие им расширения.
TARGETS = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt",
                  ".pptx"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "videos": [".mp4", ".avi", ".mov", ".mkv"],
    "audio": [".mp3", ".wav", ".ogg", ".flac"],
}


def ensure_dirs():
    """
    Create category folders inside the watch directory
    if they don't already exist.
    Создаёт папки категорий внутри отслеживаемой директории,
    если они ещё не существуют.
    """
    for folder in TARGETS:
        (WATCH_FOLDER / folder).mkdir(exist_ok=True)

    # Folder for uncategorized file types.
    # Папка для файлов, не подошедших ни под одну категорию.
    (WATCH_FOLDER / "other").mkdir(exist_ok=True)


def move_file(file_path: Path):
    """
    Move a file to the appropriate category folder based on its extension.
    Перемещает файл в соответствующую папку категории на основе его расширения.
    """
    ext = file_path.suffix.lower()

    # Iterate through categories and check if extension matches.
    # Перебор категорий и проверка, подходит ли расширение.
    for target_folder, extensions in TARGETS.items():
        if ext in extensions:
            dest = WATCH_FOLDER / target_folder / file_path.name
            shutil.move(str(file_path), str(dest))
            print(f"Перемещён: {file_path.name} → {target_folder}")
            return

    # If no category matches, move the file to "other".
    # Если расширение не подошло — переместить в категорию "other".
    dest = WATCH_FOLDER / "other" / file_path.name
    shutil.move(str(file_path), str(dest))
    print(f"Перемещён: {file_path.name} → other")


def monitor():
    """
    Continuously monitor the Downloads folder
    and sort incoming files every 5 seconds.
    Непрерывно мониторит папку Downloads и сортирует
    поступающие файлы каждые 5 секунд.
    """
    print(f"Мониторинг папки: {WATCH_FOLDER}")
    ensure_dirs()

    while True:
        # Process all files in the watched folder.
        # Обрабатывает все файлы в отслеживаемой папке.
        for file in WATCH_FOLDER.iterdir():
            if file.is_file():
                move_file(file)

        # Delay between checks.
        # Пауза между проверками.
        time.sleep(5)


if __name__ == "__main__":
    # Start the monitoring process.
    # Запуск процесса мониторинга.
    monitor()
