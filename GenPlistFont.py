#!/usr/local/bin/python3

import os
import sys


def scanFont(path):
    __files = []

    start = "\t<key>UIAppFonts</key>\n\t<array>"
    end = "\t</array>"
    for root, dirs, files in os.walk(path):
        for f in files:
            filename = os.path.join(root, f)
            is_font_support = filename.endswith('ttf')
            if is_font_support:
                file_name = os.path.basename(filename)
                __files.append("\n\t\t<string>{}</string>".format(file_name))

    plist_value = "{}{}\n{}".format(start, "".join(__files), end)
    print(plist_value)


if __name__ == '__main__':
    params = sys.argv
    if len(params) <= 1:
        print("Use: python GenPlistFont.py /path/to/dir")
        exit(1)

    scanFont(params[1])

