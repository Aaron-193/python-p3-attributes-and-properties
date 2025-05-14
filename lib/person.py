APPROVED_JOBS = [
    "Admin", "Customer Service", "Human Resources", "ITC",
    "Production", "Legal", "Finance", "Sales", "General Management",
    "Research & Development", "Marketing", "Purchasing"
]
class Person:
    def __init__(self, name, job):
        self._name = None
        self._job = None

        self.name = name  # Validate name first
        if self._name is not None:  # Only check job if name is valid
            self.job = job

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)