import pickle

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, initial_weights=None):
        if initial_weights and len(initial_weights) == input_size + 1:
            self.weights = initial_weights
        else:
            self.weights = [0.0] * (input_size + 1)  # +1 для bias
        self.learning_rate = learning_rate

    def predict(self, x):
        x_with_bias = [1] + x
        summation = sum(w * xi for w, xi in zip(self.weights, x_with_bias))
        return 1 if summation > 0 else 0

    def train(self, X, y, epochs=10):
        for _ in range(epochs):
            for xi, target in zip(X, y):
                x_with_bias = [1] + xi
                prediction = self.predict(xi)
                error = target - prediction
                for i in range(len(self.weights)):
                    self.weights[i] += self.learning_rate * error * x_with_bias[i]

    def save_weights(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.weights, f)

    def load_weights(self, filename):
        with open(filename, 'rb') as f:
            self.weights = pickle.load(f)

def input_weights(size):
    print(f"Введите {size} весов (включая bias) через пробел, или нажмите Enter для инициализации нулями:")
    line = input().strip()
    if not line:
        return None
    parts = line.split()
    if len(parts) != size:
        print(f"Ошибка: ожидается {size} чисел, получено {len(parts)}. Инициализация нулями.")
        return None
    try:
        weights = [float(p) for p in parts]
        return weights
    except ValueError:
        print("Ошибка: введены не числа. Инициализация нулями.")
        return None

if __name__ == "__main__":
    # Данные для обучения (логическая функция AND)
    X = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    y = [0, 0, 0, 1]

    input_size = 2
    initial_weights = input_weights(input_size + 1)  # +1 для bias

    p = Perceptron(input_size=input_size, initial_weights=initial_weights)
    print(f"Начальные веса: {p.weights}")

    p.train(X, y, epochs=20)
    print(f"Веса после обучения: {p.weights}")

    p.save_weights("weights.pkl")

    p2 = Perceptron(input_size=input_size)
    p2.load_weights("weights.pkl")
    predictions = [p2.predict(x) for x in X]
    print(f"Предсказания после загрузки весов: {predictions}")

    print("Веса совпадают:", p.weights == p2.weights)
1