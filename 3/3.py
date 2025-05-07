def quantity_squares(size_rectangle1, size_rectangle2, side_square):
    s_rectangle = size_rectangle1 * size_rectangle2
    s_square = side_square * side_square
    return print(f'В прямоугольнике размером {size_rectangle1}, {size_rectangle2} получается {s_rectangle / s_square} квадратов со сторонами по {side_square}')
quantity_squares(8, 2, 4)