def extract_errors(filename):
    # Создаем пустой список, куда будем складывать ошибки
    error_list = []
    
    # Используем try/except, чтобы программа не упала, если файла нет
    try:
        file = open(filename, 'r', encoding='utf-8')
        
        # Перебираем файл построчно с помощью цикла for
        for line in file:
            
            # Строковые методы (strings) и условия (conditionals)
            # Если строка начинается с INFO, пропускаем ее с помощью continue
            if line.startswith('INFO'):
                continue
            
            # Если в строке есть слово ERROR, обрабатываем ее
            if 'ERROR' in line:
                # Разрезаем строку по пробелам на список слов
                # Пример: ['2026-11-10', '10:05', 'ERROR', 'App', 'crashed', 'on', 'Android']
                words = line.split()
                
                # Берем дату (первое слово, индекс 0)
                date = words[0]
                # Берем платформу (последнее слово, индекс -1)
                platform = words[-1]
                
                # Создаем кортеж (tuple) с нужными данными
                error_record = (date, platform)
                
                # Добавляем кортеж в наш список
                error_list.append(error_record)
                
        file.close()
        
    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename.")
        return [] # Возвращаем пустой список в случае ошибки
        
    return error_list

# --- Основная часть программы ---

print("Starting log analysis...")

# Вызываем нашу функцию
found_errors = extract_errors('server_logs.txt')

# Проверяем, нашли ли мы что-нибудь
if len(found_errors) > 0:
    print("Found critical errors:")
    
    # Еще один цикл for, чтобы красиво вывести результат
    for error in found_errors:
        date = error[0]
        platform = error[1]
        print(f"- Crash on {date} (Platform: {platform})")
        
    print(f"Total errors found: {len(found_errors)}")
else:
    print("No errors found or file is empty.")