import os, sys, pickle

class Player:
    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position
    
    def __str__(self):
        return '\nName: %s\nNumber: %s\nPosition: %s' % (self.name, self.number, self.position)

    def __repr__(self):
        return self.__str__()

class Rosterdb:
    def __init__(self, file = None):
        if file == None:
            print('Must provide a filename')
            return
        self.file = file
        if os.path.isfile(file):
            try:
                f = open(file, 'rb')
            except IOError:
                sys.stderr.write('Problem opening file %s' % file)
                return
            try:
                self.db = pickle.load(f)
                return
            except pickle.UnpicklingError:
                sys.stderr.write('Not a pickled database')
                return
            f.close()
        else:
            self.db = []


    def add(self, name, number, position):
        self.db.append(Player(name, number, position))

    def remove(self, name):
        for i, player in enumerate(self.db):
            if player.name == name:
                del self.db[i]
                return True
        return False
            

    def store(self,file=None):
        try:
            f = open(self.file, 'wb')
        except IOError:
            sys.stderr.write('Problem opening file %s for write' % self.file)
            return
        pickle.dump(self.db, f)
        f.close()

    def __del__(self):
        if self.db:
            self.store()