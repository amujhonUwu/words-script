# Automation of Typing Words

This project uses Python and the `pyautogui` library to automate typing a list of words. The script is designed to type a series of words (the numbers from 1 to 30 in Spanish) with a slight delay between each letter and then press "Enter" after each word.

## Requirements

- Python 3.x
- The `pyautogui` library

You can install the `pyautogui` library using `pip`:

```bash
pip install pyautogui
```

# How to Use
1. Make sure the required dependencies are installed.
2. Run the Python script with or without the shutdown option.
3. After a 3-second delay (to allow you to select the desired window), the script will begin typing each word in the list.
4. The script will press "Enter" after typing each word.

# Args
Use no arguments to run only on pc.

-cell: This will execute the script to a cellphone. But, you have to:
  1. Have an app like "Bluestacks" or a duplicated screen of your mobile
  2. The cell phone screen should be in the upper right corner of your computer screen
     
-all: This will run both, first the PC and then the cell phone


## Optional Shutdown
You can now run the script with an optional argument `-sd` to automatically shut down the computer after it finishes running. Use it as follows:

```bash
python main.py -sd
```

# Notes
- The sleep time (time.sleep) can be adjusted as needed to match your preferred typing speed. But, by default:
    - Pc:
      DEFAULT_TIEMPO_ENTRE_PALABRA = 3
      DEFAULT_TIEMPO_ENTRE_LETRA = 0.08
    - Cellphone:
      DEFAULT_TIEMPO_ENTRE_PALABRA = 4
      DEFAULT_TIEMPO_ENTRE_LETRA = 0.08
      (Plus other 1.7 seconds to click the screen)
- Ensure the window where you want the words to be typed is active when the script starts running.
- The shutdown feature is only compatible with Windows.

# Warning
Be careful when using pyautogui, as it automates keyboard inputs and can interfere with other applications if not used properly.

# Contributions
Contributions are welcome. If you find a bug or have suggestions for improvement, feel free to create an issue or a pull request.
