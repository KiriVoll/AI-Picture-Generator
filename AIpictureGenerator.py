import pyperclip
import winsound
import webbrowser
from g4f.client import Client

client = Client()

def choose_model():
    print("Choose image generation model:")
    print("1 - bing (recommended)")
    print("2 - deepai")
    print("3 - flux")
    print("4 - pollinations")
    while True:
        choice = input("Choose model number (1‑4): ").strip()
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

def choose_action():
    print("What to do with the generated link by default?")
    print("1 – copy to clipboard + beep")
    print("2 – open directly in browser       (default)")
    while True:
        choice = input("Choose action number (1‑2) [2]: ").strip()
        if choice == "" or choice == "2":
            return "open"
        elif choice == "1":
            return "copy"
        else:
            print("Incorrect input, try again.")

model = choose_model()
action = choose_action()

print(f"Model set to: {model}")
print(f"Default action set to: {'open in browser' if action == 'open' else 'copy to clipboard'}\n")

while True:
    prompt = input("Enter the prompt (or 'exit' to exit, '/model' to change model): ").strip()

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

        if action == "copy":
            pyperclip.copy(image_url)
            print(f"\nDone!\nLink has been copied to the clipboard:\n{image_url}")
            winsound.MessageBeep()
        else:
            webbrowser.open(image_url)
            print(f"\nDone!\nOpening link in browser:\n{image_url}")

    except Exception as e:
        print(f"❌ Generation error: {e}")
