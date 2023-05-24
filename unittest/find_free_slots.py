from datetime import datetime, timedelta

def find_free_slots(start_times, durations):
    slots = []
    start_time = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
    end_time = start_time.replace(hour=18, minute=0, second=0, microsecond=0)

    for i in range(len(start_times)):
        if i == 0 and start_times[i] > start_time:
            slots.append(f"{start_time.strftime('%H:%M')}-{start_times[i].strftime('%H:%M')}")

        if i < len(start_times) - 1 and start_times[i] + timedelta(minutes=durations[i]) < start_times[i+1]:
            slots.append(f"{(start_times[i] + timedelta(minutes=durations[i])).strftime('%H:%M')}-{start_times[i+1].strftime('%H:%M')}")

        if i == len(start_times) - 1 and start_times[i] + timedelta(minutes=durations[i]) < end_time:
            slots.append(f"{(start_times[i] + timedelta(minutes=durations[i])).strftime('%H:%M')}-{end_time.strftime('%H:%M')}")

    return slots
