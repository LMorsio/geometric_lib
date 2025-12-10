## Документация по функциям
### Модуль `circle.py`
#### Применение
```python
>>> from geometric_lib import circle
```
#### `area(r)`
Возвращает площадь круга радиуса `r`.
```python
>>> circle.area(5)
78.53981633974483
```
#### `perimeter(r)`
Возвращает длину окружности (периметр) круга радиуса `r`.
```python
>>> circle.perimeter(5) 
31.41592653589793
```
#### `diameter(r)`
Возвращает диаметр круга радиуса `r`.
```python
>>> circle.diameter(5) 
10
```
---
### Модуль `rectangle.py`
#### Применение
```python
>>> from geometric_lib import rectangle 
```
#### `area(a, b)`
Возвращает площадь прямоугольника со сторонами `a` и `b`.
```python
>>> rectangle.area(3, 4)
12
```
#### `perimeter(a, b)`
Возвращает периметр прямоугольника.
```python
>>> rectangle.perimeter(3, 4)
14
```
#### `diagonal(a, b)`
Возвращает диагональ прямоугольника.
```python
>>> rectangle.diagonal(3, 4)
5.0
```
---
### Модуль `square.py`
#### Применение
```python
>>> from geometric_lib import square
```
#### `area(a)`
Возвращает площадь квадрата со стороной `a`.
```python
>>> square.area(5) 
25
```
#### `perimeter(a)`
Возвращает периметр квадрата.
```python
>>> square.perimeter(5)
20
```
#### `diagonal(a)`
Возвращает диагональ квадрата.
```python
>>> square.diagonal(5) 
7.0710678118654755
```
---
### Модуль `triangle.py`
#### Применение
```python
>>> from geometric_lib import triangle
```
#### `area(a, h)`
Возвращает площадь треугольника по основанию `a` и высоте `h`.
```python
>>> triangle.area(6, 4) 
12.0
```
#### `perimeter(a, b, c)`
Возвращает периметр треугольника по трём сторонам.
```python
>>> triangle.perimeter(3, 4, 5)
12
```