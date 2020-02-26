#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

user_input = form.getvalue("fcolor")

print("""
<h1></h1>
""")
with open("cgi-bin/color_archive.txt", "r") as reader:

    if user_input.title() in reader.read():
        print("<h1>{} is a color!</h1>".format(user_input))
    else:
        print("<h1>{} is NOT a color!</h1>".format(user_input))
