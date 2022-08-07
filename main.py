import sys
import textwrap

Title = "The Bee Movie"
Author = "Simon J. Smith, Steve Hickner"
Player = "@p"

with open("TextToConvert.txt", "r") as text:
    read_text = text.read()
    lines = textwrap.wrap(read_text, 19)
    with open("book.txt", "w") as book:
        book.write(f"/give {Player} written_book" + "{pages:[")

        FirstTime = True
        Page = []
        for line in range(len(lines)):
            Page.append(lines[line])
            summ = line % 14
            if summ == 0:
                print(Page)
                if FirstTime is True:
                    FirstTime = False
                    breakpnt = ""
                else:
                    breakpnt = ","
                book.write(breakpnt + "'{\"text\":\"")
                for x in range(len(Page)):
                    book.write(Page[x].replace("\n", "").replace("\"", "~").replace("   ", " ").replace("  ", " ").replace("'", "").strip() + " ")
                book.write("\"}'")
                Page.clear()
        book.write(f"],title:\"{Title}\",author:\"{Author}\"" + "}")
