class Manage:
    def __init__(self, name, age, register, month_value):
        self.name = name
        self.age = age
        self.register = register
        self.month_value = month_value
        
    def checkName(self):
        name_len = len(self.name)
        if(name_len > 25):
            return 'Name is too big!'
        else:
            return self.name
    
    def checkAge(self):
        try:
            age = int(self.age)
            if(age < 0):
                return 'Negative age!'
            else:
                return age
        except:
            return 'Invalid age! (Is it a number?)'
    
    def checkRegister(self):
        try:
            register = int(self.register)
            return register
        except:
            return 'Invalid register number. (is it a number?)'
        
    def checkValue(self):
        try:
            month_value = float(self.month_value)
            return month_value
        except:
            return 'Invalid value!'
        
        