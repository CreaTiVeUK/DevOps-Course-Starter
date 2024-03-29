class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    def get_items_with_list(self, status):
        items = []
        for item in self._items:
            if item.status == status:
                items.append(item)
        return items

    @property
    def todo_items(self):
        return self.get_items_with_list("To Do")
        
    @property
    def doing_items(self):
        return self.get_items_with_list("Doing")

    @property
    def done_items(self):
        return self.get_items_with_list("Done")
