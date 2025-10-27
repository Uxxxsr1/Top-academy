book = {'name': 'war and peace', 'author': 'Tolstoy', 'Printing_house': 'Moscow'}
book['yearPriting'] = 1868

def bookdata(**book_data):
    print(book_data)

bookdata(name=book['name'], author=book['author'], priting_house=book['Printing_house'])