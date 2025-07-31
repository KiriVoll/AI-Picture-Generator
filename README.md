# AI Picture Generator
# Script for generating images based on experiments with model selection

A convenient console tool for generating images based on a text description (promt) in Python using the [g4f](https://github.com/xtekky/gpt4free ) library. It supports several models: Bing, DeepAI, Flux and Pollinations.

<img width="1024" height="1024" alt="1024" src="https://github.com/user-attachments/assets/4efbbce6-505e-40fd-bf0b-c4703a066db0" />

---

## Content

* [Functionality](#functionality)
* [Requirements](#requirements)
* [Installation](#installation)
* [Launch and Use](#launch-and-use)
* [Error Handling](#error-handling)
* [Settings and Extensions](#settings-and-extensions)

---

## Functionality

1. **Choosing a generation model**

   * Bing (recommended)
   * DeepAI
   * Flux
   * Pollinations
2. **The main cycle**

   * User input of promt
   * Commands:

     * `exit`, `exit`, `quit` — terminate the script
     * `/model` — change the model without restarting
3. **Result generation and output**

   * API request:

     ```python
     response = client.images.generate(
         model=model,
         prompt=prompt,
         response_format="url"
     )
     image_url = response.data[0].url
     ```
   * Auto-copying of the link to the clipboard (`pyperclip.copy`)
   * Beep on successful generation (`winsound.MessageBeep`)
4. **Error handling**

   * Interception of exceptions and message output:

     ```text
      Generation error: <error text>
     ```

---

## Requirements

* Python 3.7+
* Windows (for `winsound` operation)

### Dependencies

* [`g4f`](https://pypi.org/project/g4f/)
* `pyperclip`
* `winsound` (included in the Windows standard library)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/KiriVoll/AI-Picture-Generator.git
   cd AI-Picture-Generator
   ```
2. Install the dependencies:

   ```bash
   pip install g4f pyperclip
   ```

---

## Launch and Use

1. Run the script with the command:

   ```bash
   python AIpictureGenerator.py
   ```
2. At the first launch, select the generation model (1-4).
3. Enter the promt in the console and press Enter.
4. After generation:

   * The link to the image will be copied to the clipboard.
   * You will hear a beep.
5. To change the model, enter the command `/model`.
6. Use `quit`, `exit` or `выход` to exit.

---

## Error Handling

The script intercepts all exceptions that occur when accessing the API and outputs them in a clear format. This allows you to continue working after an unsuccessful request.

---

## Settings and Extensions

* **Response formats**: add support for `base64` or byte data
* **GUI**: implement a graphical interface with the `tkinter` or `PyQt` libraries
* **Logging**: save the history of requests and responses to a file
* **Parallel queries**: implement batch generation of promts

## ❤️ Support
If you find this useful, feel free to star ⭐ the repo or share your improvements!
