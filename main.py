import os
import requests
import aiohttp
import asyncio
from bs4 import BeautifulSoup

# Задание 1а: Загрузка 10 случайных картинок с использованием requests
def download_images_requests():
    image_urls = [
        "https://picsum.photos/200/300?random=1",
        "https://picsum.photos/200/300?random=2",
        "https://picsum.photos/200/300?random=3",
        "https://picsum.photos/200/300?random=4",
        "https://picsum.photos/200/300?random=5",
        "https://picsum.photos/200/300?random=6",
        "https://picsum.photos/200/300?random=7",
        "https://picsum.photos/200/300?random=8",
        "https://picsum.photos/200/300?random=9",
        "https://picsum.photos/200/300?random=10",
    ]

    if not os.path.exists("images_requests"):
        os.makedirs("images_requests")

    for i, url in enumerate(image_urls):
        response = requests.get(url)
        with open(f"images_requests/image_{i + 1}.jpg", "wb") as file:
            file.write(response.content)

# Задание 1а (продолжение): Загрузка 10 случайных картинок с использованием aiohttp
async def download_image_aiohttp(url, folder, index):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            with open(f"{folder}/image_{index}.jpg", "wb") as file:
                file.write(content)

async def download_images_aiohttp():
    image_urls = [
        "https://picsum.photos/200/300?random=1",
        "https://picsum.photos/200/300?random=2",
        "https://picsum.photos/200/300?random=3",
        "https://picsum.photos/200/300?random=4",
        "https://picsum.photos/200/300?random=5",
        "https://picsum.photos/200/300?random=6",
        "https://picsum.photos/200/300?random=7",
        "https://picsum.photos/200/300?random=8",
        "https://picsum.photos/200/300?random=9",
        "https://picsum.photos/200/300?random=10",
    ]

    folder = "images_aiohttp"
    if not os.path.exists(folder):
        os.makedirs(folder)

    tasks = [download_image_aiohttp(url, folder, i + 1) for i, url in enumerate(image_urls)]
    await asyncio.gather(*tasks)

# Задание 1б: Сохранение картинок в разные папки
def save_images_to_folders():
    if not os.path.exists("images_folders"):
        os.makedirs("images_folders")

    for i in range(10):
        folder = f"images_folders/folder_{i + 1}"
        if not os.path.exists(folder):
            os.makedirs(folder)

        src_path = f"images_requests/image_{i + 1}.jpg"
        dest_path = f"{folder}/image_{i + 1}.jpg"

        if os.path.exists(src_path):
            with open(src_path, "rb") as src_file:
                with open(dest_path, "wb") as dest_file:
                    dest_file.write(src_file.read())

# Задание 2а: Получение погоды с использованием string.split()
def get_weather_string_split():
    url = "https://www.timeanddate.com/weather/kazakstan/astana"
    headers = {'User-Agent': 'Mozilla/5.0', 'Host': 'www.timeanddate.com'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        page_content = response.text
        page_content = page_content.replace("&nbsp;", " ")

        data = page_content.split('Feels Like:')
        if len(data) > 1:
            temperature = data[1].split('°C')[0].strip()
            print(f"Погода в Астане: {temperature}°C")
        else:
            print("Не удалось найти данные о температуре.")
    else:
        print(f"Ошибка при получении данных: {response.status_code}")

# Задание 2б: Получение погоды с использованием bs4 (BeautifulSoup)
def get_weather_bs4():
    url = "https://www.timeanddate.com/weather/kazakstan/astana"
    headers = {'User-Agent': 'Mozilla/5.0', 'Host': 'www.timeanddate.com'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        first_item = soup.select_one('#qlook p:nth-of-type(2)')
        if first_item:
            feels_like = first_item.get_text().replace("&nbsp;", " ").strip()
            print(f"Погода в Астане: {feels_like}")
        else:
            print("Не удалось найти данные о погоде на странице.")
    else:
        print(f"Ошибка при получении данных: {response.status_code}")


# Вызов функций
download_images_requests()  
asyncio.run(download_images_aiohttp())  
save_images_to_folders()  

get_weather_string_split()  
get_weather_bs4()  
