import os, sys, pickle

class Event:
    def __init__(self, label, event_type, f1, f2, f3, d1, d2, g, ext):
        self.label = label
        self.event_type = event_type
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.d1 = d1
        self.d2 = d2
        self.g = g
        self.ext = ext

    def __str__(self):
        return '\nDate: %s\nEvent: %s\nF1: %s\nF2: %s\nF3: %s\nD1: %s\nD2: %s\nG: %s\nExt: %s' % (self.label, self.event_type, self.f1, self.f2, self.f3, self.d1, self.d2, self.g, self.ext)

    def __repr__(self):
        return self.__str__()

class Eventdb:
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

    def add(self, label, event_type, f1, f2, f3, d1, d2, g, ext):
        self.db.append(Event(label, event_type, f1, f2, f3, d1, d2, g, ext))    

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