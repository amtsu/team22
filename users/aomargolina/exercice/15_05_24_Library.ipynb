{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4cefcb38-82cd-4886-890f-7606fb44cf87",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Book:\n",
    "    def __init__(self, name, author, pages, genre):\n",
    "        self.name = name\n",
    "        self.author = author\n",
    "        self.pages = pages\n",
    "        self.genre = genre"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "643c612a-cd54-413b-8b4f-d5dc11741475",
   "metadata": {},
   "outputs": [],
   "source": [
    "class User:\n",
    "    def __init__(self, name: str):\n",
    "        self.name = name\n",
    "        self.user_books: list[Book] = []\n",
    "\n",
    "    def take_book(self, book: Book):\n",
    "        if len(self.user_books) >= 5:\n",
    "            raise ValueError(f'Ошибка! Невозможно добавить книгу. У пользователя {self.name} уже максимальное количество книг книг!')\n",
    "        self.user_books.append(book)\n",
    "        \n",
    "     def retun_book(self, book: Book):\n",
    "         if book not in self.user_books:\n",
    "             raise ValueError(f'Ошибка! Такой книги у пользователя {self.name} такой книнги нет')\n",
    "         self.user_books.remove(book)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d6b88b6-794f-46a1-9663-0fc433f4d8bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Library:\n",
    "    def __init__(self):\n",
    "        self.books = []\n",
    "        self.books_on_hand = []\n",
    "\n",
    "    def total_book(self):\n",
    "        return len(self.books)\n",
    "\n",
    "    def avg_pages(self):\n",
    "        all_pages = []\n",
    "        for book in self.books:\n",
    "            all_pages.append(book.pages) \n",
    "        avg_pages = sum(all_pages) / self.total_book()\n",
    "        return avg_pages\n",
    "    \n",
    "    #def add_book(self, book):\n",
    "        #self.books.append(book)\n",
    "    # по красоте - дописать метод remove\n",
    "\n",
    "    def search_book(self, request: str) -> tuple[tuple]:\n",
    "        \"\"\"функция поиска книг\"\"\"\n",
    "    request = request.lower().strip()\n",
    "    name_list = []\n",
    "    author_list = []\n",
    "    genre_list = []\n",
    "    for book in self.books:\n",
    "        if request in book.name.lower():\n",
    "            name_list.append(book)\n",
    "        if request in book.author.lower():\n",
    "            author_list.append(book)\n",
    "        if request in book.genre.lower():\n",
    "            genre_list.append(book)\n",
    "    if len(name_list) == 0 and len(author_list) == 0 and len(genre_list) == 0:\n",
    "        raise ValueError(f'По вашему запросу \"{requst}\" ничего не найдено!')\n",
    "    return (tuple(name_list), tuple(author_list), tuple(genre_list))\n",
    "\n",
    "    \n",
    "    def give_book(self, user: User, book: Book): \n",
    "        \"\"\"метод выдачи книги из библиотеки пользователю\"\"\"\n",
    "        if book not in self.books:\n",
    "            raise ValueError(f'Ошибка! Такой книги {book.name} нет в библиотеке')\n",
    "        user.take_book(book)\n",
    "        self.books.remove(book)\n",
    "        self.books_on_hand.append((user, book))\n",
    "\n",
    "    def give_back_book(self, user: User, book: Book):\n",
    "        \"\"\"метод забирает книгу у пользователя и возвращает в библиотеку\"\"\"\n",
    "        user.return_book(book)\n",
    "        self.books.append(book)\n",
    "        self.books_on_hand.remove((user, book))\n",
    "        \n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
