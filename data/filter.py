def filter_func(char: str) -> bool:
    print(char, end=': ')
    if char.isalpha() or char == ' ' or char == '\n':
        print('True')
        return True
    print('False')
    return False

def main():
    with open('ilo-jan/data/corpus.txt', 'r') as f:
        filtered = ''.join(filter(filter_func, list(f.read())))
        better_filtered = list()
        for i in range(len(filtered.split('\n'))):
            better_filtered.append(f'{filtered.split('\n')[i]} \n')

    with open('ilo-jan/data/filtered_corpus.txt', 'w') as f:
        f.writelines(better_filtered)

if __name__ == "__main__":
    main()
