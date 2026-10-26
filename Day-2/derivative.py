def derivative(function , x , h = 0.01):
    rise = function(x + h) - function(x)
    run = h

    return float(rise / run)

def square(x):
    return x ** 2

def loss(w):
    return (2 * w - 6)**2

for h in [1e-2, 1e-5, 1e-8, 1e-12, 1e-15]:
    print(f"slope : h = {h:.0e} : {derivative(square, 3, h):05f}")

print(f"slope at loss function at x = 1 : {derivative(loss , 1)}")
print(f"slope at loss function at x = 5 : {derivative(loss , 5)}")