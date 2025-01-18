stations = {'UET':30, 'Sultan Pura':40, 'Railway Station':50}

def ticket_counter():
    print('Welcome to the Orange line metro station!')
    name_passenger = input('Please enter your name: ')
    print(f'Hi, {name_passenger}, Select stations from the list below:')
    for index, (key, value) in enumerate(stations.items(), start=1):
        print(f'{index}. {key} Rs.{value}')
    



ticket_counter()