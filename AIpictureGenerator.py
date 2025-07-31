import pyperclip
import winsound
from g4f.client import Client

client = Client()

def choose_model():
    print("Choose image generation model:")
    print("1 - bing (recommended)")
    print("2 - deepai")
    print("3 - flux")
    print("4 - pollinations")
    while True:
        choice = input("Choose model number (1-4): ").strip()
        if choice == "1":
            return "bing"
        elif choice == "2":
            return "deepai"
        elif choice == "3":
            return "flux"
        elif choice == "4":
            return "pollinations"
        else:
            print("Incorrect input, try again.")

model = choose_model()

while True:
    prompt = input("\nEnter the promt (or 'exit' to exit, '/model' to change model): ").strip()

    if prompt.lower() in ["выход", "exit", "quit"]:
        print("Exiting the program.")
        break

    if prompt.lower() == "/model":
        model = choose_model()
        print(f"The model has been changed to: {model}")
        continue

    try:
        response = client.images.generate(
            model=model,
            prompt=prompt,
            response_format="url"
        )
        image_url = response.data[0].url

        pyperclip.copy(image_url)
        print(f"\nDone!\nLink has been copied to the clipboard:\n{image_url}")

        winsound.MessageBeep()

    except Exception as e:
        print(f"❌ Generation error: {e}")
