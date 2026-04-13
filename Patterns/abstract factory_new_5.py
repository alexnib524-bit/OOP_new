from abc import ABC, abstractmethod

# Интерфейсы продуктов
class Hero(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass

    @abstractmethod
    def attack(self, weapon) -> str:
        pass

class Enemy(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass

    @abstractmethod
    def health(self) -> int:
        pass

class Weapon(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def damage(self) -> int:
        pass

# Конкретные продукты для Fantasy мира
class FantasyHero(Hero):
    def describe(self) -> str:
        return "Рыцарь в сверкающих доспехах с благородным сердцем"
    
    def attack(self, weapon) -> str:
        return f"Рыцарь наносит удар {weapon.name()} нанося {weapon.damage()} урона!"

class FantasyEnemy(Enemy):
    def describe(self) -> str:
        return "Огнедышащий дракон с чешуёй как сталь"
    
    def health(self) -> int:
        return 200

class FantasyWeapon(Weapon):
    def name(self) -> str:
        return "Волшебный меч-кладенец"
    
    def damage(self) -> int:
        return 45

# Конкретные продукты для SciFi мира
class SciFiHero(Hero):
    def describe(self) -> str:
        return "Космодесантник в силовой броне с имплантами"
    
    def attack(self, weapon) -> str:
        return f"Космодесантник стреляет из {weapon.name()} нанося {weapon.damage()} урона!"

class SciFiEnemy(Enemy):
    def describe(self) -> str:
        return "Боевой робот с лазерными пушками и броней из титана"
    
    def health(self) -> int:
        return 250

class SciFiWeapon(Weapon):
    def name(self) -> str:
        return "Лазерная винтовка"
    
    def damage(self) -> int:
        return 60

# Интерфейс фабрики
class WorldFactory(ABC):
    @abstractmethod
    def create_hero(self) -> Hero:
        pass
    
    @abstractmethod
    def create_enemy(self) -> Enemy:
        pass
    
    @abstractmethod
    def create_weapon(self) -> Weapon:
        pass

# Конкретная фабрика для Fantasy мира
class FantasyWorldFactory(WorldFactory):
    def create_hero(self) -> Hero:
        return FantasyHero()
    
    def create_enemy(self) -> Enemy:
        return FantasyEnemy()
    
    def create_weapon(self) -> Weapon:
        return FantasyWeapon()

# Конкретная фабрика для SciFi мира
class SciFiWorldFactory(WorldFactory):
    def create_hero(self) -> Hero:
        return SciFiHero()
    
    def create_enemy(self) -> Enemy:
        return SciFiEnemy()
    
    def create_weapon(self) -> Weapon:
        return SciFiWeapon()

# Клиентский код
def create_world(factory: WorldFactory):
    hero = factory.create_hero()
    enemy = factory.create_enemy()
    weapon = factory.create_weapon()

    print(f"Герой: {hero.describe()}")
    print(f"Враг: {enemy.describe()}")
    print(f"Здоровье врага: {enemy.health()}")
    print(hero.attack(weapon))
