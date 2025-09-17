import random
import math
import matplotlib.pyplot as plt

def euclidean(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

def total_distance(path, coords):
    return sum(euclidean(coords[path[i]], coords[path[(i+1)%len(path)]]) for i in range(len(path)))

def greedy_route(coords):
    n = len(coords)
    unvisited = set(range(1, n))
    route = [0]
    while unvisited:
        last = route[-1]
        next_city = min(unvisited, key=lambda i: euclidean(coords[last], coords[i]))
        route.append(next_city)
        unvisited.remove(next_city)
    return route

def random_route(n):
    route = list(range(n))
    random.shuffle(route)
    return route

def simulated_annealing(coords, initial_temp=1000, cooling_rate=0.995, stop_temp=1e-3, max_iter=100000):
    n = len(coords)
    current = greedy_route(coords)
    best = list(current)
    best_dist = total_distance(current, coords)
    temp = initial_temp
    for _ in range(max_iter):
        if temp < stop_temp:
            break
        # 2-opt swap
        i, j = sorted(random.sample(range(n), 2))
        new = current[:i] + current[i:j+1][::-1] + current[j+1:]
        new_dist = total_distance(new, coords)
        delta = new_dist - total_distance(current, coords)
        if delta < 0 or random.random() < math.exp(-delta/temp):
            current = new
            if new_dist < best_dist:
                best = list(new)
                best_dist = new_dist
        temp *= cooling_rate
    return best

def plot_route(coords, route, title, color='b'):
    x = [coords[i][0] for i in route] + [coords[route[0]][0]]
    y = [coords[i][1] for i in route] + [coords[route[0]][1]]
    plt.plot(x, y, marker='o', color=color, label=title)
    plt.scatter([c[0] for c in coords], [c[1] for c in coords], c='k', s=30)

def main():
    # Generate random sensor coordinates
    n_sensors = 30
    random.seed(42)
    coords = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n_sensors)]

    # Greedy solution
    greedy = greedy_route(coords)
    greedy_dist = total_distance(greedy, coords)

    # Random solution
    rand = random_route(n_sensors)
    rand_dist = total_distance(rand, coords)

    # Simulated Annealing solution
    sa = simulated_annealing(coords)
    sa_dist = total_distance(sa, coords)

    print(f"Random Path Distance: {rand_dist:.2f}")
    print(f"Greedy Path Distance: {greedy_dist:.2f}")
    print(f"Simulated Annealing Optimized Distance: {sa_dist:.2f}")

    plt.figure(figsize=(12,6))
    plt.subplot(1,2,1)
    plot_route(coords, rand, "Random Path", color='gray')
    plt.title(f"Random Path (Distance: {rand_dist:.2f})")
    plt.axis('equal')

    plt.subplot(1,2,2)
    plot_route(coords, greedy, "Greedy Path", color='orange')
    plot_route(coords, sa, "Simulated Annealing", color='green')
    plt.title(f"Greedy (Dist: {greedy_dist:.2f}) vs SA (Dist: {sa_dist:.2f})")
    plt.legend()
    plt.axis('equal')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()