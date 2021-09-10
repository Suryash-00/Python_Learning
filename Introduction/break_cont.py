cars= ['ok', 'ok', 'ok', 'faulty', 'ok']
'''
for status in cars:
    if status== 'faulty':
        print("Stopping the production line")
        break
    print(f"This car is {status}")
'''    
for status in cars:
    if status== 'faulty':
        print("Faulty car found, skipping...!")
        continue
    print(f"This car is {status}")
    print("Shipping new car to the customer")