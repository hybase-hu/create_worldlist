"""
saját worldlist generálása
töltsük fel a változó tömböt stringként vesszővel elválasztva.
az első betű legyen mindig kis betű, a program automatikussan készít nayg kezdőbetűvel is
egy varriánst
"""
import datetime
import uuid


names = ["istvan", "isti", "pisti", "petra", "petracska"]
pets = ["bia", "leila", "csuvi", "csuvy"]
favourites = ["toyota", "tankcsapda", "anime","peugeot","juventus"]
# a születésnapok első eleme mindig legyen egy "" üres karakter, így lesz szám nélküli jelszónk is
birth_numbers = ["", "1988", "0423", "88", "1128", "1999"]

now = datetime.datetime.now()

file_name = "wordlist_" + \
            now.strftime("%Y_%m_%d_%H_%M_%S_") + \
            str(uuid.uuid4())[0:4] + ".txt"

file = open(file_name, 'w')


def create_banner():
    print("#/" * 10)
    print("#/" * 10)
    print("\tPassword wordlist......")
    print("#/" * 10)
    print("#/" * 10)


def create_file():
    i = 0
    for num in birth_numbers:
        for name in names:
            file.write(name + num + "\n")
            file.write(name.capitalize() + num + "\n")
            i += 2
        for pet in pets:
            file.write(pet + num + "\n")
            file.write(pet.capitalize() + num + "\n")
            i += 2
        for fav in favourites:
            file.write(fav + num + "\n")
            file.write(fav.capitalize() + num + "\n")
            i += 2

    file.close()
    print("--" * 10)
    print("--" * 10)
    print("created file:", file.name)

    print("generated password number:", i)
    print("--" * 10)
    print("--" * 10)


if __name__ == '__main__':
    create_banner()
    create_file()
