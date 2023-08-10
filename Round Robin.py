class PCB:
    def __init__(self, process_id, arrival_time, execution_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.remaining_time = execution_time
        self.turn_around_time = 0
        self.utilization_time = 0
        self.finish_time = 0

    def execute(self, quantum):
        if self.remaining_time <= quantum:
            execution_time = self.remaining_time
            print(execution_time,f"for {self.process_id}")

        else:
            execution_time = quantum
            print(execution_time,f"for {self.process_id}")

        self.remaining_time -= execution_time
        self.utilization_time += execution_time
        return execution_time

def create_processes():
    num_processes = int(input("How many processes do you want to create (min 3, max 5)? "))
    while num_processes < 3 or num_processes > 5:
        num_processes = int(input("Invalid input. Please enter a number between 3 and 5: "))

    processes = []
    for i in range(num_processes):
        process_id = i + 1
        # arrival_time = i * 2  # Assuming arrival time of the first process starts from 0 and increases by 2 for subsequent processes
        execution_time = int(input(f"Enter execution time for process {process_id} (<= 10): "))
        arrival_time = int(input(f"Enter arrival time for process {process_id}: "))
        while execution_time > 10:
            execution_time = int(input("Invalid input. Execution time must be <= 10. Enter again: "))
        processes.append(PCB(process_id, arrival_time, execution_time))

    return processes

def round_robin(processes, quantum):
    ready_queue = processes.copy()
    current_time = 0

    while ready_queue:
        current_process = ready_queue[0]
        ready_queue.pop(0)
        execution_time = current_process.execute(quantum)
        current_time += execution_time

        if current_process.remaining_time > 0:
            ready_queue.append(current_process)
        else:
            current_process.finish_time = current_time
            print(current_process.finish_time,"f")
            current_process.turn_around_time = current_process.finish_time - current_process.arrival_time
            print(current_process.turn_around_time,"t")

    print("\nProcess Execution Details:")
    print("Process ID | Arrival Time | Execution Time | Turnaround Time | Utilization Time | Finish Time")
    for process in processes:
        print(f"  {process.process_id}        |     {process.arrival_time}        |    {process.execution_time}           |   {process.turn_around_time}            |      {process.utilization_time}        |     {process.finish_time}")

if __name__ == "__main__":
    quantum_size = int(input("Enter quantum size (<= 3): "))
    while quantum_size > 3:
        quantum_size = int(input("Invalid input. Quantum size must be <= 3. Enter again: "))

    processes = create_processes()
    round_robin(processes, quantum_size)
