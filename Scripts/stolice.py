#Quiz - pytania o stolice
#

import random

stolice={'Algieria': 'Algier', 'Angola': 'Luanda', 'Benin': 'Porto-Novo', 'Botswana': 'Gaborone', 'Burkina Faso': 'Wagadugu', 'Burundi': 'Gitega', 'Czad': 'Ndżamena', 'Demokratyczna Republika Konga': 'Kinszasa', 'Dżibuti': 'Dżibuti', 'Egipt': 'Kair', 'Erytrea': 'Asmara', 'Etiopia': 'Addis Abeba', 'Gabon': 'Libreville', 'Gambia': 'Bandżul', 'Ghana': 'Akra', 'Gwinea': 'Konakry', 'Gwinea Bissau': 'Bissau', 'Gwinea Równikowa': 'Malabo', 'Kamerun': 'Jaunde', 'Kenia': 'Nairobi', 'Komory': 'Moroni', 'Kongo': 'Brazzaville', 'Lesotho': 'Maseru', 'Liberia': 'Monrovia', 'Libia': 'Trypolis', 'Madagaskar': 'Antananarywa', 'Malawi': 'Lilongwe', 'Mali': 'Bamako', 'Maroko': 'Rabat', 'Mauretania': 'Nawakszut', 'Mauritius': 'Port Louis', 'Mozambik': 'Maputo', 'Namibia': 'Windhuk', 'Niger': 'Niamey', 'Nigeria': 'Abudża', 'RPA': 'Pretoria', 'Republika Środkowoafrykańska': 'Bangi', 'Republika Zielonego Przylądka': 'Praia', 'Rwanda': 'Kigali', 'Senegal': 'Dakar', 'Seszele': 'Victoria', 'Sierra Leone': 'Freetown', 'Somalia': 'Mogadiszu', 'Eswatini': 'Mbabane', 'Sudan': 'Chartum', 'Sudan Południowy': 'Dżuba', 'Tanzania': 'Dodoma', 'Togo': 'Lomé', 'Tunezja': 'Tunis', 'Uganda': 'Kampala', 'Wybrzeże Kości Słoniowej': 'Jamusukro', 'Wyspy Świętego Tomasza i Książęca': 'Sao Tome', 'Zambia': 'Lusaka', 'Zimbabwe': 'Harare', 'Argentyna': 'Buenos Aires', 'Boliwia': 'Sucre', 'Brazylia': 'Brasília', 'Chile': 'Santiago', 'Ekwador': 'Quito', 'Gujana': 'Georgetown', 'Kolumbia': 'Bogota', 'Paragwaj': 'Asunción', 'Peru': 'Lima', 'Surinam': 'Paramaribo', 'Urugwaj': 'Montevideo', 'Wenezuela': 'Caracas', 'Antigua i Barbuda': 'Saint John’s', 'Bahamy': 'Nassau', 'Barbados': 'Bridgetown', 'Belize': 'Belmopan', 'Dominika': 'Roseau', 'Dominikana': 'Santo Domingo', 'Grenada': 'Saint George’s', 'Gwatemala': 'Gwatemala', 'Haiti': 'Port-au-Prince', 'Honduras': 'Tegucigalpa', 'Jamajka': 'Kingston', 'Kanada': 'Ottawa', 'Kostaryka': 'San José', 'Kuba': 'Hawana', 'Meksyk': 'Meksyk', 'Nikaragua': 'Managua', 'Panama': 'Panama', 'Saint Kitts i Nevis': 'Basseterre', 'Saint Lucia': 'Castries', 'Saint Vincent i Grenadyny': 'Kingstown', 'Salwador': 'San Salvador', 'Stany Zjednoczone': 'Waszyngton', 'Trynidad i Tobago': 'Port-of-Spain', 'Afganistan': 'Kabul', 'Arabia Saudyjska': 'Rijad', 'Armenia': 'Erywań', 'Azerbejdżan': 'Baku', 'Bahrajn': 'Manama', 'Bangladesz': 'Dhaka', 'Bhutan': 'Thimphu', 'Brunei': 'Bandar Seri Begawan', 'Chiny': 'Pekin', 'Cypr': 'Nikozja', 'Filipiny': 'Manila', 'Gruzja': 'Tbilisi', 'Indie': 'Nowe Delhi', 'Indonezja': 'Dżakarta', 'Irak': 'Bagdad', 'Iran': 'Teheran', 'Izrael': 'Tel Awiw-Jafa [a]', 'Japonia': 'Tokio', 'Jemen': 'Sana', 'Jordania': 'Amman', 'Kambodża': 'Phnom Penh', 'Katar': 'Doha', 'Kazachstan': 'Nur-Sułtan', 'Kirgistan': 'Biszkek', 'Korea Południowa': 'Seul', 'Korea Północna': 'Pjongjang', 'Kuwejt': 'Kuwejt', 'Laos': 'Wientian', 'Liban': 'Bejrut', 'Malediwy': 'Male', 'Malezja': 'Kuala Lumpur', 'Mjanma': 'Naypyidaw', 'Mongolia': 'Ułan Bator', 'Nepal': 'Katmandu', 'Oman': 'Maskat', 'Pakistan': 'Islamabad', 'Rosja': 'Moskwa', 'Singapur': 'Singapur', 'Sri Lanka': 'Sri Dźajawardanapura Kotte', 'Syria': 'Damaszek', 'Tadżykistan': 'Duszanbe', 'Tajlandia': 'Bangkok', 'Timor Wschodni': 'Dili', 'Turcja': 'Ankara', 'Turkmenistan': 'Aszchabad', 'Uzbekistan': 'Taszkent', 'Wietnam': 'Hanoi', 'Zjednoczone Emiraty Arabskie': 'Abu Zabi', 'Australia': 'Canberra', 'Fidżi': 'Suva', 'Kiribati': 'Bairiki', 'Nowa Zelandia': 'Wellington', 'Palau': 'Ngerulmud', 'Papua-Nowa Gwinea': 'Port Moresby', 'Samoa': 'Apia', 'Mikronezja': 'Palikir', 'Tonga': 'Nukualofa', 'Tuvalu': 'Vaiaku', 'Vanuatu': 'Port Vila', 'Wyspy Marshalla': 'Majuro', 'Wyspy Salomona': 'Honiara', 'Albania': 'Tirana', 'Andora': 'Andora', 'Austria': 'Wiedeń', 'Belgia': 'Bruksela', 'Białoruś': 'Mińsk', 'Bośnia i Hercegowina': 'Sarajewo', 'Bułgaria': 'Sofia', 'Chorwacja': 'Zagrzeb', 'Czarnogóra': 'Podgorica', 'Czechy': 'Praga', 'Dania': 'Kopenhaga', 'Estonia': 'Tallinn', 'Finlandia': 'Helsinki', 'Francja': 'Paryż', 'Grecja': 'Ateny', 'Hiszpania': 'Madryt', 'Holandia': 'Amsterdam', 'Irlandia': 'Dublin', 'Islandia': 'Reykjavík', 'Liechtenstein': 'Vaduz', 'Litwa': 'Wilno', 'Luksemburg': 'Luksemburg', 'Łotwa': 'Ryga', 'Macedonia Północna': 'Skopje', 'Malta': 'Valletta', 'Mołdawia': 'Kiszyniów', 'Monako': 'Monako', 'Niemcy': 'Berlin', 'Norwegia': 'Oslo', 'Polska': 'Warszawa', 'Portugalia': 'Lizbona', 'Rosja': 'Moskwa', 'Rumunia': 'Bukareszt', 'San Marino': 'San Marino', 'Serbia': 'Belgrad', 'Słowacja': 'Bratysława', 'Słowenia': 'Lublana', 'Szwecja': 'Sztokholm', 'Ukraina': 'Kijów', 'Watykan': 'Watykan', 'Węgry': 'Budapeszt', 'Wielka Brytania': 'Londyn', 'Włochy': 'Rzym'}
listaABCD = ['A','B','C','D']
slownikABCD = {'A':0, 'B':1, 'C':2, 'D':3}

def quiz():

    punkty = 0
    wybraneOdp={}


    #Losowe ustawienie stolic
    kraje=list(stolice.keys())
    random.shuffle(kraje)

    for numerPytania in range(10):
        poprawnaOdp = stolice[kraje[numerPytania]]
        niepoprawnaOdp = list(stolice.values())
        del niepoprawnaOdp[niepoprawnaOdp.index(poprawnaOdp)]
        niepoprawnaOdp = random.sample(niepoprawnaOdp, 3)
        odpowiedzi = niepoprawnaOdp + [poprawnaOdp]
        random.shuffle(odpowiedzi)


        print(str(numerPytania+1) + '. Co jest stolicą kraju ' + kraje[numerPytania] + '?')
        for i in range(4):
            print('    ' + listaABCD[i] + '. ' + odpowiedzi[i])

            
        print('Wpisz odpowiedź:')
        odpGracza=input()

        while odpGracza not in listaABCD:
            print('Niewłaściwy format odpowiedzi. Wpisz A, B, C lub D.')
            odpGracza=input()
            
        if odpGracza==listaABCD[odpowiedzi.index(poprawnaOdp)]:
            punkty = punkty + 1

        wybraneOdp['pytanie' + str(numerPytania+1)]= 'Co jest stolicą kraju ' + kraje[numerPytania] + '?'
        wybraneOdp['poprawna' + str(numerPytania+1)]=listaABCD[odpowiedzi.index(poprawnaOdp)] + '. ' + poprawnaOdp
        wybraneOdp['wybrana' + str(numerPytania+1)]=odpGracza + '. ' + odpowiedzi[slownikABCD[odpGracza]]
        



    print('\nLiczba punktów: ' + str(punkty) + '/10\n')
    print('Wybrane odpowiedzi:\n')
    for numerPytania in range(10):
        print('Pytanie numer ' + str(numerPytania + 1) + '.')
        if wybraneOdp['wybrana' + str(numerPytania+1)] == wybraneOdp['poprawna' + str(numerPytania+1)]:
            print('Poprawna odpowiedź.')
        else:
            print('Zła odpowiedź')
        print('Pytanie: ' + wybraneOdp['pytanie' + str(numerPytania+1)])    
        print('Wybrana odpowiedź: ' + wybraneOdp['wybrana' + str(numerPytania+1)])
        print('Poprawna odpowiedź: ' + wybraneOdp['poprawna' + str(numerPytania+1)] + '\n')    

quiz()

while True:
    print('Wciśnij N, aby zacząć nowy quiz lub Q aby zakończyć.')
    NowaKoniec = input()
    if NowaKoniec == 'n' or NowaKoniec == 'N':
        quiz()
        continue
    elif NowaKoniec == 'q' or NowaKoniec == 'Q':
        break
    else:
        print('Niewłaściwy znak.')
        

       
