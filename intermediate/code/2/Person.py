class Person:
    def __init__(self, name: str, id: str, age: int) -> None:
        self._name = name
        self._id = id
        self.age = age

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> str:
        return self._id
    
    @property
    def age(self) -> int:
        return self._age

    @name.setter
    def set_name(self, new_name) -> None:
        self._name = new_name

    @id.setter
    def set_id(self, id) -> None:
        self._id = id

    @age.setter
    def set_age(self, age) -> None:
        self._age = age

    def __str__(self) -> str:
        return(f'name: {self.name} id: {self.id} age: {self.age}')