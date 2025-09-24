def area_rectangle(x, y):
    return x * y

def area_square(x):
    return x * x

def area_circle(x):
    return 3.14 * x * x

def calculate_area(shape, x, y=0):
    area_funcs = {
        "rectangle": lambda x, y: area_rectangle(x, y),
        "square": lambda x, y=0: area_square(x),
        "circle": lambda x, y=0: area_circle(x)
    }
    if shape in area_funcs:
        return area_funcs[shape](x, y)
    else:
        raise ValueError(f"Unknown shape: {shape}")

print(calculate_area("rectangle",5,3))
print(calculate_area("square",4))
print(calculate_area("circle",2))