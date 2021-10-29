def White(message):
    return '%s' % (message)


def Red(message):
    return '%s%s%s' % ('\033[0;31m', message, '\033[0m')


def Green(message):
    return '%s%s%s' % ('\033[0;32m', message, '\033[0m')


def BoldRed(message):
    return '%s%s%s' % ('\033[1;31m', message, '\033[0m')


def BoldGreen(message):
    return '%s%s%s' % ('\033[1;32m', message, '\033[0m')


def BoldYellow(message):
    return '%s%s%s' % ('\033[1;33m', message, '\033[0m')


def BoldPurple(message):
    return '%s%s%s' % ('\033[1;35m', message, '\033[0m')


def BlinkRed(message):
    return '\033[5;41m' + message + '\033[0m';


def BlinkGreen(message):
    return '\033[5;42m' + message + '\033[0m';


def BlinkYellow(message):
    return '\033[5;43m' + message + '\033[0m';
