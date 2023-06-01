with open("wuw.txt","r",encoding="utf-8") as file:
    content = file.read(13)
    print(content)
    file.seek(13)  
    print(file.tell())
    content2= file.read()
    print(content2)
