def test_add_marks():
    S1 = Student('Anna', 'Margolina', 28, 'Moscow', [1,3,5])
    S1.add_mark(5)
    assert S1.marks_list == [1,3,5,5]

test_add_marks()
