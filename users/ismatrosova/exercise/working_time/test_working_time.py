from working_time import (out_priority_task,)

def test_out_priority_task_1():
    input1 = {"a":"breakfast", "b":"lunch", "c":"dinner"}
    expected = "breakfast"
    assert out_priority_task(input1) == expected

def test_out_priority_task_2():
    input1 = {"b":"lunch", "c":"dinner"}
    expected = "lunch"
    assert out_priority_task(input1) == expected

def test_out_priority_task_3():
    input1 = {"c":"dinner", "a":"breakfast", "b":"lunch"}
    expected = "breakfast"
    assert out_priority_task(input1) == expected

def test_out_priority_task_4():
    input1 = {"c":"dinner", "-":"breakfast", "-":"lunch"}
    expected = "dinner"
    assert out_priority_task(input1) == expected