class Pizza:
    def __init__(self):
        self.size: str = ""
        self.dough: str = ""
        self.sauce: str = ""
        self.cheese: str = ""
        self.toppings: list[str] = []

    def __str__(self) -> str:
        toppings = ', '.join(self.toppings) if self.toppings else 'без топпингов'
        return (
            f"Пицца {self.size} на {self.dough} тесте\n"
            f"Соус: {self.sauce}, Сыр: {self.cheese}\n"
            f"Топпинги: {toppings}"
        )


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size: str):
        self.pizza.size = size
        return self
    
    def set_dough(self, dough: str):
        self.pizza.dough = dough
        return self
    
    def set_sauce(self, sauce: str):
        self.pizza.sauce = sauce
        return self
    
    def set_cheese(self, cheese: str):
        self.pizza.cheese = cheese
        return self
    
    def add_topping(self, topping: str):
        self.pizza.toppings.append(topping)
        return self
    
    def build(self) -> Pizza:
        if not self.pizza.size or not self.pizza.dough:
            raise ValueError("Обязательные параметры (размер и тесто) должны быть указаны")
        return self.pizza


class Director:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder
    
    def build_margherita(self) -> Pizza:
        return (self.builder
                .set_size("M")
                .set_dough("традиционное")
                .set_sauce("томатный")
                .set_cheese("моцарелла")
                .build())
    
    def build_pepperoni(self) -> Pizza:
        return (self.builder
                .set_size("L")
                .set_dough("традиционное")
                .set_sauce("томатный")
                .set_cheese("моцарелла")
                .add_topping("пепперони")
                .build())
    
    def build_vegetarian(self) -> Pizza:
        return (self.builder
                .set_size("M")
                .set_dough("тонкое")
                .set_sauce("песто")
                .set_cheese("пармезан")
                .add_topping("перец")
                .add_topping("грибы")
                .add_topping("оливки")
                .build())


# Ожидаемый клиентский код:
director = Director(PizzaBuilder())
print(director.build_margherita())
print(director.build_pepperoni())

# Произвольная пицца без директора:
pizza = PizzaBuilder().set_size("L").set_dough("тонкое").add_topping("грибы").build()
print(pizza)