class Job:
    def __init__(self, id, job_name, job_field, salary) -> None:
        self._id = id
        self._job_name = job_name
        self._job_field = job_field
        self._salary = salary
    
    def __str__(self) -> str:
        return f'ID: {self._id}, Tên: {self._job_name}, Lĩnh vực: {self._job_field}, Lương: {self._salary}'

class AI(Job):
    def __init__(self, job_code, job_name, field_name, salary, python_skill, ml_skill, deep_skill, math_skill):
        Job.__init__(self, job_code, job_name, field_name, salary)
        self._python_skill = python_skill
        self._ml_skill = ml_skill
        self._deep_skill = deep_skill
        self._math_skill = math_skill
        
    def __str__(self) -> str:
        return super().__str__() + f', Kỹ năng: {self._python_skill}, {self._ml_skill}, {self._deep_skill}, {self._math_skill}'
    
    def evaluate(self):
        score_dict = {
            "python_skill": self._python_skill,
            "ml_skill": self._ml_skill,
            "deep_skill": self._deep_skill,
            "math_skill": self._math_skill
        }
        score = sum(score_dict.values()) / 4
        
        if score > 9:
            return "Rất phù hợp"
        elif score > 7:
            return "Phù hợp"
        elif score > 5:
            return "Tạm được"
        elif score > 3:
            skill_under_4 = {key: value for (key, value) in score_dict.items() if value < 4}
            return f"Cần bổ sung thêm kiến thức, kỹ năng: {skill_under_4}"
        else:
            return "Bad"

class BackEnd(Job):
    def __init__(self, id, job_name, job_field, salary, SQL_skill, OOP_skill, Api_skill, Java_skill) -> None:
        Job.__init__(self, id, job_name, job_field, salary)
        self._Sql_skill = SQL_skill
        self._OOP_skill = OOP_skill
        self._Api_skill = Api_skill
        self._Java_skill = Java_skill
        
    def __str__(self) -> str:
        return super().__str__() + f', Kỹ năng: {self._Sql_skill}, {self._OOP_skill}, {self._Api_skill}, {self._Java_skill}'
    
    def evaluate(self):
        score_dict = {
            "sql_skill": self._Sql_skill,
            "oop_skill": self._OOP_skill,
            "api_skill": self._Api_skill,
            "java_skill": self._Java_skill
        }
        score = sum(score_dict.values()) / 4
        if score > 9:
            return "Rất phù hợp"
        elif score > 7:
            return "Phù hợp"
        elif score > 5:
            return "Tạm được"
        elif score > 3:
            skill_under_4 = {key: value for (key, value) in score_dict.items() if value < 4}
            return f"Cần bổ sung thêm kiến thức, kỹ năng: {skill_under_4}"
        else:
            return "Bad"

class FrontEnd(Job):
    def __init__(self, id, job_name, job_field, salary, HTML_skill, CSS_skill, Nodejs_skill, UX, UI) -> None:
        Job.__init__(self, id, job_name, job_field, salary)
        self._HTML_skill = HTML_skill
        self._CSS_skill = CSS_skill
        self._Nodejs_skill = Nodejs_skill
        self._UX = UX
        self._UI = UI
    
    def __str__(self) -> str:
        return super().__str__() + f', Kỹ năng: {self._HTML_skill}, {self._CSS_skill}, {self._Nodejs_skill}, {self._UX}, {self._UI}'
    
    def evaluate(self):
        score_dict = {
            "html_skill": self._HTML_skill,
            "css_skill": self._CSS_skill,
            "nodejs_skill": self._Nodejs_skill,
            "ux_skill": self._UX,
            "ui_skill": self._UI
        }
        score = sum(score_dict.values()) / 5
        if score > 9:
            return "Rất phù hợp"
        elif score > 7:
            return "Phù hợp"
        elif score > 5:
            return "Tạm được"
        elif score > 3:
            skill_under_4 = {key: value for (key, value) in score_dict.items() if value < 4}
            return f"Cần bổ sung thêm kiến thức, kỹ năng: {skill_under_4}"
        else:
            return "Bad"

class FullStack(BackEnd, FrontEnd):
    def __init__(self, job_code, job_name, field_name, salary, sql_skill, oop_skill, api_skill, java_skill, html_skill, css_skill, nodejs_skill, ux_skill, ui_skill):
        BackEnd.__init__(self,job_code, job_name, field_name, salary, sql_skill, oop_skill, api_skill, java_skill)
        FrontEnd.__init__(self, job_code, job_name, field_name, salary, html_skill, css_skill, nodejs_skill, ux_skill, ui_skill)
    
    def __str__(self) -> str:
        return super().__str__() + f', {self._HTML_skill}, {self._CSS_skill}, {self._Nodejs_skill}, {self._UX}, {self._UI}'
    
    def evaluate(self):
        score_dict = {
            "sql_skill": self._Sql_skill,
            "oop_skill": self._OOP_skill,
            "api_skill": self._Api_skill,
            "java_skill": self._Java_skill,
            "html_skill": self._HTML_skill,
            "css_skill": self._CSS_skill,
            "nodejs_skill": self._Nodejs_skill,
            "ux_skill": self._UX,
            "ui_skill": self._UI
        }
        score = sum(score_dict.values()) / 9
        if score > 9:
            return "Rất phù hợp"
        elif score > 7:
            return "Phù hợp"
        elif score > 5:
            return "Tạm được"
        elif score > 3:
            skill_under_4 = {key: value for (key, value) in score_dict.items() if value < 4}
            return f"Cần bổ sung thêm kiến thức, kỹ năng: {skill_under_4}"
        else:
            return "Bad"

if __name__ == '__main__':
    # Create 4 object AI, BackEnd, FrontEnd, FullStack
    ai = AI(1, "AI", "IT", 2000, 10, 1, 1, 2)
    backend = BackEnd(2, "BackEnd", "IT", 1500, 0, 1, 2, 3)
    frontend = FrontEnd(3, "FrontEnd", "IT", 1250, 10, 10, 10, 10, 10)
    fullstack = FullStack(4, "FullStack", "IT", 2500, 10, 10, 10, 10, 10, 10, 10, 10, 10)
    
    print("\n\n")
    print("AI: ", ai.evaluate())
    print(ai)
    print("\n\n")
    print("BackEnd: ", backend.evaluate())
    print(backend)
    print("\n\n")
    print("FrontEnd: ", frontend.evaluate())
    print(frontend)
    print("\n\n")
    print("FullStack: ", fullstack.evaluate())
    print(fullstack)
    print("\n\n")