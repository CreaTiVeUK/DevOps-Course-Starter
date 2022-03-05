from todo_app.data.ViewModel import ViewModel
from todo_app.data.item import Item
import pytest

def test_todo_items():
    # Setup -> add a second item not part of To do
    new_item = Item(1, "Testing", "A card used for testing", "03/15/2022", "To Do", 12345)
    list = [new_item]
    item_view_model = ViewModel(list)
    #Act
    todo_items = item_view_model.todo_items
    #Assert
    assert 1 == len(todo_items)
    assert todo_items[0].list_name == "To Do"

def test_doing_items():
    # Setup -> add a second item not part of To do
    list = []
    list.append(Item(1, "Testing", "A card used for testing", "03/15/2022", "To Do", 12345))
    list.append(Item(2, "Testing", "A card used for testing", "03/15/2022", "Doing", 12345))
    item_view_model = ViewModel(list)
    #Act
    doing_items = item_view_model.doing_items
    #Assert
    assert 1 == len(doing_items)
    assert doing_items[0].list_name == "Doing"

def test_done_items():
    # Setup
    list = []
    list.append(Item(1, "Testing", "A card used for testing", "03/15/2022", "To Do", 12345))
    list.append(Item(2, "Testing", "A card used for testing", "03/15/2022", "Doing", 12345))
    list.append(Item(3, "Testing", "A card used for testing", "03/15/2022", "Done", 12345))
    list.append(Item(4, "Testing", "A card used for testing", "03/15/2022", "Done", 12345))
    item_view_model = ViewModel(list)
    #Act
    done_items = item_view_model.done_items
    #Assert
    assert 2 == len(done_items)
    assert done_items[0].list_name == "Done"