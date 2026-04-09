from abc import ABC, abstractmethod

# Продукты
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Input(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# Конкретные продукты для светлой темы
class LightButton(Button):
    def render(self) -> str:
        return "[Light Button]"

class LightCheckbox(Checkbox):
    def render(self) -> str:
        return "[Light Checkbox]"

class LightInput(Input):
    def render(self) -> str:
        return "[Light Input]"

# Конкретные продукты для тёмной темы
class DarkButton(Button):
    def render(self) -> str:
        return "[Dark Button]"

class DarkCheckbox(Checkbox):
    def render(self) -> str:
        return "[Dark Checkbox]"

class DarkInput(Input):
    def render(self) -> str:
        return "[Dark Input]"

# Абстрактная фабрика
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass
    
    @abstractmethod
    def create_input(self) -> Input:
        pass

# Конкретные фабрики
class LightThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()
    
    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()
    
    def create_input(self) -> Input:
        return LightInput()

class DarkThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()
    
    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()
    
    def create_input(self) -> Input:
        return DarkInput()

# Клиентский код
class Application:
    def __init__(self, factory: UIFactory):
        self.factory = factory
    
    def render_ui(self):
        btn = self.factory.create_button()
        chk = self.factory.create_checkbox()
        inp = self.factory.create_input()
        print(btn.render(), chk.render(), inp.render())

# Использование
if __name__ == "__main__":
    # Светлая тема
    light_factory = LightThemeFactory()
    app_light = Application(light_factory)
    app_light.render_ui()
    
    # Тёмная тема
    dark_factory = DarkThemeFactory()
    app_dark = Application(dark_factory)
    app_dark.render_ui()