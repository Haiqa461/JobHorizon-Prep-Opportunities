stations = {'UET':30, 'Sultan Pura':40, 'Railway Station':50}

def ticket_counter():
    print('Welcome to the Orange line metro station!')
    name_passenger = input('Please enter your name: ')
    print(f'Hi, {name_passenger}, Select stations from the list below:')
    for index, (key, value) in enumerate(stations.items(), start=1):
        print(f'{index}. {key} Rs.{value}')
    try:
        choice = int(input('Enter the number of the station you want to select: '))
        match choice:
            case 1:
                station_name = 'UET'
            case 2:
                station_name = 'Sultan Pura'
            case 3:
                station_name = 'Railwat Station'
        
        station_price = stations[station_name]
        print(f"You selected: {station_name} with a ticket price of Rs. {station_price}.")
    except ValueError:
        print("Invalid input. Please enter a number corresponding to the station.")        

ticket_counter()