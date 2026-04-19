class TaskManager:
  """
  Task Manager handles a list of Tasks.
  Operations:
  - filter by priority
  - filter by status
  - order by priority
  - order by status
  - edit task
  - delete task
  - add task
  - load tasks from file (JSON file)
  - save tasks to file (JSON file)
  - __str__, __repr__
  """
  _instance = None #class variable, needed for singleton pattern

  def __new__(cls):
    """
    Need to control instance creation since it class is using Singleton Pattern
    """
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    if not hasattr(self, 'tasks'): # hasattr checks if the attribute already exists — so tasks only gets initialised on the very first cal
      self.tasks = []

  def add_task(self, task):
    """
    Adds a task to the task list
    """
    self.tasks.append(task)

  def remove_task(self, task):
    """
    Removes a task from the task list.
    If list is empty removal is not attempted
    """
    try:
      self.tasks.remove(task)
    except ValueError:
      pass # handle gracefully, do nothing


