def calculator(a , b):
    sum = a + b
    return sum

result = calculator(2 , 5)
print(result)



def sumrange():
    

    sum = 0
    
    for num in range(2, 12):
        sum += num

        print(sum)

print(sumrange())


def sumtotal():
    total = 0
    for i in range(4, 20):
       total += i

       print(total)

sumtotal()



def fruits_shop():
    fruits = {
            "mango":2.00,
            "orange":5.00,
            "grape":8.50,
            "apple":4.60,
            "cherry":3.50,
            "kiwi":6.70
            }
    fruit_price = 0
    fruit_ordered = []

    for fruit_name,price in fruits.items():
        fruit_price += price
        fruit_ordered.append(fruit_name)

    print(f"the total cost of fruit bought {fruit_price}")
    print(f"the list of fruit bought {fruit_ordered}")


fruits_shop()
