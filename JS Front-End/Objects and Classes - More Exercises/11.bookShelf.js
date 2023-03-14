function bookShelf(input) {
    let shelves = {};
    let books = {};

    for (const line of input) {
        if (line.includes('->')) {
            let [shelfId, genre] = line.split(' -> ');
            if (!shelves.hasOwnProperty(shelfId)) {
                shelves[shelfId] = genre;
                books[genre] = [];
            }
        } else {
            let [title, other] = line.split(': ');
            let [author, bookGenre] = other.split(', ');
            if (books.hasOwnProperty(bookGenre)) {
                books[bookGenre].push({ title, author });
            }
        }
    }

    let sortedGenres = Object.entries(books)
    .sort((bookA, bookB) => {
        let booksACount = bookA[1].length;
        let booksBCount = bookB[1].length;

        return booksBCount - booksACount;
    });

    for (const [genre, booksCollection] of sortedGenres) {
        let shelfId = Object.entries(shelves)
            .find(([id, g]) => g === genre)[0];
        console.log(`${shelfId} ${genre}: ${booksCollection.length}`);
        let sortedBooks = booksCollection.sort((bookA, bookB) => bookA.title.localeCompare(bookB.title));
        for (const { title, author } of sortedBooks) {
            console.log(`--> ${title}: ${author}`);
        }
    }
}
