class SelectQueryBuilder:
    def __init__(self):
        self._table = None
        self._columns = []
        self._joins = []
        self._where_conditions = []
        self._order_by_column = None
        self._order_by_direction = None
        self._limit_value = None
        self._offset_value = None
    
    def from_table(self, table):
        self._table = table
        return self
    
    def select(self, *columns):
        self._columns = list(columns)
        return self
    
    def join(self, table, condition):
        self._joins.append((table, condition))
        return self
    
    def where(self, condition):
        self._where_conditions.append(condition)
        return self
    
    def order_by(self, column, direction="ASC"):
        self._order_by_column = column
        self._order_by_direction = direction.upper()
        return self
    
    def limit(self, limit):
        self._limit_value = limit
        return self
    
    def offset(self, offset):
        self._offset_value = offset
        return self
    
    def build(self):
        if not self._table:
            raise ValueError("FROM clause is required")
        
        # SELECT часть
        if self._columns:
            select_clause = f"SELECT {', '.join(self._columns)}"
        else:
            select_clause = "SELECT *"
        
        # FROM часть
        from_clause = f"FROM {self._table}"
        
        # JOIN части
        join_clauses = []
        for table, condition in self._joins:
            join_clauses.append(f"JOIN {table} ON {condition}")
        
        # WHERE часть
        if self._where_conditions:
            where_clause = f"WHERE {' AND '.join(self._where_conditions)}"
        else:
            where_clause = None
        
        # ORDER BY часть
        if self._order_by_column:
            order_clause = f"ORDER BY {self._order_by_column} {self._order_by_direction}"
        else:
            order_clause = None
        
        # LIMIT и OFFSET
        limit_offset_clause = None
        if self._limit_value is not None:
            if self._offset_value is not None:
                limit_offset_clause = f"LIMIT {self._limit_value} OFFSET {self._offset_value}"
            else:
                limit_offset_clause = f"LIMIT {self._limit_value}"
        elif self._offset_value is not None:
            limit_offset_clause = f"OFFSET {self._offset_value}"
        
        # Сборка запроса
        parts = [select_clause, from_clause]
        parts.extend(join_clauses)
        
        if where_clause:
            parts.append(where_clause)
        
        if order_clause:
            parts.append(order_clause)
        
        if limit_offset_clause:
            parts.append(limit_offset_clause)
        
        return "\n".join(parts)


# Клиентский код
sql = (
    SelectQueryBuilder()
    .from_table("orders")
    .select("id", "total", "status")
    .join("users", "orders.user_id = users.id")
    .where("status = 'new'")
    .where("total > 1000")
    .order_by("created_at", "DESC")
    .limit(10)
    .offset(20)
    .build()
)
print(sql)
print()

# Минимальный запрос
sql_min = SelectQueryBuilder().from_table("products").build()
print(sql_min)