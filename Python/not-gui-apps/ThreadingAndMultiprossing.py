import threading ,  multiprocessing , concurrent.futures , time

# Main Fanction

def do_somthing(seconds) :

    print(f"Sleep {seconds} second...")
    time.sleep(seconds)
    print("Done Sleeping...")

# Classical Way

def classical_way():
    for _ in range(10):

        do_somthing(1)

# Threading Way
def threading_way(option):

    if option == 1 :

        threads = []
        for _ in range(10):

            t = threading.Thread(target=do_somthing , args=[1]) 
            t.start()
            threads.append(t)

        for thr in threads :

            thr.join()
    
    elif option == 2 :

        with concurrent.futures.ThreadPoolExecutor() as executor :

            for _ in range(10):
                m = executor.submit(do_somthing(1) , 1)

            # print(m)

start = time.perf_counter()

# classical_way()
threading_way(2)

finish = time.perf_counter()

print(f"Finish in {round(finish - start , 2)} second(s)")
