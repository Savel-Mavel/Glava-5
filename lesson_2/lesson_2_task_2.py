
n = int(input("Введите год: "))

def is_year_leap(year: int) -> bool:
       return year % 4 == 0

result = is_year_leap(n)
print(f"год {n}: {result}")