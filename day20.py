import time

print("⏱️ Stopwatch Timer - Day 20")
print("Press ENTER to start, ENTER to stop, type 'q' to quit")

while True:
    command = input("\nPress ENTER to start or 'q' to quit: ")
    if command.lower() == 'q':
        print("👋 Exiting Stopwatch...")
        break

    start_time = time.time()
    input("▶️ Press ENTER to stop: ")
    end_time = time.time()

    elapsed = end_time - start_time
    print(f"⏳ Elapsed Time: {round(elapsed, 2)} seconds")
