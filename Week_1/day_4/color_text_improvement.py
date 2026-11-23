# colorama is a module that lets us add color to terminal text
# Modules are bundles of extra features we can import into our programs
# import colorama
from colorama import Back, Fore, Style, init

# autoreset=True means we don't have to manually reset the color after each print
init(autoreset=True)


# --- Foreground (text) colors ---
print(Fore.RED + "This is red text!")
print(Fore.GREEN + "This is green text!")
print(Fore.BLUE + "This is blue text!")


# --- Text styles ---
message = "Python is dope!"
print(Fore.YELLOW + Style.BRIGHT + message)
print(Fore.YELLOW + Style.DIM + message)
print(Fore.YELLOW + Style.NORMAL + message)


# --- Background colors ---
print(Fore.BLACK + Back.YELLOW + "This text has a yellow background!")
print(Fore.WHITE + Back.BLUE + "This text has a blue background!")
print(Fore.BLACK + Back.GREEN + "This text has a green background!")