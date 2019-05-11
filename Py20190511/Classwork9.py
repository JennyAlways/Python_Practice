class Human: #定义一个类别
    def __init__(self, height, gender, name): #定义一个实例， 展示属性
        #确定属性
        self.height = height
        self.gender = gender
        self.name = name

    def print_info(self):
        print("height", self.height)
        print("gender", self.gender)
        print("name", self.name)

rock = Human(181, "male", "rock")
rock.print_info()

teacher = Human(170, 'male", "teacher')
teacher.print_info()
