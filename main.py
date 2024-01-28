"""
saját worldlist generálása
töltsük fel a változó tömböt stringként vesszővel elválasztva.
minden betű legyen mindig kis betű, a program automatikussan készít nagy kezdőbetűvel is
egy varriánst
"""
import datetime
import uuid

pets = ["bia", "leila", "csuvi", "csuvy"]
childs = ["janka", "botond", "barnabas"]
favourites = ["toyota", "tankcsapda", "anime", "peugeot", "juventus", "juventus", "realMadrid"]
first_name = ["kiss", "vitez"]
last_name = ["viktor", "vivien", "elemer", "zoltan"]
# a születésnapok első eleme mindig legyen egy "" üres karakter, így lesz szám nélküli jelszónk is
birth_numbers = ["", "1988", "0423", "88", "1128", "1999", "2000", "20001002", "1002"]

now = datetime.datetime.now()

file_name = "wordlist_" + \
            now.strftime("%Y_%m_%d_%H_%M_%S_") + \
            str(uuid.uuid4())[0:4] + ".txt"

file = open(file_name, 'w')


def create_banner():
    print("*" * 50)
    print("Create Password wordlist with data......")
    print("*" * 50)


def create_file():
    i = 0
    for num in birth_numbers:
        for fname in first_name:
            for lname in last_name:
                file.write(fname.capitalize() + lname + '\n')
                file.write(fname + lname.capitalize() + '\n')
                file.write(fname.capitalize() + lname.capitalize() + '\n')
                file.write(fname.capitalize() + lname + num + '\n')
                file.write(fname + lname.capitalize() + num + '\n')
                file.write(fname.capitalize() + lname.capitalize() + num + '\n')

                i += 6
        for pet in pets:
            file.write(pet + num + "\n")
            file.write(pet.capitalize() + num + "\n")
            i += 2
        for child in childs:
            file.write(child + num + "\n")
            file.write(child.capitalize() + num + "\n")
            i += 2
        for fav in favourites:
            file.write(fav + num + "\n")
            file.write(fav.capitalize() + num + "\n")
            i += 2

    file.close()
    print("created file:", file.name)

    print("generated password number:", i)


if __name__ == '__main__':
    create_banner()
    create_file()
