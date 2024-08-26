

### <h1> Dice Roll Simulation Tool</h1>

## Overview
This Python script simulates rolling a dice using the `random` and `colorama` libraries. The user is presented with a simple menu allowing them to roll a dice or exit the program. The results are displayed in color for enhanced visual feedback. The script includes error handling to manage invalid inputs gracefully.

## Features
- **Roll Dice:** Simulates rolling a standard 6-sided dice.
- **Colorful Output:** Uses `colorama` to provide colored terminal output for better user experience.
- **Error Handling:** Handles invalid inputs with informative error messages.
- **Continuous Interaction:** Runs in a loop until the user chooses to exit.


![GitHub repo size](https://img.shields.io/github/repo-size/nishuR31/Dicey_dice)

<div style="display: inline-flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 20px;">
  <img src="https://img.shields.io/badge/HELLO-CODERS-black" alt="Custom Badge">
  <img src="https://img.shields.io/github/issues-pr-closed/nishuR31/nishuR31?color=blueviolet" alt="Issue Count">
  <img src="https://img.shields.io/github/issues/nishuR31/nishuR31?color=blueviolet" alt="Issue Count"></div>
<br>
<div align="centre">
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" width="60"/> </a></div>


## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nishuR31/Dicey_dice.git
   cd Dicey_dice
   ```


2. **Install Dependencies:**
   Ensure you have Python installed, then install the required package:
   ```bash
   pip install colorama
   ```
   or
   
   ```bash
   pip install -r requirements.txt
   ```



## Usage

1. **Run the Script:**
   ```bash
   python dice.py
   ```
   ```bash
   python -u "dice.py"
   ```

2. **Menu Options:**
   - **1:** Roll the dice.
   - **0:** Exit the program.

3. **Example Interaction:**

   ```plaintext
   1:roll the dice
   0:exit
   
   what you want to do: 1
   
   Rolled number: 4

   what you want to do: 0
   
   Exiting.
   ```

## Script Breakdown
- **Imports:**
  - `random` is used to generate random numbers simulating the dice roll.
  - `colorama` is used to add color to terminal output.

- **Main Loop:**
  - Displays a menu with options to roll the dice or exit.
  - Takes user input and processes it.
  - Rolls the dice and displays the result if the user chooses to roll.
  - Exits the program if the user chooses to exit.
  - Handles invalid input with appropriate error messages.

- **Error Handling:**
  - Catches and reports errors related to invalid input.

## Error Handling
- **Invalid Input:**
  - If the user enters anything other than "1" or "0", an error message is displayed.
  - The script handles exceptions and provides a user-friendly error message.


[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=nishuR31&repo=Dicey_dice&show_owner=true&theme=midnight-purple)](https://github.com/nishuR31)


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Feel free to submit issues, feature requests, and pull requests.

## Contact
For questions or suggestions, please contact [nishanrajak7679@gmail.com](mailto:nishanrajak7679@gmail.com)  or [GitHub](https://github.com/nishuR31/)

