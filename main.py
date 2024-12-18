# vazifa 1
import time
from threading import Thread

def numbers(num: str):
    yigindi = 0
    for i in num:
        print("Sonlar yig‘indisi hisoblanmoqda...")
        time.sleep(0.5)
        yigindi += int(i)
        print("Sonlar yig‘indisi hisoblandi!")

num = input("Son kiriting: ")

start = time.time()

threades = []

for i in range(100):
    th1 = Thread(target=numbers, args=(num,))
    th1.start()
    threades.append(th1)


for th1 in threades:
    th1.join()

end = time.time()

print(f"Dastur ishlash vaqti: {round(end - start, 2)} soniya")

# ============================================================================

# vazifa 2
import time
from threading import Thread

def formatlash(sekund: int):
    print("Formatlanmoqda...")
    time.sleep(1)
    kun = sekund // 86400
    sekund %= 86400

    soat = sekund // 3600
    sekund %= 3600

    minut = sekund // 60
    sekund %= 60
    print("Formatlandi!!!")
    return f"{kun} kun, {soat} soat, {minut} minut, {sekund} sekund"

sekund = input("Sekundni kiritin: ")

RED = "\033[31m"
RESET = "\033[0m"

if sekund.isdigit():
    sekund = int(sekund)

    start = time.time()

    threades = []

    for i in range(100):
        th1 = Thread(target=formatlash, args=(sekund,))
        th1.start()
        threades.append(th1)


    for th1 in threades:
        th1.join()

    end = time.time()
    print(f"Natija {formatlash(sekund)}\nDastur ishlash vaqti: {round(end - start, 2)} soniya")

else:
    print(RED + "Son kiritin harf emas!!!" + RESET)

# ============================================================================

# vazifa 3
import time
from threading import Thread, Lock

new_names = []
lock = Lock()


def capitalize_str(royxat: list):
    print("So'zning bosh harfi katta qilinmoqda...")
    local_names = []
    for i in royxat:
        time.sleep(0.5)
        l = i.capitalize()
        local_names.append(l)
    with lock:
        new_names.extend(local_names)
    print("So'zning bosh harfi katta qilindi!!!")
    return f"Natija {local_names}"


names = ['alfred', 'tabitha', 'william', 'arla']

threads = []

start = time.time()

for i in range(100):
    th = Thread(target=capitalize_str, args=(names,))
    th.start()
    threads.append(th)

for th in threads:
    th.join()

end = time.time()

print(capitalize_str(names))
print(f"Ishlash vaqti: {end - start:.2f} soniya")

# ============================================================================

# vazifa 4
import time
from threading import Thread, Lock

new_names = []
lock = Lock()


def numbers(royxat: list):
    print("Tekshiruv amalga oshmoqda...")
    local_nums = []
    for i in royxat:
        time.sleep(0.5)
        if i > 75:
            local_nums.append(i)
    with lock:
        new_names.extend(local_nums)
    print("Tekshiruv yakunlandi!!!")
    return f"Natija {local_nums}"

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

threads = []

start = time.time()

for i in range(100):
    th = Thread(target=numbers, args=(scores,))
    th.start()
    threads.append(th)

for th in threads:
    th.join()

end = time.time()

print(numbers(scores))
print(f"Dastur ishlash vaqti: {end - start:.2f} soniya")

# ============================================================================

# vazifa 5
import time
from threading import Thread

def find_palindromes(words):
    word_list = []
    print("Tekshiruv amalga oshmoqda...")
    for i in words:
        if i.lower() == i.lower()[::-1]:
            word_list.append(i)
            time.sleep(0.5)
    print("Tekshiruv amalga oshirildi!!!")
    return word_list

words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']

threads = []

start = time.time()

for i in range(100):
    th = Thread(target=find_palindromes, args=(words,))
    th.start()
    threads.append(th)

for th in threads:
    th.join()

end = time.time()

print("Natija: ",find_palindromes(words))
print(f"Dastur ishlash vaqti: {end - start:.2f} soniya")

# ============================================================================

# vazifa 6
import time
from threading import Thread

def orin_almashtirish(text: str):
    result = ""
    index = 0
    while index < len(text):
        print("Tekshiruv amalga oshmoqda...")
        time.sleep(0.5)
        if text[index] == 'e':
            result += '3'
        else:
            result += text[index]
        index += 1
        print("Tekshiruv amalga oshirildi!!!")
    return result

text = input("Matn kiriting: ")

threads = []

start = time.time()

for i in range(100):
    th = Thread(target=orin_almashtirish, args=(text,))
    th.start()
    threads.append(th)

for th in threads:
    th.join()

end = time.time()


print("Natija:", orin_almashtirish(text))
print(f"Dastur ishlash vaqti: {end - start:.2f} soniya")

# ============================================================================

# vazifa 7
import time
from threading import Thread

def orin_almashtirish(text: str):
    result = ""
    index = 0
    while index < len(text):
        print("Tekshiruv amalga oshmoqda...")
        time.sleep(0.5)
        if text[index] != ' ':
            result += text[index]
        index += 1
        print("Tekshiruv amalga oshirildi!!!")
    return result

text = input("Matn kiriting: ")

threads = []

start = time.time()

for i in range(100):
    th = Thread(target=orin_almashtirish, args=(text,))
    th.start()
    threads.append(th)

for th in threads:
    th.join()

end = time.time()

print("Natija:", orin_almashtirish(text))
print(f"Dastur ishlash vaqti: {end - start:.2f} soniya")

# ============================================================================

# vazifa 8
import time
from threading import Thread

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def kopaytirish(numbers: list):
    new_numbers = []
    for i in numbers:
        print("Tekshiruv amalga oshmoqda...")
        time.sleep(1)
        a = i * 2
        new_numbers.append(a)
        print("Tekshiruv amalga oshirildi!!!")
    return new_numbers
threads = []

start = time.time()

for i in range(100):
    th = Thread(target=kopaytirish, args=(numbers,))
    th.start()
    threads.append(th)

for th in threads:
    th.join()

end = time.time()

print("Natija: ",kopaytirish(numbers))
print(f"Dastur ishlash vaqti: {end - start:.2f} soniya")

# ============================================================================

# vazifa 9
import threading
import random
import time

results = []

lock = threading.Lock()

def generate_random_number():
    num = random.randint(1, 100)
    print("Tekshiruv amalga oshmoqda...")
    time.sleep(0.5)
    print("Tekshiruv amalga oshirildi!!!")

    with lock:
        results.append(num)


if __name__ == "__main__":
    threads = []
    start = time.time()

    for _ in range(10):
        thread = threading.Thread(target=generate_random_number)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.time()

    print("Har bir oqim yaratgan tasodifiy sonlar:", results)
    print(f"Dastur ishlash vaqti: {end - start:.2f} soniya")
