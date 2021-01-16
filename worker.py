
#Описание работника:
#имя_фамилия
#возраст
#место работы
#есть ли прививка

#worker_list = ['Name', 'Surname', 'Age']
#worker_dict = {'Name_Surname': 'Basil Petrov',
               #"Age": 33,
               #'Place': 'shop',
              # 'Vaccine': True}
#print(worker_dict['Vaccine'])
#worker_dict['was_ill'] = False
#print(worker_dict)
#print(worker_dict.keys())
#print(worker_dict.values())

'''
Вход через КПП:
На входе оставляет каждый данные о себе:
    имя фамилия
    место работы
    вакцина есть ли
    температура
Мы должны сохранить всех кто пришел,
если у нас кто-то заболел и у них есть не привитые на месте работы
то мы должны закрыть вход и вывести проблемную зону.
'''


worker_dict = {'name_surname': None,
               'place': None,
               'vaccine': None,
               'temperature': None}

today_workers = []
while True:
    continue_check = input('Continue: ')
    if continue_check == 'No':
        print(f'Today workers: {today_workers}')
        break
    worker_dict['name_surname'] = input("Your name: ")
    worker_dict['place'] = input("Your place: ")
    worker_dict['vaccine'] = input("Vaccine?: ")
    print(worker_dict['vaccine'])
    worker_dict['temperature'] = float(input("temperature?: "))
    today_workers.append(worker_dict.copy())
    if worker_dict['temperature'] > 37.5:
        inf_place = worker_dict['place']
        ill_workers = []
        for worker in today_workers:
            print(worker['name_surname'], worker['place'], worker['vaccine'])
            if worker['place'] == inf_place and worker['vaccine'] == 'No':
                print('person is ill!')
                ill_workers.append(worker)
        print(f'Alarm! Next workers could be ill {ill_workers}')
        print(f'Today workers: {today_workers}')
        break