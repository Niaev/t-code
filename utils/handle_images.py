from PIL import Image

img_folder = 'imgs/'
abc_img = img_folder + 'alphabet/'
other_img = img_folder + 'other/'

def get_image(char: str) -> 'PIL.Image.Image':
    """Get correspondent image object of the given single char

    Arguments:
        char {str} -- Single character

    Returns:
        {PIL.Image.Image} -- Image of the given char
    """

    ch = char
    if ch == '.':
        ch = 'period'
    elif ch == ' ':
        ch = 'space'

    img_file = abc_img + ch + '.png'
    img = Image.open(img_file)

    return img

def border_image() -> 'PIL.Image.Image':
    """Get image object of the border"""
    return Image.open(other_img + 'border.png')