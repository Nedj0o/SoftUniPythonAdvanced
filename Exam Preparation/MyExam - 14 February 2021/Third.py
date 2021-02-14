def stock_availability(flavourslist, sellordelivery, *args):
    flavourslist = list(flavourslist)

    toaddlist = []
    if args:
        for i in range(len(args)):
            toaddlist.append(args[i])

    if sellordelivery == 'sell' and args and str(args[0]).isnumeric():#if number
        for i in range(int(args[0])):
            if flavourslist:
                flavourslist.pop(0)
    elif sellordelivery == 'sell' and args:
        for i in range(len(args)):
            flavourslist = list(filter(args[i].__ne__, flavourslist))
    elif sellordelivery == 'sell' and not args:#if no args
        if flavourslist:
            flavourslist.pop(0)
    elif sellordelivery == 'delivery' and args:
        for i in range(len(toaddlist)):
            flavourslist.append(toaddlist[i])


    return flavourslist


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
