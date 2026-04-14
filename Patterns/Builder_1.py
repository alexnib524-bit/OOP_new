from typing import List, Dict, Optional


class Resume:
    """Класс резюме, создаваемый через строителя"""
    def __init__(
        self,
        name: str,
        email: str,
        phone: str = "",
        summary: str = "",
        experience: list[dict] = None,
        education: list[dict] = None,
        skills: list[str] = None,
        languages: list[str] = None,
        certifications: list[str] = None,
    ):
        self.name = name
        self.email = email
        self.phone = phone
        self.summary = summary
        self.experience = experience or []
        self.education = education or []
        self.skills = skills or []
        self.languages = languages or []
        self.certifications = certifications or []

    def __str__(self) -> str:
        result = [
            f"\n{'='*50}",
            f"=== {self.name} ===",
            f"Email: {self.email}",
            f"Телефон: {self.phone}" if self.phone else "",
            f"О себе: {self.summary}" if self.summary else "",
            f"\n--- Навыки ---",
            f"{', '.join(self.skills)}" if self.skills else "Не указаны",
            f"\n--- Опыт работы ---",
        ]
        for exp in self.experience:
            result.append(f"  • {exp.get('company', '')} — {exp.get('years', '')} лет: {exp.get('position', '')}")
        
        result.append("\n--- Образование ---")
        for edu in self.education:
            result.append(f"  • {edu.get('degree', '')} — {edu.get('school', '')}")
        
        if self.languages:
            result.append(f"\n--- Языки ---\n{', '.join(self.languages)}")
        if self.certifications:
            result.append(f"\n--- Сертификаты ---\n{', '.join(self.certifications)}")
        
        return "\n".join(filter(None, result))


class ResumeBuilder:
    """Строитель для пошагового создания резюме"""
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._name = ""
        self._email = ""
        self._phone = ""
        self._summary = ""
        self._experience = []
        self._education = []
        self._skills = []
        self._languages = []
        self._certifications = []
        return self
    
    def set_name(self, name: str):
        self._name = name
        return self
    
    def set_contacts(self, email: str, phone: str = ""):
        self._email = email
        self._phone = phone
        return self
    
    def set_summary(self, summary: str):
        self._summary = summary
        return self
    
    def add_experience(self, company: str, years: int, position: str = ""):
        self._experience.append({"company": company, "years": years, "position": position})
        return self
    
    def add_education(self, degree: str, school: str, year: int = 0):
        self._education.append({"degree": degree, "school": school, "year": year})
        return self
    
    def add_skill(self, skill: str):
        self._skills.append(skill)
        return self
    
    def add_language(self, language: str):
        self._languages.append(language)
        return self
    
    def add_certification(self, certification: str):
        self._certifications.append(certification)
        return self
    
    def build(self) -> Resume:
        """Возвращает готовый объект Resume"""
        return Resume(
            name=self._name,
            email=self._email,
            phone=self._phone,
            summary=self._summary,
            experience=self._experience,
            education=self._education,
            skills=self._skills,
            languages=self._languages,
            certifications=self._certifications,
        )


class ResumeDirector:
    """Директор для создания стандартных конфигураций резюме"""
    
    @staticmethod
    def build_standard_resume(builder: ResumeBuilder, name: str, email: str) -> Resume:
        """Стандартное резюме: имя, контакты, базовые навыки"""
        return (builder
            .reset()
            .set_name(name)
            .set_contacts(email)
            .add_skill("Коммуникабельность")
            .add_skill("Работа в команде")
            .add_skill("Ответственность")
            .build()
        )
    
    @staticmethod
    def build_extended_resume(
        builder: ResumeBuilder, 
        name: str, 
        email: str, 
        phone: str,
        company: str,
        years: int,
        degree: str,
        school: str
    ) -> Resume:
        """Расширенное резюме: имя, контакты, опыт, образование, навыки, языки, сертификаты"""
        return (builder
            .reset()
            .set_name(name)
            .set_contacts(email, phone)
            .set_summary(f"Опытный специалист с {years}+ годами опыта в {company}")
            .add_experience(company, years, "Senior Developer")
            .add_education(degree, school, 2020)
            .add_skill("Python")
            .add_skill("SQL")
            .add_skill("Docker")
            .add_skill("Git")
            .add_language("Английский (B2)")
            .add_language("Немецкий (A2)")
            .add_certification("AWS Certified Developer")
            .add_certification("Kubernetes Basics")
            .build()
        )
