
import unittest
from src.task import Task


class TestTask(unittest.TestCase):
    """
    Tests Task using the following test suites:
    Task Creation
    Task Status Tests
    Task Priority Tests
    Task Is Done Tests
    __str__,  __repr__
    """

    def test_create_task_with_default_values(self):
        """
        Tests Task creation with default values
        :return:
        """
        task = Task("Task1")
        self.assertEqual("Task1", task.title)
        self.assertEqual(Task.Priority.UNASSIGNED, task.priority)
        self.assertEqual(Task.Status.UNASSIGNED, task.status)

    def test_create_task_with_explicit_values(self):
        """
        Test task creation with explicit values
        :return:
        """
        # test priority and status assignment
        task = Task("Task2", Task.Status.PENDING, Task.Priority.LOW)
        self.assertEqual("Task2", task.title)
        self.assertEqual(Task.Priority.LOW, task.priority)
        self.assertEqual(Task.Status.PENDING, task.status)

    def test_task_with_empty_name(self):
        """
        Tests if empty task name will raise a value error
        :return:
        """
        with self.assertRaises(ValueError):
            Task("")

    def test_task_with_none_as_name(self):
        """
        Tests if None used for task name will raise a value error
        :return:
        """
        with self.assertRaises(ValueError):
            Task(None)


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

    def test_change_priority_incorrect_value(self):
        """
        Tests if setter error is raised if Priority value is incorrect
        :return:
        """
        task = Task("T1")
        with self.assertRaises(ValueError):
            task.change_priority("NOT_A_VALID_PRIORITY")


    def test_change_priority_high(self):
        """
        Tests change priority to HIGH
        :return:
        """
        task = Task("T1") #created by default with UNASSIGNED priority
        task.change_priority(Task.Priority.HIGH)
        self.assertEqual(Task.Priority.HIGH, task.priority)

    def test_change_priority_low(self):
            """
            Tests change priority to LOW
            :return:
            """
            task = Task("T1")  # created by default with UNASSIGNED priority
            task.change_priority(Task.Priority.LOW)
            self.assertEqual(Task.Priority.LOW, task.priority)

    def test_change_priority_medium(self):
        """
        Tests change priority to MEDIUM
        :return:
        """
        task = Task("T1") #created by default with UNASSIGNED priority
        task.change_priority(Task.Priority.MEDIUM)
        self.assertEqual(Task.Priority.MEDIUM, task.priority)

    def test_task_done(self):
        """
        Tests if tasks is done
        :return:
        """
        task = Task("T1")
        task.mark_status_complete()
        self.assertEqual(True, task.is_done())

    def test_task_unassigned_not_done(self):
        """
        Tests if task is not done
        :return:
        """
        task = Task("T1") # by default created with UNASSIGNED status
        self.assertEqual(False, task.is_done())

    def test_task_pending_not_done(self):
        """
        Tests if task is not done
        :return:
        """
        task = Task("T1") # by default created with UNASSIGNED status
        task.mark_status_pending()
        self.assertEqual(False, task.is_done())

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





