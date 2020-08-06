from search_engine import SearchEngine


def main():
    print("Building SearchEngine")
    engine = SearchEngine()

    answer = 'y'
    while answer == 'y':
        term = input('Enter Search Term:')
        ranking = engine.search(term)
        print("Displaying results for " + "'" + term + "':")
        if ranking is None:
            print("No results")
        rank = 1
        for doc in ranking:
            print('    ' + str(rank) + '. ' + doc)
            rank += 1
        print()
        answer = ''
        while not (answer == 'y' or answer == 'n'):
            answer = input('Would you like to search another term (y/n) ')


if __name__ == '__main__':
    main()
