from dataclasses import dataclass, field

@dataclass
class Email:
    from_addr: str
    to: list[str]
    subject: str
    cc: list[str] = field(default_factory=list)
    bcc: list[str] = field(default_factory=list)
    text_body: str = ""
    html_body: str = ""
    attachments: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        return (
            f"От: {self.from_addr}\n"
            f"Кому: {', '.join(self.to)}\n"
            f"Тема: {self.subject}\n"
            f"Вложений: {len(self.attachments)}"
        )


class EmailBuilder:
    def __init__(self):
        self._from_addr = None
        self._to = []
        self._cc = []
        self._bcc = []
        self._subject = None
        self._text_body = ""
        self._html_body = ""
        self._attachments = []
    
    def set_from(self, from_addr):
        "Устанавливает отправителя"
        self._from_addr = from_addr
        return self
    
    def add_to(self, to_addr):
        "Добавляет получателя"
        self._to.append(to_addr)
        return self
    
    def add_cc(self, cc_addr):
        "Добавляет получателя в копию"
        self._cc.append(cc_addr)
        return self
    
    def add_bcc(self, bcc_addr):
        "Добавляет получателя в скрытую копию"
        self._bcc.append(bcc_addr)
        return self
    
    def set_subject(self, subject):
        "Устанавливает тему письма"
        self._subject = subject
        return self
    
    def set_text_body(self, text_body):
        "Устанавливает текстовое содержимое"
        self._text_body = text_body
        return self
    
    def set_html_body(self, html_body):
        "Устанавливает HTML содержимое"
        self._html_body = html_body
        return self
    
    def add_attachment(self, attachment):
        "Добавляет вложение"
        self._attachments.append(attachment)
        return self
    
    def build(self):
        "Собирает и возвращает объект Email"
        if not self._from_addr:
            raise ValueError("Отправитель (from_addr) обязателен")
        if not self._to:
            raise ValueError("Хотя бы один получатель (to) обязателен")
        if not self._subject:
            raise ValueError("Тема (subject) обязательна")
        
        return Email(
            from_addr=self._from_addr,
            to=self._to,
            subject=self._subject,
            cc=self._cc,
            bcc=self._bcc,
            text_body=self._text_body,
            html_body=self._html_body,
            attachments=self._attachments
        )


class Director:
    def __init__(self, builder):
        "Принимает экземпляр EmailBuilder"
        self._builder = builder
    
    def build_welcome_email(self, to_addr, username):
        "Строит приветственное письмо"
        return (
            self._builder
            .set_from("welcome@company.com")
            .add_to(to_addr)
            .set_subject(f"Добро пожаловать, {username}!")
            .set_text_body(f"Здравствуйте, {username}!\n\nРады приветствовать вас в нашем сервисе.")
            .set_html_body(f"<h1>Здравствуйте, {username}!</h1><p>Рады приветствовать вас в нашем сервисе.</p>")
            .build()
        )
    
    def build_password_reset_email(self, to_addr, reset_link):
        "Строит письмо для сброса пароля"
        return (
            self._builder
            .set_from("security@company.com")
            .add_to(to_addr)
            .set_subject("Сброс пароля")
            .set_text_body(f"Для сброса пароля перейдите по ссылке: {reset_link}\n\nСсылка действительна в течение 1 часа.")
            .set_html_body(f"<p>Для сброса пароля перейдите по ссылке: <a href='{reset_link}'>{reset_link}</a></p><p>Ссылка действительна в течение 1 часа.</p>")
            .build()
        )


# Клиентский код
print("=== Приветственное письмо ===")
director = Director(EmailBuilder())
email = director.build_welcome_email("user@example.com", "Иван")
print(email)
print()

print("=== Письмо для сброса пароля ===")
director2 = Director(EmailBuilder())
reset_email = director2.build_password_reset_email("user@example.com", "https://example.com/reset?token=abc123")
print(reset_email)
print()

print("=== Произвольное письмо ===")
custom_email = (
    EmailBuilder()
    .set_from("noreply@company.com")
    .add_to("client@example.com")
    .add_cc("manager@company.com")
    .set_subject("Ваш счёт №1234")
    .set_html_body("<h1>Счёт</h1>")
    .add_attachment("invoice_1234.pdf")
    .build()
)
print(custom_email)
print()

# Проверка валидации
print("=== Проверка валидации ===")
try:
    invalid_email = EmailBuilder().set_from("test@test.com").build()
except ValueError as e:
    print(f"Ошибка: {e}")