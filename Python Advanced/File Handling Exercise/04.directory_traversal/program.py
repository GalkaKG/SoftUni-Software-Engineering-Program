from os import listdir, path


def traverse_dir(current_path, files_extensions):
    for file in listdir(current_path):
        if path.isdir(path.join(current_path, file)):
            traverse_dir(path.join(current_path, file), files_extensions)
        else:
            extension = file.split('.')[-1]
            if extension not in files_extensions:
                files_extensions[extension] = []
            files_extensions[extension].append(file)


files_extensions = {}
traverse_dir('.', files_extensions)

for extension, files in sorted(files_extensions.items(), key=lambda x: x[0]):
    report = open('report.txt', 'a')
    report.write(f'.{extension}\n')
    print(f'.{extension}')
    for file in sorted(files):
        report.write(f'--- {file}\n')
        print(f'--- {file}')
    report.close()
