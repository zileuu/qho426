# qho426
University work for QHO426 - Problem solving through programming
from person import Person

class Database:

    def __init__(self):
        self.name = "Piotr's Database"
        self.people = []
        self.n_people = len(self.people)

    def add_person(self, person):
        self.people.append(person)
    
    def remove_person(self, person):
        self.people.remove(person)

    def display_all(self):
        for p in self.people:
            p.hello()

if __name__ == "__main__":
    x = Person("Rita", 7, 72, 88)
    y = Person("Klaudio", 34)
    z = Person("Ada", 88, 90, 20)
    a = Person("Henry")
    db = Database()
    db.add_person(x)
    db.add_person(y)
    db.add_person(z)
    db2 = Database()
    db2.add_person(a)
    db.display_all()
    db.remove_person(y)
    db.display_all()
    db2.display_all()