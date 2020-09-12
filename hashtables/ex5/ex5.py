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
