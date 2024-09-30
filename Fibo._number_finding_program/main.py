def fibo():
    import turtle
    import random
    first_number = 1
    second_number = 1

    given_number = int(input(
        'Which position of fibo number do you wanna see?\nI will list all the fibo numbers end of your desired'
        ' position.'
        '\nThe last number of the list will be your.\n> '))

    if given_number <= 2:
        fibo_number = 1
    else:
        i = 3
        ls = [1, 1, ]
        while i <= given_number:
            v = 180
            i += 1
            first_number, second_number = second_number, first_number + second_number
            fibo_number = second_number
            ls += [fibo_number]

            co = ['yellow', 'red', 'blue', 'white', 'green']
            for num in ls:
                color = random.choice(co)

            turtle.bgcolor('black')
            turtle.color("white")
            turtle.pensize(2)
            turtle.fillcolor(color)

            turtle.begin_fill()
            turtle.speed(0)
            turtle.circle(fibo_number, v)

            turtle.end_fill()

        print(ls)
        turtle.done()

fibo()