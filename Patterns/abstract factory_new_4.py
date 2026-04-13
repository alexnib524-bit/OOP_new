from abc import ABC, abstractmethod

# Интерфейсы продуктов
class Header(ABC):
    @abstractmethod
    def render(self, title: str, subtitle: str) -> str:
        pass

class Table(ABC):
    @abstractmethod
    def render(self, headers: list[str], rows: list[list]) -> str:
        pass

class Footer(ABC):
    @abstractmethod
    def render(self, text: str, page: int) -> str:
        pass

# Конкретные продукты для PDF
class PdfHeader(Header):
    def render(self, title: str, subtitle: str) -> str:
        return f"PDF Header: {title} - {subtitle}\n"

class PdfTable(Table):
    def render(self, headers: list[str], rows: list[list]) -> str:
        result = "PDF Table:\n"
        result += " | ".join(headers) + "\n"
        result += "-" * 30 + "\n"
        for row in rows:
            result += " | ".join(str(cell) for cell in row) + "\n"
        return result

class PdfFooter(Footer):
    def render(self, text: str, page: int) -> str:
        return f"PDF Footer: {text}, Page {page}\n"

# Конкретные продукты для DOCX
class DocxHeader(Header):
    def render(self, title: str, subtitle: str) -> str:
        return f"DOCX Header: {title} - {subtitle}\n"

class DocxTable(Table):
    def render(self, headers: list[str], rows: list[list]) -> str:
        result = "DOCX Table:\n"
        for header in headers:
            result += f"[{header}] "
        result += "\n"
        for row in rows:
            for cell in row:
                result += f"{cell} "
            result += "\n"
        return result

class DocxFooter(Footer):
    def render(self, text: str, page: int) -> str:
        return f"DOCX Footer: {text}, Page {page}\n"

# Интерфейс фабрики
class DocumentFactory(ABC):
    @abstractmethod
    def create_header(self) -> Header:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass

    @abstractmethod
    def create_footer(self) -> Footer:
        pass

# Конкретная фабрика для PDF
class PdfFactory(DocumentFactory):
    def create_header(self) -> Header:
        return PdfHeader()

    def create_table(self) -> Table:
        return PdfTable()

    def create_footer(self) -> Footer:
        return PdfFooter()

# Конкретная фабрика для DOCX
class DocxFactory(DocumentFactory):
    def create_header(self) -> Header:
        return DocxHeader()

    def create_table(self) -> Table:
        return DocxTable()

    def create_footer(self) -> Footer:
        return DocxFooter()

# Клиентский код
def build_sales_report(factory: DocumentFactory, data: list[list]) -> str:
    header = factory.create_header()
    table = factory.create_table()
    footer = factory.create_footer()

    result = header.render("Отчёт о продажах", "Квартал 1, 2025")
    result += table.render(["Продукт", "Количество", "Сумма"], data)
    result += footer.render("Конфиденциально", 1)
    return result
