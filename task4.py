class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours=None, rest_days=None, email=None):
        if hours is None:
            if rest_days is not None:
                hours = (7 - rest_days) * 8
            else: print("Недостаточно данных, нужны или часы или дни отдыха")
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        if self.hours is not None:
            salary = self.hours * self.hourly_payment
        elif self.rest_days is not None:
            salary = (7 - self.rest_days) * 8 * self.hourly_payment
        else:
            print("Недостаточно данных для расчета зп, нужны или часы или дни отдыха")
        return salary
    