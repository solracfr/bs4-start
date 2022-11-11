from bs4 import BeautifulSoup
import lxml  # used if html parsing doesn't work

# needs utf-8 encoding to access this file, likely cause of
# the heart emoji
with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")  # pass in contents of website and the kind of parser to use
# print(soup.title)  # gets full html line
# print(soup.title.name)  # gets just the html tag title
# print(soup.title.string)  # gets the string inside the html tag
#
# print(soup.a)  # prints the first <a> tag seen. works the same way with all other tags
#
# print(soup)  # prints the whole html file in one line
# print(soup.prettify())  # prints the whole html file with correct indentation
