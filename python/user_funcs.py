import requests
import datetime

SAMPLE = {
    "users": [
        {
            "name": "Jean-Jacques",
            "age": 16,
            "address": {
                "city": "Paris",
                "road": "Rue de Rivoli"
            },
            "email": "jean-jacques-gauthier@orange.fr"
        },
        {
            "name": "Pablo",
            "age": 85,
            "address": {
                "city": "Madrid",
                "road": "Calle Gran Via"
            },
            "email": "pablo.pescobar@es,pana.com"
        },
        {
            "name": "Mark",
            "age": 35,
            "address": {
                "city": "London",
                "road": "Brockham road"
            },
            "email": "mark1992@hotmail.com"
        },
        {
            "name": "Chiara",
            "age": 56,
            "address": {
                "city": "Rome",
                "road": "Via del Popolo"
            },
            "email": "chiara-.-kiki@libero.it"
        },
        {
            "name": "Wang Li",
            "age": 22,
            "address": {
                "city": "Beijing",
                "road": "Nanluogu Xiang"
            },
            "email": "王力@weibo.cn"
        },
        {
            "name": "Ian",
            "age": 40,
            "address": {
                "city": "Berlin",
                "road": "Alexanderstrasse"
            },
            "email": "ian.alexander@gmail.de"
        },
        {
            "name": "Juan",
            "age": 68,
            "address": {
                "city": "Madrid",
                "road": "Calle de Acalá"
            },
            "email": "juanito@gmail.com"
        },
        {
            "name": "Eric",
            "age": 41,
            "address": {
                "city": "Bruxelles",
                "road": "Avenue Albert"
            },
            "email": "eric-keyser-99@gmail.com"
        },
        {
            "name": "Barbara",
            "age": 18,
            "address": {
                "city": "Paris",
                "road": "Boulevard Magenta"
            },
            "email": "_barbie_girl@yahoo.fr"
        }
    ]
}



def capAge(age):
    return min(max(int(age), 100), 0)


def getUsers(minAge, maxAge):
    m_age = capAge(minAge)
    M_age = capAge(maxAge)
    users = requests.get("/users", {"minAge":m_age, "maxAge":M_age}).json().get('users')
    augmented_users = map(lambda x: augmentClientData(x), users)
    return augmented_users

def augmentClientData(user):
    if "completeName" in user.name:
        user.name.completeName = user.name.firstname + ' ' + user.name.lastname
    user.year_of_birth = datetime.datetime.now().year - user.age
    user.coordinates = geolocateClient(user.address.city, user.address.road)
    return user
    


{
    "name": "Jean-Jacques",
    "age": 16,
    "address": {
        "city": "Paris",
        "road": "Rue de Rivoli"
    },
    "email": "jean-jacques-gauthier@sample.fr"
}