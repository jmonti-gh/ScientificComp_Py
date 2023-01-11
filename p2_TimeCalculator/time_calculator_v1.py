''' Scientific Computing w/Python - project 2: Time Calculator '''

# time_calculator_v0.py + add dow calc

def add_time(start, duration, sdow=False):
    # get the hours, mins, and AM-PM necesary to do operations
    st_tme = start.split()[0]
    st_xm = start.split()[1]
    st_hou = st_tme.split(':')[0]
    st_min = st_tme.split(':')[1]
    dur_hou = duration.split(':')[0]
    dur_min = duration.split(':')[1]

    # One way is convert all to minutes, add minuts, then sep dys, hs, minut
    # but before conver all to 24hs clock upon AM or PM & use ints
    st_hou = int(st_hou)                #st_xm  == AM"
    if st_xm == 'PM': st_hou += 12
    st_min_tot = st_hou * 60 + int(st_min)
    # calc dur_min_tot
    dur_min_tot = int(dur_hou) * 60 + int(dur_min)
    
    # Calc new_timeime, first calt total end minutes
    end_min_tot = st_min_tot + dur_min_tot
    # 1 day = 24hs = 1440 mins || 1 hour = 60 mins
    end_day = end_min_tot // 1440       # int number of days (end)
    min_d_remind = end_min_tot % 1440   # int nber of mins reminder
    end_hou = min_d_remind // 60        # int nber of hours (end)
    end_min = min_d_remind % 60         # int final mins result
    # have to calc endAM - endPM and mod. end_hou in accordance
    if end_hou < 12: end_xm = 'AM'
    else:
        end_xm = 'PM'
        end_hou -= 12
    # correct the situation when hou = 0 show 12
    if end_hou == 0: end_hou = 12

    # add 0 left mins if necesary (hours and days do not need)
    if end_min < 10: end_min = '0' + str(end_min)
    else: end_min = str(end_min)

    # dow calc -> Before building the result (new_time)
    if sdow:
        dows = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']
        st_dow = sdow.capitalize()
        # if sdow string is erroneus - danger!
        try:
            nbr_st_dow = dows.index(st_dow)
        except ValueError as e:
            print('Error: Invalid Day of Week:', sdow,
                 '   - # dow Calc.', e)
            end_dow = 'Wrong_dow!'
        else:
            # Reminder is necesary to mantain between 0 an 6
            nbr_end_dow = (nbr_st_dow + end_day) % 7
            end_dow = dows[nbr_end_dow]

    # build basic new_time (end_time funct result)
    new_time = str(end_hou) + ':' + end_min + ' ' + end_xm
    # but if end_day > 0 then add more info to basic new_time
    if end_day == 1:
        nxt_day = ' (next day)'
    elif end_day > 1:
        nxt_day = ' (' + str(end_day) + ' days later)'
    # Build de final new_time upon sdow exist & end_day > 0
    if sdow: new_time += ', ' + end_dow     # 1st add end_dow if optional arg
    if end_day: new_time += nxt_day         # 2nd add nxt_day if end_day > 0
    # if none of the above new_time remains basic.

    return new_time

  

print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print()
print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print()
print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print()
print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print()
print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

# print()
# print(add_time("11:43 PM", "24:20", "teSday"))
# # Returns: 12:03 AM, Thursday (2 days later)

print()
print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)

# print()
# print(add_time("6:30 PM", "205:12", 'Sunday'))
# # Returns: 7:42 AM (9 days later)