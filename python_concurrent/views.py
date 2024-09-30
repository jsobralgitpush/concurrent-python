import time
import concurrent.futures
from django.shortcuts import render

def heavy_task(n):
    time.sleep(2)
    return f"Task {n} completed"

def synchronous_view(request):
    start_time = time.time()
    results = []
    for i in range(5):
        results.append(heavy_task(i))
    end_time = time.time()
    sync_time = end_time - start_time
    context = {
        'method': 'Synchronous',
        'results': results,
        'execution_time': sync_time
    }
    return render(request, 'python_concurrent/performance.html', context)


def concurrent_view(request):
    start_time = time.time()
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(heavy_task, i) for i in range(5)]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    end_time = time.time()
    concurrent_time = end_time - start_time
    context = {
        'method': 'Concurrent',
        'results': results,
        'execution_time': concurrent_time
    }
    return render(request, 'python_concurrent/performance.html', context)
