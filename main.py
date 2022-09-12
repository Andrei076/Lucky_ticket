import threading
from multiprocessing import Process
import datetime


interval_x = ["000000", "250000"]
interval_y = ["250001", "500000"]
interval_z = ["500001", "750000"]
interval_r = ["750001", "999999"]


def lucky_ticket(interval):
    start = int(interval[0])
    end = int(interval[1])
    lucky_tickets = 0
    for itm in range(start, end+1):
        ticket = f"{itm:06}"
        if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3])\
                + int(ticket[4]) + int(ticket[5]):
            lucky_tickets += 1
    print(f"Number of lucky tickets is {lucky_tickets} in interval{interval}")


if __name__ == '__main__':
    # process_x = Process(target=lucky_ticket, args=(interval_x,))
    # process_y = Process(target=lucky_ticket, args=(interval_y,))
    # process_z = Process(target=lucky_ticket, args=(interval_z,))
    # process_r = Process(target=lucky_ticket, args=(interval_r,))

    thread_x = threading.Thread(target=lucky_ticket, args=(interval_x,))
    thread_y = threading.Thread(target=lucky_ticket, args=(interval_y,))
    thread_z = threading.Thread(target=lucky_ticket, args=(interval_z,))
    thread_r = threading.Thread(target=lucky_ticket, args=(interval_r,))

    # process_start = datetime.datetime.now()
    # print(f"Process starting at {process_start.strftime('%H:%M:%S:%f')}")
    # process_x.start()
    # process_y.start()
    # process_z.start()
    # process_r.start()
    # process_x.join()
    # process_y.join()
    # process_z.join()
    # process_r.join()

    # process_finish = datetime.datetime.now()
    # print(f"Process finished  at {process_finish.strftime('%H:%M:%S:%f')}")

    thread_start = datetime.datetime.now()
    print(f"Thread start at {thread_start.strftime('%H:%M:%S:%f')}")
    thread_x.start()
    thread_y.start()
    thread_z.start()
    thread_r.start()
    thread_x.join()
    thread_y.join()
    thread_z.join()
    thread_r.join()

    thread_finish = datetime.datetime.now()
    print(f"Thread finished at {thread_finish.strftime('%H:%M:%S:%f')}")

    # time_process = process_finish - process_start
    # print(f"Processes worked {time_process}")

    time_thread = thread_finish - thread_start
    print(f"Threads worked {time_thread}")
