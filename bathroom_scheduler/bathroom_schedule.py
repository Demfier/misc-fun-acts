from datetime import date, timedelta

unit_num = 1
num_rooms = 5

room_nums = list(range(unit_num * 100 + 1, unit_num * 100 + (num_rooms+1)))
room_nums += [room_nums[0]]  # make the list cyclic

curr_date = date.today()
end_date = date(2020, 9, 1)  # end schedule on 1st Sept. 2020

schedule_line = 'Date\tBathroom1\tBathroom2\n'
date_counter, room_counter = 0, 0
time_diffs = [timedelta(days=4), timedelta(days=3)]

while curr_date < end_date:
    schedule_line += '{}\t{}\t{}\n'.format(
        curr_date.strftime("%A %d, %B %Y"),
        room_nums[room_counter], room_nums[room_counter+1])
    curr_date += time_diffs[date_counter]
    date_counter = (date_counter + 1) % len(time_diffs)
    room_counter = (room_counter + 2) % num_rooms

with open('bathroom_schedule_unit{}.tsv'.format(unit_num), 'w') as f:
    f.write(schedule_line)

