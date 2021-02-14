def TaxiExpress():
    Customers = input()
    CustomerTime = []
    CustomerTime = Customers.split(', ')
    CustomerTime = [int(i) for i in CustomerTime]
    Taxis = input()
    TaxiTime = []
    TaxiTime = Taxis.split(', ')
    TaxiTime = [int(i) for i in TaxiTime]

    TotalTime = 0
    BadDay = False
    result = ''

    while BadDay is False and TaxiTime and CustomerTime:
        currentTaxi = TaxiTime.pop()
        currentCustomer = CustomerTime.pop(0)

        if currentTaxi >= currentCustomer:
            TotalTime += currentCustomer
        elif currentCustomer > currentTaxi:
            CustomerTime.reverse()
            CustomerTime.append(currentCustomer)
            CustomerTime.reverse()

    if not TaxiTime:
        BadDay = True

    if BadDay is True and CustomerTime:
        result += 'Not all customers were driven to their destinations\n'
        result += 'Customers left: ' + str(CustomerTime).strip('[]')
    else:
        result += 'All customers were driven to their destinations\n'
        result += 'Total time: {0} minutes'.format(TotalTime)

    print(result)


if __name__ == '__main__':
    TaxiExpress()
