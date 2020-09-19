products = [('Arroz', 20), ('Feijao', 10), ('Suco', 5), ('Sorvete', 2)]


def list_products():
    ind = 0
    for i in products:
        ind = ind+1
        index = (len(products) - (len(products)-ind))
        print(index, '-', i[0], 'R$', i[1])


def get_products():
    list_products()
    another_product = 'sim'
    cart_total = 0
    while(another_product == 'sim'):
        product = input('Digite o código do seu produto (1,2,3...): ')
        product_value = products[int(product)][1]
        cart_total = cart_total + product_value
        print('Seu total é: ', cart_total)
        another_product = input(
            'Gostaria de adicionar outro produto? (sim / não) : ')


get_products()
