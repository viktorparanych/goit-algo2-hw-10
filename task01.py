import time
import random
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    """QuickSort з випадковим вибором опорного елемента."""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    """QuickSort із фіксованим вибором опорного елемента середина масиву."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    runs = 5
    
    rand_times = []
    det_times = []
    
    for size in sizes:
        rand_time_sum = 0
        det_time_sum = 0
        
        for _ in range(runs):
           
            test_arr = [random.randint(0, 1_000_000) for _ in range(size)]
            
            arr_for_rand = test_arr.copy()
            arr_for_det = test_arr.copy() 
    
            start_time = time.time()
            randomized_quick_sort(arr_for_rand)
            rand_time_sum += time.time() - start_time
            
            start_time = time.time()
            deterministic_quick_sort(arr_for_det)
            det_time_sum += time.time() - start_time
            
        avg_rand = rand_time_sum / runs
        avg_det = det_time_sum / runs
        
        rand_times.append(avg_rand)
        det_times.append(avg_det)
        
        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {avg_rand:.4f} секунд")
        print(f"   Детермінований QuickSort: {avg_det:.4f} секунд\n")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, rand_times, marker='o', label='Рандомізований QuickSort', color='tab:blue')
    plt.plot(sizes, det_times, marker='s', label='Детермінований QuickSort', color='tab:orange')
    
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()