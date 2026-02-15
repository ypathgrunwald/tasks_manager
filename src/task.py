from enum import Enum

class Task:
    """
    Task Class Defines a class and it's behaviour.
    Tasks can have `title`, `description`, `priority`, `status`
    Task is created in PENDING status and moves to COMPLETE
    Task is created with UNASSIGNED priority and can be assigned one later
    """
    class Status(Enum):
        PENDING = "PENDING"
        COMPLETE = "COMPLETE"
        UNASSIGNED = "UNASSIGNED"

    class Priority(Enum):
        UNASSIGNED = "UNASSIGNED"
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"

    def __init__(self, title, status=Status.UNASSIGNED, priority=Priority.UNASSIGNED):
        self.title = title
        self.status = status
        self.priority = priority

    @property
    def status(self):
        return self._status
    '''
    Attributes in Python are public, to enforce a specific value need to check value and raise
    an error if the value is incorrect
    '''
    @status.setter
    def status(self, value):
        if not isinstance(value, Task.Status):
            raise ValueError("Invalid Status")
        self._status = value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if not isinstance(value, Task.Priority):
            raise ValueError("Invalid Priority")
        self._priority = value

    def mark_status_complete(self):
        self.status = Task.Status.COMPLETE

    def mark_status_pending(self):
        self.status = Task.Status.PENDING

    def mark_status_unassigned(self):
        self.status = Task.Status.UNASSIGNED

    def change_priority(self, priority):
        if not isinstance(priority, Task.Priority):
            raise ValueError("Invalid Priority")
        self.priority = priority

    def is_done(self):
        return self.status == Task.Status.COMPLETE

    def __str__(self):
        return f"{self.title}: {self.status.value}, {self.priority.value}"

    def __repr__(self):
        return f"Task {self.title} is {self.status.value} and has {self.priority.value} priority."

