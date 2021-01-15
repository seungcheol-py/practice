my_home = {
    'location': 'seoul',
    'area': '02'
}

print(my_home['location'])

print(my_home.get('location'))

# error가 나오지 않고 None이 나온다.
print(my_home.get('name'))
