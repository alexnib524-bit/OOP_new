<?php

// Класс Resume
class Resume {
    public function __construct(
        public readonly string $name,
        public readonly string $email,
        public readonly string $phone = '',
        public readonly string $summary = '',
        public readonly array  $experience = [],
        public readonly array  $education = [],
        public readonly array  $skills = [],
        public readonly array  $languages = [],
        public readonly array  $certifications = [],
    ) {}

    public function __toString(): string {
        return sprintf(
            "=== %s ===\nEmail: %s\nНавыки: %s\nОпыт: %d позиций",
            $this->name,
            $this->email,
            implode(', ', $this->skills),
            count($this->experience)
        );
    }
}

// Строитель для резюме
class ResumeBuilder {
    private string $name = '';
    private string $email = '';
    private string $phone = '';
    private string $summary = '';
    private array $experience = [];
    private array $education = [];
    private array $skills = [];
    private array $languages = [];
    private array $certifications = [];
    
    public function set_name(string $name): self {
        $this->name = $name;
        return $this;
    }
    
    public function set_contacts(string $email, string $phone = ''): self {
        $this->email = $email;
        $this->phone = $phone;
        return $this;
    }
    
    public function add_experience(string $company, int $years, string $position = ''): self {
        $this->experience[] = [
            'company' => $company,
            'years' => $years,
            'position' => $position
        ];
        return $this;
    }
    
    public function add_education(string $degree, string $school, int $year = 0): self {
        $this->education[] = [
            'degree' => $degree,
            'school' => $school,
            'year' => $year
        ];
        return $this;
    }
    
    public function add_skill(string $skill): self {
        $this->skills[] = $skill;
        return $this;
    }
    
    public function add_language(string $language, string $level = ''): self {
        $this->languages[] = [
            'language' => $language,
            'level' => $level
        ];
        return $this;
    }
    
    public function add_certification(string $certification): self {
        $this->certifications[] = $certification;
        return $this;
    }
    
    public function set_summary(string $summary): self {
        $this->summary = $summary;
        return $this;
    }
    
    public function build(): Resume {
        // Проверка обязательных полей
        if (empty($this->name)) {
            throw new Exception("Имя обязательно для резюме");
        }
        if (empty($this->email)) {
            throw new Exception("Email обязателен для резюме");
        }
        
        return new Resume(
            name: $this->name,
            email: $this->email,
            phone: $this->phone,
            summary: $this->summary,
            experience: $this->experience,
            education: $this->education,
            skills: $this->skills,
            languages: $this->languages,
            certifications: $this->certifications
        );
    }
}

// Директор для сборки стандартных резюме
class Director {
    private ResumeBuilder $builder;
    
    public function __construct(ResumeBuilder $builder) {
        $this->builder = $builder;
    }
    
    // Стандартное резюме
    public function buildStandardResume(string $name, string $email): Resume {
        return $this->builder
            ->set_name($name)
            ->set_contacts($email)
            ->add_skill('Коммуникабельность')
            ->add_skill('Работа в команде')
            ->add_skill('Ответственность')
            ->set_summary('Молодой специалист с желанием развиваться')
            ->build();
    }
    
    // Расширенное резюме (с опытом и образованием)
    public function buildExtendedResume(
        string $name, 
        string $email, 
        string $phone,
        string $summary
    ): Resume {
        return $this->builder
            ->set_name($name)
            ->set_contacts($email, $phone)
            ->set_summary($summary)
            ->add_skill('Python')
            ->add_skill('SQL')
            ->add_skill('Docker')
            ->add_skill('Git')
            ->add_experience('Яндекс', 3, 'Разработчик')
            ->add_experience('Google', 1, 'Стажёр')
            ->add_education('Бакалавр', 'МГУ', 2020)
            ->add_education('Магистр', 'МФТИ', 2022)
            ->add_language('Английский', 'B2')
            ->add_language('Немецкий', 'A2')
            ->add_certification('AWS Practitioner')
            ->build();
    }
}

// Клиентский код

echo "=== Стандартное резюме ===\n";
$builder = new ResumeBuilder();
$director = new Director($builder);
$standardResume = $director->buildStandardResume('Анна Иванова', 'anna@example.com');
echo $standardResume . "\n\n";

echo "=== Расширенное резюме ===\n";
$builder2 = new ResumeBuilder();
$director2 = new Director($builder2);
$extendedResume = $director2->buildExtendedResume(
    'Петр Сидоров',
    'petr@example.com',
    '+7-900-123-45-67',
    'Опытный разработчик с 5-летним стажем'
);
echo $extendedResume . "\n\n";

echo "=== Ручное построение резюме через билдер ===\n";
$customResume = (new ResumeBuilder())
    ->set_name('Мария Петрова')
    ->set_contacts('maria@example.com', '+7-901-234-56-78')
    ->add_experience('Сбербанк', 2, 'Аналитик')
    ->add_education('Бакалавр', 'ВШЭ', 2019)
    ->add_skill('SQL')
    ->add_skill('Tableau')
    ->add_skill('Excel')
    ->add_language('Английский', 'C1')
    ->set_summary('Аналитик данных с опытом работы в крупной компании')
    ->build();

echo $customResume . "\n\n";

// Проверка валидации
echo "=== Проверка валидации ===\n";
try {
    $invalidResume = (new ResumeBuilder())
        ->set_name('Тест')
        ->build(); // Нет email
} catch (Exception $e) {
    echo "Ошибка: " . $e->getMessage() . "\n";
}