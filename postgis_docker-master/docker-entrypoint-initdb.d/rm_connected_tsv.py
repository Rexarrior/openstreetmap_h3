import re
import os
import sys


def extract_tsv_filenames_from_file(file_path):
    tsv_filenames = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Используем регулярное выражение для поиска и извлечения имен TSV-файлов
                match = re.search(r'FROM \'(.*?)\' DELIMITER', line)
                if match:
                    tsv_filename = match.group(1)
                    tsv_filenames.append(tsv_filename)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return tsv_filenames


def delete_files(file_list):
    for file_name in file_list:
        try:
            os.remove(file_name)
            print(f"Deleted file: {file_name}")
        except OSError as e:
            print(f"Error deleting file '{file_name}': {str(e)}")

def correct_filename(fname):
    return fname.replace("/input", "./data")

def test():
    folder_path = "./data/sql"
    file_list = os.listdir(folder_path)
    for file in file_list:
        print(f'process {file}')
        fpath = f'{folder_path}/{file}'
        filenames = extract_tsv_filenames_from_file(fpath)
        print(f"get {len(filenames)} filenames")
        filenames = [correct_filename(fname) for fname in filenames]
        delete_files(filenames)

def run(fname):
    print(f"process file {fname}")
    filenames = extract_tsv_filenames_from_file(fname)
    print(f"found {len(filenames)}")
    delete_files(filenames)
    print("process finished")

if __name__ == "__main__":
    # test()
    print(f"Run with args {sys.argv[0]}")
    run(sys.argv[1])


