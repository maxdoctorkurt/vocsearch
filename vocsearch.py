import re
import pprint
from beautifultable import BeautifulTable

langs = {
"ru" : open("ru.xml", "r", encoding="utf-8"),
"uk" : open("uk.xml", "r", encoding="utf-8"),
"en" : open("en.xml", "r", encoding="utf-8")
}

help_msg = '"C" - переведено, но закомментированно; "+" - переведено; " " - не переведено'

lang_names = {}
names_set = set()
commented_names = {}

for lang in langs:
    temp = []
    commented = []
    for line in langs[lang].readlines():
        result = re.search(r'name="(\w+)"',line)
        if result != None:
            name = result.group(1)
            temp.append(name)
            names_set.add(name)

            if "<!--" in line:
                commented.append(name)
    commented_names[lang] = commented

    lang_names[lang] = temp

hat = ['*']

hat.extend(lang_names.keys())

table = BeautifulTable()

table.append_row(hat)

for name in sorted(names_set):

    row = [name]

    for lang in hat:
        if lang != '*':

            if name in commented_names[lang]:
                row.append("C")
            elif name in lang_names[lang]:
                row.append("+")
            else:
                row.append(" ")

    table.append_row(row)

print(help_msg)
print(table)
print(help_msg)
