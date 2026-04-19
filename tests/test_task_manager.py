import unittest
from src.task import Task
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    """
    Tests Task Manager using the following test suites:
    Task Manager with empty task list
    Adding Tasks
    ToString equivalent __repr__, __str__
    """
    # TODO: and understand when and how to use: mock, autospec, patch and checking if methods are called
    # TODO: use set up and tear down to test singleton TaskManager

    def setUp(self):
        """
        Method used to clear all states, will automatically run after every step
        """
        TaskManager._instance = None # reset singleton before every test
        TaskManager._instance = TaskManager()

    def tearDown(self):
        """
        Method used to clear resources, automatically called after every test
        """
        #TODO: use it when testing save to file: closing file

    def test_create_task_manager_with_empty_list(self):
        """
        Tests that task manager is created with an empty list
        """
        self.assertTrue(not TaskManager().tasks) # Pythonic way, True if list is empty


    def test_add_task(self):
        """
        Test adding a task to task list
        """
        task = Task("t1")
        TaskManager().add_task(task)
        self.assertIn(task, TaskManager().tasks)

    def test_remove_task_when_task_list_not_empty(self):
        """
        Test removing task when task list is not empty
        """
        task = Task("t1")
        TaskManager().add_task(task)
        TaskManager().remove_task(task)
        self.assertNotIn(task, TaskManager().tasks)

    def test_remove_task_when_task_list_is_empty(self):
        """
        Test removing task when task list is empty. Should be handled gracefully by the code
        """
        task = Task("t1")
        TaskManager().remove_task(task)
        self.assertTrue(not TaskManager().tasks)  # Pythonic way, True if list is empty

    def test_remove_un_existing_task(self):
        """
        Test removing an un existent task from tasks list
        :return:
        """
        task1 = Task("t1")
        task2 = Task("t2")
        TaskManager().add_task(task1)
        TaskManager().remove_task(task2)
        self.assertIn(task1, TaskManager().tasks)
        self.assertEqual(1, len(TaskManager().tasks))


