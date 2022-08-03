class MyHashSet:
    x=[]

    def __init__(self):
        self.x=[]
        
    def add(self, key: int) -> None:
        self.x.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.x:
            self.x=list(set(self.x))
            self.x.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.x:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)