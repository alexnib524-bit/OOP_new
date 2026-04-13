from abc import ABC, abstractmethod

# Интерфейсы продуктов
class Toast(ABC):
    @abstractmethod
    def show(self, message: str) -> None:
        pass

class Dialog(ABC):
    @abstractmethod
    def show(self, title: str, body: str, buttons: list[str]) -> None:
        pass

class ProgressBar(ABC):
    @abstractmethod
    def show(self, label: str, value: int) -> None:
        pass

# Конкретные продукты для iOS
class IOSToast(Toast):
    def show(self, message: str) -> None:
        print(f"[iOS Toast] {message}")

class IOSDialog(Dialog):
    def show(self, title: str, body: str, buttons: list[str]) -> None:
        print(f"[iOS Dialog] {title}")
        print(f"             {body}")
        print(f"             Кнопки: {', '.join(buttons)}")

class IOSProgressBar(ProgressBar):
    def show(self, label: str, value: int) -> None:
        bar_length = 20
        filled = int(bar_length * value / 100)
        bar = "#" * filled + "-" * (bar_length - filled)
        print(f"[iOS Progress] {label}: [{bar}] {value}%")

# Конкретные продукты для Android
class AndroidToast(Toast):
    def show(self, message: str) -> None:
        print(f"[Android Toast] {message}")

class AndroidDialog(Dialog):
    def show(self, title: str, body: str, buttons: list[str]) -> None:
        print(f"[Android Dialog] {title}")
        print(f"                 {body}")
        print(f"                 Кнопки: {', '.join(buttons)}")

class AndroidProgressBar(ProgressBar):
    def show(self, label: str, value: int) -> None:
        bar_length = 20
        filled = int(bar_length * value / 100)
        bar = "#" * filled + "-" * (bar_length - filled)
        print(f"[Android Progress] {label}: [{bar}] {value}%")

# Абстрактная фабрика
class NotificationFactory(ABC):
    @abstractmethod
    def create_toast(self) -> Toast:
        pass

    @abstractmethod
    def create_dialog(self) -> Dialog:
        pass

    @abstractmethod
    def create_progress_bar(self) -> ProgressBar:
        pass

# Конкретная фабрика для iOS
class IOSFactory(NotificationFactory):
    def create_toast(self) -> Toast:
        return IOSToast()

    def create_dialog(self) -> Dialog:
        return IOSDialog()

    def create_progress_bar(self) -> ProgressBar:
        return IOSProgressBar()

# Конкретная фабрика для Android
class AndroidFactory(NotificationFactory):
    def create_toast(self) -> Toast:
        return AndroidToast()

    def create_dialog(self) -> Dialog:
        return AndroidDialog()

    def create_progress_bar(self) -> ProgressBar:
        return AndroidProgressBar()

# Клиентский код — не зависит от платформы
def show_upload_progress(factory: NotificationFactory, filename: str, progress: int):
    toast = factory.create_toast()
    bar = factory.create_progress_bar()

    toast.show(f"Загрузка {filename} начата")
    bar.show("Прогресс загрузки", progress)

    if progress == 100:
        dialog = factory.create_dialog()
        dialog.show("Готово", f"{filename} успешно загружен", ["OK"])
