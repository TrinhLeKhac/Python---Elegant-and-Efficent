import csv


def is_good_char(c):
    return ord(c) <= 127


def clean_str(s):
    return ''.join(filter(is_good_char, s))


def main():
    # print(os.path.curdir)
    with (
        open('features/advanced/remove_unicode_character/names.csv', newline='', encoding='utf-8') as dirty,
        open('features/advanced/remove_unicode_character/name_cleaned.csv', 'w', newline='') as clean
    ):
        reader = csv.reader(dirty)
        writer = csv.writer(clean)
        for row in reader:
            print(row)
            writer.writerow(map(clean_str, row))


if __name__ == '__main__':
    main()
