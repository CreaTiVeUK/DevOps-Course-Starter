class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    def get_items_with_list(self, list_name):
        items = []
        for item in self._items:
            if item.list_name == list_name:
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

    """
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
    """
