speed_limit = int(input('Please enter the speed limit for the road: '))
vehicle_speed = int(input('Please enter the vehicles recorded speed: '))

modified_speed = vehicle_speed - speed_limit


if modified_speed < 10:
    print('The speeding fine is $50.')

elif 6 <= modified_speed <= 20:
    print('The speeding fine is $75.')

elif 21 <= modified_speed <= 40:
    print('The speeding fine is $150.')    

elif 40 <= modified_speed:
    print('The speeding fine is $300.')

else:
    print('There is no fine.')