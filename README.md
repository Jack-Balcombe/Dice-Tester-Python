# Dice-Tester-Python

## About
This is a simple Python script which tests if dice are fair or biased, using the Chi-Squared test: https://en.wikipedia.org/wiki/Chi-squared_test

This script is forked from mindbane's [Dice-Tester](https://github.com/mindbane/Dice-Tester/). Functionally, it is almost identical to mindbane's script, but written in Python instead of Visual Basic. I wanted a Python version of the script because I use Linux, and Visual Basic scripts only work on Windows as far as I know.

I translated the original script into Python, with the help of Google Gemini. The underlying maths and the way it works is identical to mindbane's script, but I made a few changes:
- Made the script display how many input rolls you have entered so far. I found that entering 100+ numbers into the terminal with no indication of how many more I had to go was a little frustrating, and wanted to see my progress.
- Dice numbers start from 1 instead of 0, to make things less confusing (ie. if you have a 12 sided dice, "12" is a valid roll, and "0" is not)
- Updated some of the prompts to be a little clearer
- Added basic handling of invalid input
- Tidied up and Python-ified the code *(Gemini translated it without any issues, but the output code had bad style and was not very Pythonic. Gemini also made use of the `numpy` library, which was unnecessary for such a simple script. By using default Python features instead of `numpy`, I made the script work without having to set up a virtual environment or install additional libraries first)*

## How to Use
To run the Dice Tester script, enter the command
```python3 dice_tester.py```
in your terminal.

If the file permissions of `dice_tester.py` allow you to execute the file as a program, you can instead use
```python3 dice_tester.py```
*(On Mac and Linux, to change the file permissions of `dice_tester.py` and allow it to be executed directly, use the command `chmod +x dice_tester.py`)*

The script will walk you through the steps to test your dice and do the maths for you.
