
class OneIndexList:

    def __init__(self, items=list()):
        self.items = list(items)

    def __getitem__(self, item):
        return self.items[item-1]
