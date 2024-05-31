def test_function(*num):
        a = input(' Enter integer :')
        print(f'Hello, {a}')
        def inner_function(*arg):
            for i in arg:
                b = 1000 + int(a) + int(i)
            print("Я в области видимости функции test_function")
            print(b, 'inner')
            def low_function(*low):
                nonlocal a
                c = int(a) * b
                print(a, 'Low', b, c)
                a = 654
                print(a, 'Без nonlocal выдает ошибку')
            low_function()
        inner_function(10)
test_function()

# inner_function()
