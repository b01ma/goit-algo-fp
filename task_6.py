items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []

    for name, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            total_cost += info['cost']
            total_calories += info['calories']
            selected_items.append(name)

    return selected_items, total_calories

def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost, calories = info['cost'], info['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення вибраних предметів
    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = item_list[i - 1][0]
            selected_items.append(name)
            w -= item_list[i - 1][1]['cost']

    return selected_items[::-1], dp[n][budget]

greedy_result = greedy_algorithm(items, 100)
dp_result = dynamic_programming(items, 100)
print('Greedy results:', greedy_result)
print('Dynamic programming results:', dp_result)
