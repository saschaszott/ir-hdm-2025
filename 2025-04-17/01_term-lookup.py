import time
import random
import bisect
import numpy as np
import matplotlib.pyplot as plt

# Versuchsparameter
n = 1_000_000       # Größe des Term Dictionary
num_trials = 1000   # Anzahl der Suchanfragen

# Testdaten vorbereiten
terms = [f"word{i}" for i in range(n)]
# lexikographisch sortiertes Term Dictionary
sorted_terms = sorted(terms)
hash_dict = {term: i for i, term in enumerate(terms)}

def linear_search(data, key):
    """
    Linear search algorithm to find a key in a list.
    """
    for item in data:
        if item == key:
            return True
    return False

def binary_search(data, key):
    """
    Binary search algorithm (iterative) to find a key in a sorted list.
    """
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == key:
            return True
        elif data[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return False

def hash_lookup(dictionary, key):
    """
    Hash lookup algorithm to find a key in a dictionary.
    """
    return key in dictionary

def bisect_search(data, key):
    """
    Bisect search algorithm to find a key in a sorted list.
    """
    idx = bisect.bisect_left(data, key)
    return idx < len(data) and data[idx] == key

def measure(method_name, function, data_structure, queries):
    """
    Measure the time taken by one of the search methods.
    """
    durations = []
    for key in queries:
        start = time.perf_counter()
        function(data_structure, key)
        end = time.perf_counter()
        durations.append(end - start)
    durations = np.array(durations)
    return {
        "name": method_name,
        "avg_time": durations.mean(),             # arithmetischer Mittelwert
        "max_time": np.quantile(durations, 1.0),  # alle Werte kleiner gleich
        "q95_time": np.quantile(durations, 0.95), # 95%-Quantil: 95% der Werte kleiner gleich
        "q90_time": np.quantile(durations, 0.9),  # 90%-Quantil: 90% der Werte kleiner gleich
        "q50_time": np.quantile(durations, 0.5),  # 50%-Quantil: 50% der Werte kleiner gleich
        "all_times": durations
    }

# Erzeugung zufälliger Suchbegriff
search_terms = random.choices(terms, k=num_trials)
if num_trials < 10:
    print("Suchbegriffe:", search_terms)

# Durchführung der Messungen
results = []
results.append(measure("Linear Search", linear_search, terms, search_terms))
results.append(measure("Binary Search", binary_search, sorted_terms, search_terms))
results.append(measure("Bisect Search", bisect_search, sorted_terms, search_terms))
results.append(measure("Hash Lookup", hash_lookup, hash_dict, search_terms))

# Ausgabe der Ergebnisse
print(f"{'Methode':<15} {'Ø Zeit (ms)':>18} {'max. Zeit (ms)':>18} {'95%-Quantil (ms)':>18} {'90%-Quantil (ms)':>18} {'50%-Quantil (ms)':>18}")
print("-" * 110)
for r in results:
    print(f"{r['name']:<15} {r['avg_time']*1000:18.3f} {r['max_time']*1000:18.3f} {r['q95_time']*1000:18.3f} {r['q90_time']*1000:18.3f} {r['q50_time']*1000:18.3f}")

labels = [r["name"] for r in results]
avg_times = [r["avg_time"] * 1000 for r in results]
max_times = [r["max_time"] * 1000 for r in results]
q95_times = [r["q95_time"] * 1000 for r in results]
q90_times = [r["q90_time"] * 1000 for r in results]
q50_times = [r["q50_time"] * 1000 for r in results]

x = np.arange(len(labels))
width = 0.25

fig, ax = plt.subplots()
ax.bar(x - width/2, avg_times, width, label='arithmetischer Durchschnitt')
ax.bar(x - width/4, max_times, width, label='Maximum')
ax.bar(x,           q95_times, width, label='95%-Quantil')
ax.bar(x + width/4, q90_times, width, label='90%-Quantil')
ax.bar(x + width/2, q50_times, width, label='50%-Quantil / Median')

ax.set_ylabel('Zeit (ms)')
ax.set_title(f"Suchzeitvergleich bei {n} Einträgen (Versuchsanzahl: {num_trials})")
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=15)
ax.legend()

plt.yscale("log")
plt.tight_layout()
plt.show()