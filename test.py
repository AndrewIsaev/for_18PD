#новый словарь нужно было объявить в циикле)

users = [{'id': 1, 'imia': 'Hudson', 'familia': 'Pauloh', 'vozrast': 31, 'pochta': 'elliot16@mymail.com',
          'role': 'customer', 'phone': '6197021684'},
         {'id': 2, 'imia': 'George', 'familia': 'Matter', 'vozrast': 41, 'pochta': 'lawton46@mymail.com',
          'role': 'executor', 'phone': '8314786677'},
         {'id': 3, 'imia': 'Grant', 'familia': 'Traviser', 'vozrast': 23, 'pochta': 'tobias45@mymail.com',
          'role': 'customer', 'phone': '9528815998'},
         {'id': 4, 'imia': 'Malcolm', 'familia': 'Douglasoh', 'vozrast': 28, 'pochta': 'daniel37@mymail.com',
          'role': 'customer', 'phone': '6428998684'},
         {'id': 5, 'imia': 'Lester', 'familia': 'Archibaldoh', 'vozrast': 20, 'pochta': 'joshua18@mymail.com',
          'role': 'executor', 'phone': '8825887253'},
         {'id': 6, 'imia': 'Gareth', 'familia': 'Tobiaser', 'vozrast': 27, 'pochta': 'barnabe18@mymail.com',
          'role': 'customer', 'phone': '8254630383'},
         {'id': 7, 'imia': 'Vivian', 'familia': 'Philipik', 'vozrast': 49, 'pochta': 'jaime46@mymail.com',
          'role': 'customer', 'phone': '9884423362'},
         {'id': 8, 'imia': 'Nate', 'familia': 'Travisik', 'vozrast': 18, 'pochta': 'nate46@mymail.com',
          'role': 'executor', 'phone': '8353350197'},
         {'id': 9, 'imia': 'Norman', 'familia': 'Larryoh', 'vozrast': 37, 'pochta': 'shahaf06@mymail.com',
          'role': 'executor', 'phone': '6448371821'},
         {'id': 10, 'imia': 'George', 'familia': 'Emiloh', 'vozrast': 49, 'pochta': 'grant35@mymail.com',
          'role': 'executor', 'phone': '8872495923'},
         {'id': 11, 'imia': 'Graham', 'familia': 'Reginalder', 'vozrast': 20, 'pochta': 'george38@mymail.com',
          'role': 'executor', 'phone': '7356168167'},
         {'id': 12, 'imia': 'Malcolm', 'familia': 'Jameser', 'vozrast': 22, 'pochta': 'graham27@mymail.com',
          'role': 'executor', 'phone': '8967033901'},
         {'id': 13, 'imia': 'Marvin', 'familia': 'Austenoh', 'vozrast': 19, 'pochta': 'nicholas46@mymail.com',
          'role': 'executor', 'phone': '6723331776'},
         {'id': 14, 'imia': 'Jack', 'familia': 'Normaner', 'vozrast': 32, 'pochta': 'myron25@mymail.com',
          'role': 'executor', 'phone': '7490416454'},
         {'id': 15, 'imia': 'Travis', 'familia': 'Chanceer', 'vozrast': 20, 'pochta': 'kurt17@mymail.com',
          'role': 'customer', 'phone': '9491120005'},
         {'id': 16, 'imia': 'Neil', 'familia': 'Ronaldoh', 'vozrast': 43, 'pochta': 'john36@mymail.com',
          'role': 'customer', 'phone': '8913865074'},
         {'id': 17, 'imia': 'Shahaf', 'familia': 'Larryoh', 'vozrast': 33, 'pochta': 'ebenezer08@mymail.com',
          'role': 'customer', 'phone': '6514816015'},
         {'id': 18, 'imia': 'Wayne', 'familia': 'Markik', 'vozrast': 43, 'pochta': 'larry37@mymail.com',
          'role': 'executor', 'phone': '6496155163'},
         {'id': 19, 'imia': 'Dougie', 'familia': 'Adrianik', 'vozrast': 23, 'pochta': 'vincent46@mymail.com',
          'role': 'customer', 'phone': '9965723667'},
         {'id': 20, 'imia': 'Vincent', 'familia': 'Davider', 'vozrast': 47, 'pochta': 'cuthbert36@mymail.com',
          'role': 'executor', 'phone': '7125872211'},
         {'id': 21, 'imia': 'Addison', 'familia': 'Reginaldik', 'vozrast': 48, 'pochta': 'reginald25@mymail.com',
          'role': 'executor', 'phone': '9963171227'},
         {'id': 22, 'imia': 'Arthur', 'familia': 'Chanceik', 'vozrast': 23, 'pochta': 'stephen25@mymail.com',
          'role': 'executor', 'phone': '6786170626'},
         {'id': 23, 'imia': 'Earl', 'familia': 'Frankliner', 'vozrast': 40, 'pochta': 'lawton47@mymail.com',
          'role': 'executor', 'phone': '7851277139'},
         {'id': 24, 'imia': 'Marshall', 'familia': 'Arloer', 'vozrast': 43, 'pochta': 'floyd36@mymail.com',
          'role': 'executor', 'phone': '6442333628'},
         {'id': 25, 'imia': 'Mark', 'familia': 'Nicholasoh', 'vozrast': 33, 'pochta': 'nicolas35@mymail.com',
          'role': 'customer', 'phone': '8143159413'},
         {'id': 26, 'imia': 'Edgar', 'familia': 'Arthurik', 'vozrast': 18, 'pochta': 'vincent45@mymail.com',
          'role': 'executor', 'phone': '6159310195'},
         {'id': 27, 'imia': 'Travis', 'familia': 'Pelegoh', 'vozrast': 24, 'pochta': 'jeffrey05@mymail.com',
          'role': 'executor', 'phone': '9300837797'},
         {'id': 28, 'imia': 'Nate', 'familia': 'Albertoh', 'vozrast': 30, 'pochta': 'peleg36@mymail.com',
          'role': 'executor', 'phone': '6158921977'},
         {'id': 29, 'imia': 'Cardew', 'familia': 'Hughik', 'vozrast': 28, 'pochta': 'jolyon37@mymail.com',
          'role': 'executor', 'phone': '6787970230'},
         {'id': 30, 'imia': 'Graham', 'familia': 'Joeyoh', 'vozrast': 28, 'pochta': 'myron26@mymail.com',
          'role': 'executor', 'phone': '6962652739'}]

new_users = []
for user in users:
    new_user = {}
    new_user["id"] = user["id"]
    new_user["first_name"] = user["imia"]
    new_user["last_name"] = user["familia"]
    new_user["age"] = user["vozrast"]
    new_user["email"] = user["pochta"]
    new_user["role"] = user["role"]
    new_user["phone"] = user["phone"]
    new_users.append(new_user)

print(new_users)
