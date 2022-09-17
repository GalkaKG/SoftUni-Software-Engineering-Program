jobs = [int(x) for x in input().split(', ')]
idx = int(input())

clock_cycles = 0
last_job = jobs[idx]

while jobs:
    curr_job = 36 ** 36
    for job in jobs:
        if job < curr_job:
            curr_job = job
            ind_curr_job = jobs.index(curr_job)

    if curr_job > last_job:
        break
    clock_cycles += curr_job
    jobs[ind_curr_job] = 33333333

print(clock_cycles)
