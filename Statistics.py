"""
Author: Karl Künnapas
Task description: A program that navigates to the Statistics Estonia main indicators page and
saves the names and numerical values of all main indicators to a file. Then, it asks the user
which indicator they want to know about and outputs it to the console.
"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def print_options():
    """
    Function "print_options" definition
    The function displays on the screen the saved names from the webpage along with their serial numbers.
    """
    for i in range(1, 19):
        print(str(i) + ".", indicator_names[i - 1])


"""Launch Firefox in headless mode."""
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

"""Saving indicator names and their values from Statistics Estonia's homepage."""
browser.get('https://www.stat.ee/en/avasta-statistikat/main-indicators')
webpage_names = browser.find_elements_by_class_name("button__label")  # Names
webpage_indicators = browser.find_elements_by_class_name("indicator-single__value")  # Indicators


"""Writing the numerical values of indicators to a file."""
with open("Indicators.txt", "w", encoding="UTF-8") as f:
    for indicator in webpage_indicators:
        f.write(indicator.text + "\n")

"""Adding indicator names to a list."""
indicator_names = []
for name in webpage_names:
    indicator_names.append(name.text)

browser.close()


"""Reading indicators from the file and adding them line by line to a list without newline characters."""
indicators = []
with open("Indicators.txt") as f:
    for indicator in f:
        indicators.append(indicator.strip("\n"))

"""Displaying all saved main indicator names from the webpage with serial numbers to the user."""
print("Which indicator would you like to display? \nOptions:")
print_options()

"""
Asking the user for an integer, i.e., the serial number of the indicator, and displaying
the desired indicator based on the received response.
"""
choice = input("Enter the serial number (as an integer): ")
while True:
    try:
        choice = int(choice)
        if choice < 1:
            raise IndexError
        else:
            print("According to Statistics Estonia, the", indicator_names[choice - 1].lower(), "is",
                  indicators[choice - 1] + ".")
            choice = input("Enter the serial number (as an integer): ")

    except IndexError:
        choice = input("Please enter a valid serial number: ")

    except ValueError:
        choice = input("Please enter a valid serial number: ")
