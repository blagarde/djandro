from django.utils.termcolors import PALETTES

palette = PALETTES['dark']
COLOR_MAP = {
    'black': '000000',
    'red': 'ff0000',
    'green': '00ff00',
    'blue': '0000ff',
    'cyan': '00ffff',
    'magenta': 'ff00ff',
    'yellow': 'ffff00',
    'white': 'ffffff'
}

STYLE_MAP = {
    'bold': 'b',
    'italic': 'i'
}

def colorize(msg, style):
    style_dct = palette[style]
    color = style_dct.get('fg', None)
    if color is not None:
        msg = '[color=#' + COLOR_MAP[color] + ']' + msg + '[/color]'
    opts = style_dct.get('opts', [])
    for o in opts:
        msg = '[' + STYLE_MAP[o] + ']' + msg + '[/' + STYLE_MAP[o] + ']'
    return msg


def add_markup(msg, args):
    # Utilize terminal colors, if available
    if args[1][0] == '2':
        # Put 2XX first, since it should be the common case
        msg = colorize(msg, 'HTTP_SUCCESS')
    elif args[1][0] == '1':
        msg = colorize(msg, 'HTTP_INFO')
    elif args[1] == '304':
        msg = colorize(msg, 'HTTP_NOT_MODIFIED')
    elif args[1][0] == '3':
        msg = colorize(msg, 'HTTP_REDIRECT')
    elif args[1] == '404':
        msg = colorize(msg, 'HTTP_NOT_FOUND')
    elif args[1][0] == '4':
        msg = colorize(msg, 'HTTP_BAD_REQUEST')
    else:
        # Any 5XX, or any other response
        msg = colorize(msg, 'HTTP_SERVER_ERROR')
    return msg
