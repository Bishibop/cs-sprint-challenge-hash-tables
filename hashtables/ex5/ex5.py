'''
Take each file and split it to get the file name
Key that file name into a hash with the full path in a list as the value.
If that file name already exists in the hash, append the file name to the list.

Take each query and concat the lists of paths stored as values in the hash.
'''


def finder(files, queries):

    file_to_paths = {}

    for file_path in files:
        file_name = file_path.split('/')[-1]
        if file_name in file_to_paths:
            file_to_paths[file_name].append(file_path)
        else:
            file_to_paths[file_name] = [file_path]

    result = []
    for query in queries:
        if query in file_to_paths:
            result.extend(file_to_paths[query])

    return result


if __name__ == "__main__":
    files = ['/bin/foo', '/bin/bar', '/usr/bin/baz']
    queries = ["foo", "qux", "baz"]
    print(finder(files, queries))
