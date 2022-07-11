def read_file(file_name):
    file_data = {}
    count = 0
    text_lines = []
    with open(file_name, 'rt', encoding='utf8') as f:
        while f.readable() or count < 1000:
            line = f.readline().strip()
            if line == '':
                break
            text_lines.append(line)
            count += 1
    file_data.update({'file_name': file_name})
    file_data.update({'count_of_rows': count})
    file_data.update({'text_lines': text_lines})
    return file_data


def write_files(file_name, *files):
    sorted_files = sorted(files, key=lambda file: file.get('count_of_rows'))
    with open(file_name, 'wt', encoding='utf8') as write_file:
        for f in sorted_files:
            write_file.write(f.get('file_name'))
            write_file.write('\n')
            write_file.write(str(f.get('count_of_rows')))
            write_file.write('\n')
            for line in f.get('text_lines'):
                write_file.write(line)
                write_file.write('\n')


if __name__ == '__main__':
    file1 = read_file('1.txt')
    file2 = read_file('2.txt')
    write_files('resultFile.txt', file1, file2)
    result_file = read_file('resultFile.txt')
    print(result_file)
