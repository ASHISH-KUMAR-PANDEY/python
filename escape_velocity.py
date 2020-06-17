def system_escape_velocity(planet):
    information = [
        {
            'planet': 'Mercury',
            've1': 4.25,
            've2': 67.7
        },
        {
            'planet': 'Venus',
            've1': 10.36,
            've2': 49.5
        },
        {
            'planet': 'Earth',
            've1': 11.186,
            've2': 42.1
        },
        {
            'planet': 'Mars',
            've1': 5.03,
            've2': 34.1
        },
        {
            'planet': 'Jupiter',
            've1': 60.20,
            've2': 18.5
        },
        {
            'planet': 'Saturn',
            've1': 36.09,
            've2': 13.6
        },
        {
            'planet': 'Uranus',
            've1': 21.38,
            've2': 9.6
        },
        {
            'planet': 'Neptune',
            've1': 23.56,
            've2': 7.7
        }
    ]

    ve1, ve2 = None, None
    for i in information:
        if i['planet'] == planet:
            ve1 = i['ve1']
        if i['planet'] == planet:
            ve2 = i['ve2']

    k = 0.2929

    ves = round(((k*ve2)**2+ve1**2)**(1/2), 1)

    ve1_earth, ve2_earth = None, None
    for i in information:
        if i['planet'] == 'Earth':
            ve1_earth = i['ve1']
        if i['planet'] == 'Earth':
            ve2_earth = i['ve2']
    
    ves_earth = ((k*ve2_earth)**2+ve1_earth**2)**(1/2)

    ratio = round(ves/ves_earth, 1)

    return ('The escape velocity from the system ' + str(planet) + '/Sun is ' + str(ves) + ' km/s.\n' +
    'The escape velocity from the system ' + str(planet) + '/Sun is ' + str(ratio) + ' times the escape velocity from the system Earth/Sun.')
