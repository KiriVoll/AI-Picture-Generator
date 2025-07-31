import pyperclip
import winsound
from g4f.client import Client

client = Client()

def choose_model():
    print("Выберите модель генерации картинки:")
    print("1 - bing (рекомендуется)")
    print("2 - deepai")
    print("3 - flux")
    print("4 - pollinations")
    while True:
        choice = input("Введите номер модели (1-4): ").strip()
        if choice == "1":
            return "bing"
        elif choice == "2":
            return "deepai"
        elif choice == "3":
            return "flux"
        elif choice == "4":
            return "pollinations"
        else:
            print("Некорректный ввод, попробуйте снова.")

model = choose_model()

while True:
    prompt = input("\nВведите промт (или 'exit' для выхода, '/model' для смены модели): ").strip()

    if prompt.lower() in ["выход", "exit", "quit"]:
        print("Выход из программы.")
        break

    if prompt.lower() == "/model":
        model = choose_model()
        print(f"Модель изменена на: {model}")
        continue

    try:
        response = client.images.generate(
            model=model,
            prompt=prompt,
            response_format="url"
        )
        image_url = response.data[0].url

        pyperclip.copy(image_url)
        print(f"\nГотово!\nСсылка скопирована в буфер обмена:\n{image_url}")

        winsound.MessageBeep()

    except Exception as e:
        print(f"❌ Ошибка генерации: {e}")
