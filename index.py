#!venv/bin/python3

# General Imports
import sys
from datetime import datetime

# Project Imports
from utils.handle_text import clear_text
from utils.handle_matrix import get_text_array
from utils.handle_images import matrix_to_image

def handle_options() -> tuple[str, int, str]:
    """Manage options given from 

    Returns:
        tuple[str, int, str]: _description_
    """

    options = sys.argv
    t = ''
    if len(options) == 1:
        print('[-] You need to provide a text to be encoded!')
        print('[-] Shutting down algorithm')
        sys.exit()
    elif len(options) > 1:
        t = options[1]
        print('[+] Got user given text:')
        print(f'    "{t}"')
    
    save = 0
    if len(options) >= 3:
        if options[2] == 'save': 
            save = 1
    
    outname = datetime.now().strftime('%Y%m%d%H%M%S%f')
    if len(options) == 4:
        if save:
            outname = options[3]
        else:
            print('[+] Ignoring useless given options')

    if save:
        print('[+] Going to save the output to file:')
        print(f'    {outname}\n')
    else:
        print('[+] Going to show image at the end\n')

    return t, save, outname

if __name__ == '__main__':
    print(sys.argv)
    print()

    text, save, output_file = handle_options()

    print('[+] Processing text')
    text = clear_text(text)
    print('[+] Processed text:')
    print(f'    "{text}"')

    print('[+] Generating matrix')
    matrix = get_text_array(text)
    
    print('[+] Generating image')
    img = matrix_to_image(matrix)

    if not save:
        img.show()
        print('\n[+] Shutting down algorithm')
        sys.exit()
    
    img.save(f'{output_file}.png')
    print('[+] Image saved')
    print('\n[+] Shutting down algorithm')
    sys.exit()