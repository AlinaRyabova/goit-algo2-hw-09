import random
import math

# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)

# Hill Climbing
def hill_climbing(func, bounds, iterations=5000, epsilon=1e-6):
    # Початкова точка (випадкова)
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)

    for _ in range(iterations):
        # Генеруємо нову точку в околі поточної
        new_solution = [xi + random.uniform(-epsilon, epsilon) for xi in current_solution]
        new_solution = [min(max(xi, b[0]), b[1]) for xi, b in zip(new_solution, bounds)]  # Забезпечуємо межі
        new_value = func(new_solution)

        # Якщо нове значення краще, оновлюємо поточне рішення
        if new_value < current_value:
            current_solution, current_value = new_solution, new_value

        # Якщо зміна значення менша за epsilon, завершуємо
        if abs(current_value - new_value) < epsilon:
            break

    return current_solution, current_value

# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    # Початкова точка (випадкова)
    best_solution = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best_solution)

    for _ in range(iterations):
        # Генеруємо нову випадкову точку
        new_solution = [random.uniform(b[0], b[1]) for b in bounds]
        new_value = func(new_solution)

        # Якщо нове значення краще, оновлюємо найкраще рішення
        if new_value < best_value:
            best_solution, best_value = new_solution, new_value

        # Якщо зміна значення менша за epsilon, завершуємо
        if abs(best_value - new_value) < epsilon:
            break

    return best_solution, best_value

# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    # Початкова точка (випадкова)
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    best_solution, best_value = current_solution, current_value

    for _ in range(iterations):
        # Генеруємо нову точку в околі поточної
        new_solution = [xi + random.uniform(-epsilon, epsilon) for xi in current_solution]
        new_solution = [min(max(xi, b[0]), b[1]) for xi, b in zip(new_solution, bounds)]  # Забезпечуємо межі
        new_value = func(new_solution)

        # Різниця між новим і поточним значенням
        delta = new_value - current_value

        # Якщо нове значення краще, приймаємо його
        if delta < 0:
            current_solution, current_value = new_solution, new_value
            if new_value < best_value:
                best_solution, best_value = new_solution, new_value
        else:
            # Інакше приймаємо з ймовірністю exp(-delta / temp)
            if random.random() < math.exp(-delta / temp):
                current_solution, current_value = new_solution, new_value

        # Знижуємо температуру
        temp *= cooling_rate

        # Якщо температура менша за epsilon, завершуємо
        if temp < epsilon:
            break

    return best_solution, best_value

if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)