# Automation of Typing Words

This project uses Python and the `pyautogui` library to automate typing a list of words... for nothing specifically. The code is designed to type a series of words (the numbers from 1 to 30 in spansih) with a slight delay between each letter and then press "Enter" after each word.

## Requirements

- Python 3.x
- The `pyautogui` library

You can install the `pyautogui` library using `pip`:

```bash
pip install pyautogui
```

# How to Use
1. Make sure the required dependencies are installed.
2. Run the Python script.
3. After a 3-second delay (to allow you to select the desired window), the script will begin typing each word in the lista.
4. The script will press "Enter" after typing each word.

# Notes

The sleep time (time.sleep) can be adjusted as needed to match your preferred typing speed.
Make sure the window where you want the words to be typed is active when the script starts running.

# Warning
Be careful when using pyautogui, as it automates keyboard inputs and can interfere with other applications if not used properly.

# Contributions
Contributions are welcome. If you find a bug or have suggestions for improvement, feel free to create an issue or a pull request.