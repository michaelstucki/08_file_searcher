import os
import collections


SearchResult = collections.namedtuple('SearchResult', 'line, file, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry, that location cannot be searched.")
        return

    text = get_search_text_from_user()
    if not text:
        print("Sorry, cannot search for nothing!")
        return

    matches = search_folders(folder, text)
    for match in matches:
        print('--------- MATCH ---------')
        print('file:  {}'.format(match.file))
        print('line:  {}'.format(match.line))
        print('match: {}'.format(match.text.strip()))
        print()


def print_header():
    print('---------------------------------------')
    print('                                       ')
    print('            FILE SEARCH APP')
    print('                                       ')
    print('---------------------------------------')


def get_folder_from_user():
    folder = input('What folder should I search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('For what text should I look [single phrases only]? ')
    return text.lower()


def search_folders(folder, text):
    # all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)
            # matches = search_folders(full_item, text)
            # all_matches.extend(matches)

            # for match in matches:
            #     yield match
            # yield from matches
        else:
            yield from search_file(full_item, text)
            # all_matches.extend(matches)
            # for match in matches:
            #     yield match

    # return all_matches


def search_file(filename, search_text):
    # matches = []
    with open(filename, 'r', encoding='utf-8') as fin:
        line_number = 0
        for line in fin:
            line_number += 1
            if line.lower().find(search_text) >= 0:
                match = SearchResult(
                    line=line_number, file=filename, text=line)
                # matches.append(match)
                yield match

    # return matches


if __name__ == '__main__':
    main()
