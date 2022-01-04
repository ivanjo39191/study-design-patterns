import copy
from collections import OrderedDict

class Ninja:
    def __init__(self, name, skill, **rest):
        self.name = name
        self.skill = skill
        self.__dict__.update(**rest)
    
    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append(f'{i}: {ordered[i]}\n')
        return ''.join(mylist)
        
        

class Prototype:
    def __init__(self):
        self.objects = dict()
    
    def register(self, identifier, obj):
        self.objects[identifier] = obj
        
    def unregister(self, identifier, obj):
        del self.objects[identifier]
    
    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise VauleError(f'Incorrect object identifier: {identifier}.')
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj
        
def main():
    ninja1 = Ninja('漩渦鳴人', '螺旋丸')
    prototype = Prototype()
    cid = 'first ninja'
    prototype.register(cid, ninja1)
    ninja2 = prototype.clone(cid, skill='大玉螺旋丸')
    print(ninja1)
    print(ninja2)
    print(ninja1)
    
if __name__ == '__main__':
    main()
    