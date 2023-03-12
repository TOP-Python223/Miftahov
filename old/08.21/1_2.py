from shutil import get_terminal_size

def important_message(text):
    col = get_terminal_size().columns - 3
    print(f"#{col * '='}#")
    print(f"#{col * ' '}#")
    if len(text) >= col:
        line_break = len(text) // col + 1
        for _ in range(line_break):
            print(f"#  {text[:col - 4].ljust(col - 2)}#")
            text = text[col - 4:]
    else:
        print(f"#  {text.ljust(col - 2)}#")
    print(f"#{col * ' '}#")
    print(f"#{col * '='}#")
    
    

text = "Now you're looking at the very important message from the team of the developers of this miraculous script Now you're looking at the very important message from the team of the developers of this miraculous script"

res = important_message(text)
