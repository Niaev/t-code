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

def matrix_to_image(l: list) -> 'PIL.Image.Image':
    """Get text matrix and transform it to encoded image

    Arguments:
        l {list} -- Bidimentional array with zeros and single char 
                    strings

    Returns:
        PIL.Image.Image: Image that represents the encoded text in
                         T Code :)
    """

    h = len(l) * 16
    w = len(l[0]) * 16

    img = Image.new('RGBA', (w, h), 'WHITE')

    border_img = border_image()

    x_offset = 0
    y_offset = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            oc = l[i][j]
            if oc == 0:
                x_offset += 16
                continue
                
            c = oc.lower()

            char_img = get_image(c)
            img.paste(char_img, (x_offset, y_offset))

            if oc == c.upper() and oc != ' ' and oc != '.':
                img.paste(border_img, (x_offset, y_offset), border_img)

            x_offset += 16
        
        x_offset = 0
        y_offset += 16

    return img

if __name__ == '__main__':
    from utils.handle_text import clear_text
    from utils.handle_matrix import get_text_array

    t = input('Text: ')
    t = clear_text(t)
    l = get_text_array(t)
    img = matrix_to_image(l)
    img.save('Test.png')