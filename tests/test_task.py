
import unittest
from src.task import Task

'''
Tests Task using the following test scenarios:
Task Creation - DONE
Status Tests - DONE
Priority Tests - DONE
Task Is Done - DONE
ToString equivalent __repr__

'''
class TestTask(unittest.TestCase):
    def test_create_task(self):
        """
        Tests Task creation
        :return:
        """
        task = Task("Task1")
        self.assertEqual("Task1", task.title)
        self.assertEqual(Task.Priority.UNASSIGNED, task.priority)
        self.assertEqual(Task.Status.UNASSIGNED, task.status)

        # test priority and status assignment
        task = Task("Task2", Task.Status.PENDING, Task.Priority.LOW)
        self.assertEqual("Task2", task.title)
        self.assertEqual(Task.Priority.LOW, task.priority)
        self.assertEqual(Task.Status.PENDING, task.status)

    def test_mark_status_unassigned(self):
        """
        Tests mark status as unassigned
        :return:
        """
        task = Task("T1", Task.Status.PENDING)
        task.mark_status_unassigned()
        self.assertEqual(Task.Status.UNASSIGNED, task.status)

    def test_mark_status_complete(self):
        """
        Tests mark status as complete
        :return:
        """
        task = Task("T1")
        task.mark_status_complete()
        self.assertEqual(Task.Status.COMPLETE, task.status)

    def test_mark_status_pending(self):
        """
        Tests mark status as pending
        :return:
        """
        task = Task("T1")
        task.mark_status_pending()
        self.assertEqual(Task.Status.PENDING, task.status)

    def test_status_access_modifiers(self):
        """
        Tests if setter and getter work correctly
        :return:
        """
        task = Task("T1", Task.Status.PENDING)
        task.status = Task.Status.UNASSIGNED
        self.assertEqual(Task.Status.UNASSIGNED, task.status)

    def test_status_setter_invalid_value(self):
        """
        Tests setter error raised if Status value is incorrect
        :return:
        """
        task = Task("Test Task")
        with self.assertRaises(ValueError):
            task.status = "NOT_A_VALID_STATUS"  # this should trigger your validation

    def test_priority_access_modifiers(self):
        """
        Tests if setter and getter work correctly
        :return:
        """
        task = Task("T1")
        task.priority = Task.Priority.LOW
        self.assertEqual(Task.Priority.LOW, task.priority)

    def test_priority_setter_incorrect_value(self):
        """
        Tests if setter error is raised if Priority value is incorrect
        :return:
        """
        task = Task("T1")
        with self.assertRaises(ValueError):
            task.priority = "NOT_A_VALID_PRIORITY"

    def test_change_priority(self):
        """
        Tests change priority method
        :return:
        """
        task = Task("T1") #created by default with UNASSIGNED priority
        task.change_priority(Task.Priority.HIGH)
        self.assertEqual(Task.Priority.HIGH, task.priority)

    def test_is_task_done(self):
        task = Task("T1") #created by default with UNASSIGNED priority
        self.assertEqual(False, task.is_done())
        task.mark_status_complete()
        self.assertEqual(True, task.is_done())

    def test_str(self):
        """
        Tests __str__ method that represents task as:
        TaskName: Status, Priority
        :return:
        """
        task = Task("T1", Task.Status.PENDING, Task.Priority.HIGH)
        expected_str_repr = "T1: PENDING, HIGH"
        self.assertEqual(expected_str_repr, str(task))

    def test_repr(self):
        """
        Tests __str__ method that represents task as:
        Task TaskName is Status and has Priority
        :return:
        """
        task = Task("T1", Task.Status.PENDING, Task.Priority.HIGH)
        expected_str_repr = "Task T1 is PENDING and has HIGH priority."
        self.assertEqual(expected_str_repr, repr(task))





