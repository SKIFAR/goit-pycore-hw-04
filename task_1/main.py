def total_salary(path: str) -> tuple[int, int] | None:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            count = 0

            for line in file:
                line_parts = line.strip().split(',')

                if len(line_parts) != 2:
                    print(f"Неправильний формат рядка: {line.strip()}")
                    continue

                try:
                    salary = int(line_parts[1])
                    total_salary += salary
                    count += 1

                except ValueError:
                    print(f"Неправильний формат рядка: {line.strip()}")
                    continue

            if count == 0:
                print("Не знайдено жодної заробітної плати.")
                return (0, 0)

            average_salary = total_salary // count
            return (total_salary, average_salary)
    
    except FileNotFoundError as e:
        print(f"Файл не знайдено: {e}")
        return None
    
# Example:
total, average = total_salary("task_1/monthly_salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")