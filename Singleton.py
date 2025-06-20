import streamlit as st
import reveal_slides as rs
from threading import Lock


# 1. Реализация Singleton через декоратор
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

# 2. Добавляем слайды с теорией
def show_singleton_slides():
    slides_content = """
    ## Паттерн Singleton
    ---
    ### Тип паттерна
    - Порождающий паттерн
    - Гарантирует единственный экземпляр класса
    - Предоставляет глобальную точку доступа
    
    ---
    ### Базовая структура
       classDiagram
        class Singleton {
            -static instance
            +getInstance() Singleton
        }
    ---
    ### Типичные случаи применения
    - Пул соединений с БД
    - Менеджер конфигураций
    - Логгер приложения
    - Кэш данных
    
    ---
    ### Способы реализации в Python
    1. Модульный уровень
    2. Метод __new__
    3. Декоратор
    4. Мета-классы
    """
    
    rs.slides(
        slides_content,
        height=500,
        theme="night",
        config={
            "controls": True,
            "progress": True,
            "center": True
        }
    )

# 3. Практический пример - пул соединений БД
class DatabaseConnectionPool:
    def __init__(self):
        self.connections = {}
        st.write("Инициализирован пул соединений (выполняется один раз)")
    
    def add_connection(self, name, conn_str):
        self.connections[name] = conn_str
    
    def get_connection(self, name):
        return self.connections.get(name)

def main():
    st.title("Демонстрация паттерна Singleton")
    
    # Показываем теоретические слайды
    st.header("1. Теория паттерна Singleton")
    show_singleton_slides()
    
    # Практическая демонстрация
    st.header("2. Пример с пулом соединений БД")
    
    db_pool1 = DatabaseConnectionPool()
    db_pool1.add_connection("master", "mysql://master:3306")
    
    db_pool2 = DatabaseConnectionPool()
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Операции с экземпляром 1")
        db_pool1.add_connection("backup", "mysql://backup:3306")
    
    with col2:
        st.subheader("Просмотр через экземпляр 2")
        st.write("Все соединения:", db_pool2.connections)
    
    st.success(f"Это один и тот же экземпляр: {db_pool1 is db_pool2}")

if __name__ == "__main__":
    main()
