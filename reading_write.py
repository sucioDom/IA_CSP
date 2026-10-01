#IA, reading_writing

with open('practice.txt', "r") as file:
      content = file.read()
      print(content)
      print(content.upper())
      word = content.find("Arredondo")
      leingth = len("Arredondo")
      content += "Treyson!"
      file.write(content)
      print(content[word:word+leingth])

with open("practice.txt", "w") as  file:
    file.write("Hello")
      