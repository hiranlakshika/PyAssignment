def read_file(file, column):
    f = open(file, "r")
    lines = f.readlines()
    output = []
    i = 0
    while i < len(lines):
        result = lines[i].split()
        if result[column] != '999.0':
            output.append(result[column])
        i += 1
    f.close()

    return output


degree_sign = u'\N{DEGREE SIGN}'
database_name = "test.db"
