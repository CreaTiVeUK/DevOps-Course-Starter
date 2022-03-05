

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        items = []
        for item in self.items:
            if item.list_name == "To Do":
                items.append(item)
        return items

    @property
    def doing_items(self):
        items = []
        for item in self.items:
            if item.list_name == "Doing":
                items.append(item)
        return items

    @property
    def done_items(self):
        items = []
        for item in self.items:
            if item.list_name == "Done":
                items.append(item)
        return items
