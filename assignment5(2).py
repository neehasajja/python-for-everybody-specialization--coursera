largest = None
smallest = None
while True:

        try:

            num = int(inp)

        except:

            if inp == 'done' or inp == 'Done' or inp == 'DONE' :

                break

            else:

                print('Invalid input')

                continue

        if smallest is None:

            smallest = num

            largest = num

        elif num < smallest :

            smallest = num

        elif num > largest :

            largest = num



    print('Maximum is',largest)

    print('Minimum is',smallest)
