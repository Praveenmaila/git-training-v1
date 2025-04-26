file_path = "Create Files.py"
new_file = open(file_path, "w")

new_file.write("Hello, Python!")

new_file.close()

with open(file_path, "w" ) as new_file:
    new_file.write("hello python world !")

    file_path = "existing_file.txt"

    with open(file_path, "a") as existing_file: