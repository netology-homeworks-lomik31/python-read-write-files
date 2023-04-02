# Небольшой гайд по использованию `FileCombiner.py`

-----
Запуск происходит в методе Main класса Program:

```py
class Program:
    def Main():

        # your code here
        
        pass
```

Запуск производится вызовом метода `Combine` класса `Combiner`:
```py
Combiner.Combine()
```

Метод принимает параметрами:

1. Полный (абсолютный или относительный) путь к файлу сохранения (в который произведётся запись результата)

2. Словарь с информацией о файлах в виде `{"filename": linesCount}`

3. Путь к папке, в которой лежат файлы, которые нужно обработать

Словарь с данными можно получить выполнив команду
```py
CreateDictOfFilesData()
```

Она параметрами принимает следующие аргументы:

1. Путь к папке, в которой лежат файлы для обработки. **ОБЯЗАТЕЛЬНО** должен совпадать с путем для `Combiner.Combine()`

2. Список файлов внутри папки из прошлого пункта, которые необходимо обработать (включая расширение файла)

Таким образом, запуск скрипта должен выглядеть примерно следующим образом:

```py
folderPath = "files"
Combiner.Combine("files/res.txt", Reader.CreateDictOfFilesData(folderPath, ["1.txt", "2.txt"]), folderPath)
```

В данном примере обрабатываемые файлы хранятся в папке `files` и имеют названия `1.txt` и `2.txt`, а файл с результатом выполнения будет лежать находиться по пути `files/res.txt`