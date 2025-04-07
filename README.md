# Dice-Tester-Python

## About
This is a simple Python script which tests if dice are fair or biased, using the Chi-Squared test: https://en.wikipedia.org/wiki/Chi-squared_test

This script is forked from mindbane's [Dice-Tester](https://github.com/mindbane/Dice-Tester/). Functionally, it is almost identical to mindbane's script, but written in Python instead of Visual Basic. I wanted a Python version of the script because I use Linux, and Visual Basic scripts only work on Windows as far as I know.

I used Google Gemini to translate the original script into Python. The underlying maths and the way it works is identical to mindbane's script, but I made a few changes:
- Made the script display how many input rolls you have entered so far. I found that entering 100+ numbers into the terminal with no indication of how many more I had to go was a little frustrating, and wanted to see my progress.
- Dice numbers start from 1 instead of 0, to make things less confusing (ie. if you have a 12 sided dice, "12" is a valid roll, and "0" is not)
- Updated some of the prompts to be a little clearer
- Added basic handling of invalid input
- Tidied up and Python-ified the code (Gemini translated it without any issues, but the output code was ugly and not very Pythonic)

## How to Use
To run the script, first set up a Python virtual environment and install the `numpy` library.

**Windows (command prompt):**
```
python3 -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```
*(I have never used Python virtual environments in Windows without WSL so please let me know if the commands above don't work)*

**Mac / Linux (Bash / zsh):**
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Once you have activated the virtual environment and installed `numpy`, you should be able to run the Dice Tester script in your terminal with the command
```
python3 dice_tester.py
```

The script will walk you through the steps to test your dice and do the maths for you.

Note that if you close and re-open your terminal, you will have to activate the virtual environment again before running the script (`venv\Scripts\activate.bat` or `source venv/bin/activate` depending on your OS)
