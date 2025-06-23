def get_cats_info(path: str) -> list[dict[str, str]] | None:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            list_of_cats = []
            
            for line in file:
                cat_info = line.strip().split(',')
                
                if len(cat_info) != 3:
                    print(f"Неправильний формат рядка: {line.strip()}")
                    continue

                id, name, age = cat_info
                list_of_cats.append({"id": id, "name": name, "age": age})
            return list_of_cats
        
    except FileNotFoundError as e:
        print(f"Файл не знайдено: {e}")
        return None

# Example:

cats_info = get_cats_info("task_2/cats_info.txt")
print(cats_info)