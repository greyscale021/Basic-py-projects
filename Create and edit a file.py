employee_file = open("index.html", "r+")
employee_file.write("<html><body><h1>Hello World!</h1>")
print(employee_file.read())
employee_file.close()
