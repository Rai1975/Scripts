def read_file():
    lines = []
    with open(r'C:\Users\User\projects\Scripts\Python\files\cover_letter_input.txt', 'r+') as f:
        lines = f.readlines()

    return lines

def replace_titles(company_name, position_title, lines):
    new_lines = []

    for line in lines:
        new_line = line
        new_line = line.replace('COMPANY_NAME', company_name)
        new_line = line.replace('POSITION_NAME', position_title)

        new_lines.append(new_line)

    return new_lines

def write_to_file(lines):
    with open(r'C:\Users\User\projects\Scripts\Python\files\cover_letter_output.txt', 'w+') as f:
        f.writelines(lines)


if __name__=="__main__":
    lines = read_file()

    new_lines = replace_titles('Idaho National Lab', 'Soft Engineer', lines)

    write_to_file(new_lines)

