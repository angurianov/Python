def create_record(name, telephone, age):
    """Create Record"""
    record = {
        'name': name,
        'phone': telephone,
        'age': age
    }
    return record

user1 = create_record("Vasya", "+7-977-77-77-777", "40")
user2 = create_record("Petya", "33-33-43", "20")

print(user1)
print(user2)

def give_award(medal, *persons):
    """Give medals to persons"""
    for person in persons:
        print("Name " + person.title() + " get award " + medal)

give_award("Za Berlin", "Vasya", "Petya")
give_award("Za London", "Petya", "Kolya")
