from abc import ABC, abstractmethod

# Интерфейсы продуктов
class Connection(ABC):
    @abstractmethod
    def connect(self, dsn: str) -> None: pass

    @abstractmethod
    def close(self) -> None: pass

class QueryBuilder(ABC):
    @abstractmethod
    def select(self, table: str, columns: list[str]) -> str: pass

    @abstractmethod
    def where(self, condition: str) -> str: pass

class Transaction(ABC):
    @abstractmethod
    def begin(self) -> None: pass

    @abstractmethod
    def commit(self) -> None: pass

    @abstractmethod
    def rollback(self) -> None: pass

# Конкретные продукты для MySQL
class MySQLConnection(Connection):
    def connect(self, dsn: str) -> None:
        print(f"MySQL: Подключение к {dsn}")
    
    def close(self) -> None:
        print("MySQL: Соединение закрыто")

class MySQLQueryBuilder(QueryBuilder):
    def select(self, table: str, columns: list[str]) -> str:
        cols = ", ".join(columns)
        return f"SELECT {cols} FROM {table}"
    
    def where(self, condition: str) -> str:
        return f"WHERE {condition}"

class MySQLTransaction(Transaction):
    def begin(self) -> None:
        print("MySQL: Начало транзакции (START TRANSACTION)")
    
    def commit(self) -> None:
        print("MySQL: Фиксация транзакции (COMMIT)")
    
    def rollback(self) -> None:
        print("MySQL: Откат транзакции (ROLLBACK)")

# Конкретные продукты для PostgreSQL
class PostgreSQLConnection(Connection):
    def connect(self, dsn: str) -> None:
        print(f"PostgreSQL: Подключение к {dsn}")
    
    def close(self) -> None:
        print("PostgreSQL: Соединение закрыто")

class PostgreSQLQueryBuilder(QueryBuilder):
    def select(self, table: str, columns: list[str]) -> str:
        cols = ", ".join(columns)
        return f'SELECT {cols} FROM "{table}"'
    
    def where(self, condition: str) -> str:
        return f"WHERE {condition}"

class PostgreSQLTransaction(Transaction):
    def begin(self) -> None:
        print("PostgreSQL: Начало транзакции (BEGIN)")
    
    def commit(self) -> None:
        print("PostgreSQL: Фиксация транзакции (COMMIT)")
    
    def rollback(self) -> None:
        print("PostgreSQL: Откат транзакции (ROLLBACK)")

# Интерфейс абстрактной фабрики
class DatabaseFactory(ABC):
    @abstractmethod
    def create_connection(self) -> Connection: pass
    
    @abstractmethod
    def create_query_builder(self) -> QueryBuilder: pass
    
    @abstractmethod
    def create_transaction(self) -> Transaction: pass

# Конкретные фабрики
class MySQLFactory(DatabaseFactory):
    def create_connection(self) -> Connection:
        return MySQLConnection()
    
    def create_query_builder(self) -> QueryBuilder:
        return MySQLQueryBuilder()
    
    def create_transaction(self) -> Transaction:
        return MySQLTransaction()

class PostgreSQLFactory(DatabaseFactory):
    def create_connection(self) -> Connection:
        return PostgreSQLConnection()
    
    def create_query_builder(self) -> QueryBuilder:
        return PostgreSQLQueryBuilder()
    
    def create_transaction(self) -> Transaction:
        return PostgreSQLTransaction()

# Клиентский код
def run_query(factory: DatabaseFactory):
    conn = factory.create_connection()
    qb = factory.create_query_builder()
    tx = factory.create_transaction()

    conn.connect("host=localhost dbname=shop")
    tx.begin()
    sql = qb.select("orders", ["id", "total"]) + " " + qb.where("status = 'new'")
    print(f"Запрос: {sql}")
    tx.commit()
    conn.close()
