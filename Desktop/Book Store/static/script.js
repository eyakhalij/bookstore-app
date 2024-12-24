document.addEventListener("DOMContentLoaded", () => {
    const booksDiv = document.getElementById("books");
    const books = [
        { id: 1, title: "Book One", author: "Author One" },
        { id: 2, title: "Book Two", author: "Author Two" },
    ];

    books.forEach(book => {
        const bookElement = document.createElement("div");
        bookElement.textContent = `${book.title} by ${book.author}`;
        booksDiv.appendChild(bookElement);
    });
});
