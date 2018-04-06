"""Simple Colored Text using ANSI Escape Codes.

This module contains functions for writing colored text to consoles supporting
16 ANSI background and foreground colors.

The following colors are available as both foreground and background colors:

    black
    red
    green
    yellow
    blue
    magenta
    cyan
    white
    brightblack
    brightred
    brightgreen
    brightyellow
    brightblue
    brightmagenta
    brightcyan
    brightwhite

"""

from sys import stdout

def color_print(
        *args,
        sep=' ',
        end='\n',
        file=stdout,
        flush=False,
        fg='white',
        bg='black'
):
    """Print colored objects to the text stream file, separated by sep and 
    followed by end. Can safely replace Python's print statement to support ANSI
    colors.

    Args:
        args: objects to print.
        sep: separates objects if there are multiple objects.
        end: final character printed.
        file: text stream to print to.
        flush: forces stream flushing.
        fg: foreground color of output text.
        bg: background color of output text.

    """
    message = ""

    for i, arg in enumerate(args):
        message += str(arg)
        if i < len(args) - 1:
            message += sep
    
    print(color_string(message, fg, bg), end=end, file=file, flush=flush)

def color_string(message, fg='white', bg='black'):
    """Build a printable colored string using ANSI escape codes.
    
    Args:
        message: string representing the text data to color.
        fg: string representing the desired foreground color (see module
            documentation for colors).
        bg: string representing the desired background color (see module 
            documentation for colors).

    Returns:
        string: the original message, colored if specified.

    """
    if fg == 'white' and bg == 'black':
        return message

    return '\x1b[{0};{1}m{2}\x1b[0m'.format(
        color_string.ansi_foreground[fg],
        color_string.ansi_background[bg],
        message
    )

color_string.ansi_foreground = {
    'black' : '30',
    'red' : '31',
    'green' : '32',
    'yellow' : '33',
    'blue' : '34',
    'magenta' : '35',
    'cyan' : '36',
    'white' : '37',
    'brightblack' : '90',
    'brightred' : '91',
    'brightgreen' : '92',
    'brightyellow' : '93',
    'brightblue' : '94',
    'brightmagenta' : '95',
    'brightcyan' : '96',
    'brightwhite' : '97',
}

color_string.ansi_background = {
    'black': '40',
    'red' : '41',
    'green' : '42',
    'yellow' : '43',
    'blue' : '44',
    'magenta' : '45',
    'cyan' : '46',
    'white' : '47',
    'brightblack' : '100',
    'brightred' : '101',
    'brightgreen' : '102',
    'brightyellow' : '103',
    'brightblue' : '104',
    'brightpink' : '105',
    'brightcyan' : '106',
    'brightwhite' : '107'
}

def set_color(fg=None, bg=None):
    """Set the proceeding text colors. Reset colors if no arguments are given.

    Args:
        fg: String representing the desired foreground color of proceeding text.
        bg: string representing the desired background color of proceeding text.

    """
    
    if not (fg or bg):
        print(color_string(""), end="")
        return

    if set_color.first_run:
        print('\x1b[{0};{1}m'.format(color_string.ansi_foreground['white'],
                                     color_string.ansi_background['black']), end="")
        set_color.first_run = False

    if fg and not bg:
        print('\x1b[{0}m'.format(color_string.ansi_foreground[fg]), end="")
    elif bg and not fg:
        print('\x1b[{0}m'.format(color_string.ansi_background[bg]), end="")
    else:
        print('\x1b[{0};{1}m'.format(color_string.ansi_foreground[fg],
                                     color_string.ansi_background[bg]), end="")

set_color.first_run = True
