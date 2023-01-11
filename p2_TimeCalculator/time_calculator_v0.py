''' Scientific Computing w/Python - project 2: Time Calculator '''

# time_calculator_v0.py

def add_time(startt, duration, sdow=False):
    # get the hours, mins, and AM-PM necesary to do operations
    st_tme = startt.split()[0]
    st_xm = startt.split()[1]
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
    
    # Calc endtime, first calt total end minutes
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

    # build basic endt (end_time funct result)
    endt = str(end_hou) + ':' + end_min + ' ' + end_xm
    # but if end_day > 0 then
    if end_day == 1:
        endt += ' (next day)'
    elif end_day > 1:
        endt += ' (' + str(end_day) + ' days later)'

    #print(end_day, end_hou, end_xm, end_min)
    return endt


    

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

print()
print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
