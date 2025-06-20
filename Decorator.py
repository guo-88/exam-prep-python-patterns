import streamlit as st
import reveal_slides as rs
from functools import wraps

# ======================
# 1. Теоретическая часть (слайды)
# ======================
def show_theory_slides():
    slides_md = """
    ## Паттерн Декоратор (Decorator Pattern)
    ---
    ### Основная концепция
    Динамическое расширение функциональности объектов без изменения их структуры  
    Альтернатива наследованию, соответствует принципу открытости/закрытости
    ---
    ### Компоненты паттерна
   
    Component (абстрактный компонент)
    │
    ├── ConcreteComponent (конкретный компонент)
    │
    └── Decorator (абстрактный декоратор)
        ├── ConcreteDecoratorA (конкретный декоратор)
        └── ConcreteDecoratorB
    
    ---
    ### Преимущества и недостатки
    Преимущества  
    1. Более гибкий чем наследование  
    2. Избегает "взрыва" классов  
    3. Динамическое добавление/удаление функциональности  

    Недостатки  
    1. Множественные декораторы усложняют код  
    2. Небольшие накладные расходы
    ---
    ### Типичные случаи применения
    - Форматирование текста (жирный/цвет/шрифт)
    - Обработка I/O потоков (шифрование/сжатие/кэширование)
    - Веб-мидлвары (аутентификация/логирование)
    """
    
    # Рендеринг слайдов
    rs.slides(
        slides_md,
        height=500,
        theme="serif",
        config={
            "controls": True,
            "progress": True,
            "center": True
        }
    )

# ======================
# 2. Реализация паттерна
# ======================
class TextComponent:
    def render(self) -> str:
        raise NotImplementedError

class PlainText(TextComponent):
    def init(self, text: str):
        self.text = text

    def render(self) -> str:
        return self.text

class TextDecorator(TextComponent):
    def init(self, component: TextComponent):
        self._component = component

class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"{self._component.render()}"

class ColorDecorator(TextDecorator):
    def init(self, component: TextComponent, color: str):
        super().init(component)
        self.color = color

    def render(self) -> str:
        return f'<span style="color:{self.color}">{self._component.render()}</span>'

# ======================
# 3. Интерактивная демонстрация
# ======================
def interactive_demo():
    st.divider()
    st.subheader("Демонстрация работы декораторов")

    col1, col2 = st.columns(2)
    with col1:
        text = st.text_input("Введите текст", "Пример текста")
        bold = st.checkbox("Жирный текст")
    with col2:
        color = st.selectbox("Цвет текста", ["red", "blue", "green", "orange"])
        font_size = st.slider("Размер шрифта", 10, 30, 16)

    # Построение цепочки декораторов
    component = PlainText(text)
    if bold:
        component = BoldDecorator(component)
    component = ColorDecorator(component, color)
    
    # Отображение результата
    st.markdown(
        f'<div style="font-size:{font_size}px">{component.render()}</div>', 
        unsafe_allow_html=True
    )

# ======================
# Основная программа
# ======================
def main():
    st.title("Демонстрация паттерна Декоратор")
    show_theory_slides()  # Показ теоретических слайдов
    interactive_demo()    # Интерактивная демонстрация

if __name__ == "main":
    main()
