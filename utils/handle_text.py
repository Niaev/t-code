import re

def transform_periods(t: str) -> str:
    """Transform '?' and '!' in periods ('.').
    
    Arguments:
        t {str} -- User input text

    Returns:
        {str} -- Processed text
    """
    return re.sub(r'[!?]', '.', t)

def transform_numbers(t: str):
    """Transform digits in numbers in words.

    Arguments:
        t {str} -- User input text

    Returns:
        {str} -- Processed text
    """

    # Numbers dictionary
    d = {
        '0': 'zero ',
        '1': 'one ',
        '2': 'two ',
        '3': 'three ',
        '4': 'four ',
        '5': 'five ',
        '6': 'six ',
        '7': 'seven ',
        '8': 'eight ',
        '9': 'nine '
    }
    # List of number in words
    l_nstr = [d[i] for i in d]

    # Replace number by number in words
    for i in d:
        t = t.replace(i, d[i])

    # If there is any number in words that is followed by two spaces 
    # ('  '), remove one space
    for n in l_nstr:
        wrong = n + ' '
        if wrong in t:
            t = t.replace(wrong, n)

    return t

def remove_useless_chars(t: str) -> str:
    """Remove all characters that aren't in the T Code alphabet, which 
    are the common alphabet, period and space.

    This function assumes that the inputted text is already in lower 
    case.

    Arguments:
        t {str} -- User input text

    Returns:
        {str} -- Processed text
    """
    return re.sub(r'[^a-z. ]', '', t)

def clear_text(t: str) -> str:
    """Transform the input text in a T Code friendly text.

    This task includes transforming all characters to lower case,
    transforming periods with 'transform_periods', transforming
    numbers with 'transform_numbers' and removing useless characters
    with 'remove_useless_chars'.

    Arguments:
        t {str} -- User input text

    Returns:
        {str} -- Processed text
    """

    t = t.lower()
    t = transform_periods(t)
    t = transform_numbers(t)
    t = remove_useless_chars(t)
    return t

if __name__ == '__main__':
    text = input('Input your text: ')
    print(clear_text(text))