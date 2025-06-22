import random
import pandas as pd

def monte_carlo_dice_simulation(trials=100_000):
    results = {i: 0 for i in range(2, 13)}  # суми від 2 до 12

    for _ in range(trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        results[total] += 1

    data = []
    for total, count in results.items():
        percent = round(count / trials * 100, 2)
        fraction = f"{count}/{trials}"
        data.append([total, f"{percent}%", fraction])

    df = pd.DataFrame(data, columns=["Сума", "Імовірність", "Кількість випадків"])
    return df

# Запуск
df = monte_carlo_dice_simulation(trials=100_000)
print(df.to_string(index=False))
