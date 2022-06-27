shelf_with_books = input().split('&')

while True:
    command = input()

    if command == 'Done':
        break

    command = command.split(' | ')
    book_name = command[1]

    if 'Add Book' == command[0]:
        if book_name not in shelf_with_books:
            shelf_with_books.insert(0, book_name)

    elif 'Take Book' == command[0]:
        if book_name in shelf_with_books:
            shelf_with_books.remove(book_name)

    elif 'Swap Books' == command[0]:
        if command[1] in shelf_with_books and command[2] in shelf_with_books:
            index1 = shelf_with_books.index(command[1])
            index2 = shelf_with_books.index(command[2])
            book_1 = command[1]
            shelf_with_books[index1] = shelf_with_books[index2]
            shelf_with_books.pop(index2)
            shelf_with_books.insert(index2, book_1)

    elif 'Insert Book' == command[0]:
        if book_name not in shelf_with_books:
            shelf_with_books.append(book_name)

    elif 'Check Book' == command[0]:
        index = int(command[1])
        if 0 <= index < len(shelf_with_books):
            print(shelf_with_books[index])

print(', '.join(shelf_with_books))
