# Automatic Downloads Folder File Sorter

A cross-platform Python script that automatically monitors the user's **Downloads** directory and sorts files into structured subfolders based on file type.

---

## 🌍 English Documentation

### 📌 Overview
This Python script automatically organizes files in the user's **Downloads** folder by monitoring it and sorting files into categorized subdirectories. It simplifies file management and keeps the Downloads folder clean.

---

## ✨ Features
- Auto-detects the user's Downloads folder  
- Monitors the folder every 5 seconds  
- Sorts files into:
  - `images/`
  - `documents/`
  - `archives/`
  - `videos/`
  - `audio/`
  - `other/`
- Automatically creates required folders  
- Works on Windows, macOS, and Linux  

---

## 📥 Installation
1. Install **Python 3.8** or newer  
2. Download the script file:  
   **`auto_sort_downloads.py`**
3. Run the script:

```bash
python auto_sort_downloads.py
```

---

## ⚙️ How It Works
- Detects the path to the user's Downloads directory  
- Creates necessary folders if they are missing  
- Scans the directory every 5 seconds  
- Moves files based on their extensions  

Resulting structure:

```text
Downloads/
├── images/
├── documents/
├── archives/
├── videos/
├── audio/
└── other/
```

---

## 📂 Supported File Types

### Images  
`jpg, jpeg, png, gif, bmp, svg, webp`

### Documents  
`pdf, doc, docx, txt, xls, xlsx, ppt, pptx`

### Archives  
`zip, rar, 7z, tar, gz`

### Videos  
`mp4, avi, mov, mkv`

### Audio  
`mp3, wav, ogg, flac`

---

## ⚠️ Limitations
- The script must remain running to monitor the directory  
- Large or currently-downloading files may require extra time before being moved  

---

## 📄 License
MIT License

---

# 🇷🇺 Русская документация

## 📌 Обзор
Этот Python-скрипт автоматически сортирует файлы в папке **Загрузки**, регулярно проверяя её и раскладывая файлы по категориям. Он помогает поддерживать порядок и избавляет от ручной сортировки.

---

## ✨ Возможности
- Автоматически определяет папку Загрузки  
- Сканирует папку каждые 5 секунд  
- Сортирует файлы по папкам:
  - `images/`
  - `documents/`
  - `archives/`
  - `videos/`
  - `audio/`
  - `other/`
- Сам создаёт необходимые каталоги  
- Работает на Windows, macOS и Linux  

---

## 📥 Установка
1. Установите **Python 3.8** или новее  
2. Скачайте файл:  
   **`auto_sort_downloads.py`**  
3. Запустите скрипт:

```bash
python auto_sort_downloads.py
```

---

## ⚙️ Принцип работы
- Определяет путь к папке Загрузки  
- Создаёт необходимые каталоги (если отсутствуют)  
- Каждые 5 секунд проверяет её содержимое  
- Перемещает файлы в зависимости от расширения  

Структура папки после сортировки:

```text
Downloads/
├── images/
├── documents/
├── archives/
├── videos/
├── audio/
└── other/
```

---

## 📂 Поддерживаемые типы файлов

### Изображения  
`jpg, jpeg, png, gif, bmp, svg, webp`

### Документы  
`pdf, doc, docx, txt, xls, xlsx, ppt, pptx`

### Архивы  
`zip, rar, 7z, tar, gz`

### Видео  
`mp4, avi, mov, mkv`

### Аудио  
`mp3, wav, ogg, flac`

---

## ⚠️ Ограничения
- Скрипт должен работать постоянно  
- Файлы, которые ещё загружаются, могут переместиться с задержкой  
