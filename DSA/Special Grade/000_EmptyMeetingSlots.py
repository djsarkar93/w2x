########################################################################################################################
# Empty Meeting Slots 
# ----------------------------------------------------------------------------------------------------------------------
# Calendar 1   - [['09:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
# Work Hours 1 - ['09:00', '20:00']
# 
# Calendar 2   - [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
# Work Hours 2 - ['10:00', '18:30']
#
# Output       - [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
# ----------------------------------------------------------------------------------------------------------------------
# Time  Complexity: O( 3(m+n) )
# Space Complexity: O( 3(m+n) )
########################################################################################################################


def get_merged_calendars(cal1, cal2):
    m = len(cal1)
    n = len(cal2)
    i = j = 0
    
    merged_cal = list()
    while i < m and j < n:
        if cal1[i][0] < cal2[j][0]:
            merged_cal.append(cal1[i])
            i += 1
        else:
            merged_cal.append(cal2[j])
            j += 1
    
    while i < m:
        merged_cal.append(cal1[i])
        i += 1 
    
    while j < n:
        merged_cal.append(cal2[j])
        j += 1
    
    return merged_cal


def get_compacted_calendars(cal):
    i = 0
    compacted_cal = list()
    compacted_cal.append(list(cal[0]))
    for j in range(1, len(cal)):
        if compacted_cal[i][0] <= cal[j][0] and compacted_cal[i][1] >= cal[j][0]:
            compacted_cal[i][1] = max(compacted_cal[i][1], cal[j][1])
        else:
            compacted_cal.append(list(cal[j]))
            i += 1 
         
    return compacted_cal


def find_empty_slots(cal1, wrkhrs1, cal2, wrkhrs2):
    merged_cal = get_merged_calendars(cal1, cal2)
    merged_cal = [['00:00', min(wrkhrs1[0], wrkhrs2[0])], ['00:00', max(wrkhrs1[0], wrkhrs2[0])]] + merged_cal 
    merged_cal = merged_cal + [[min(wrkhrs1[1], wrkhrs2[1]), '23:59'], [max(wrkhrs1[1], wrkhrs2[1]), '23:59']]
    
    compacted_cal = get_compacted_calendars(merged_cal)
    
    empty_slots = list()
    for i in range( len(compacted_cal)-1 ):
        empty_slots.append( [compacted_cal[i][1], compacted_cal[i+1][0]] )
    
    return empty_slots


cal1 = [['09:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
wrkhrs1 = ['09:00', '20:00']

cal2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
wrkhrs2 = ['10:00', '18:30']

empty_slots = find_empty_slots(cal1, wrkhrs1, cal2, wrkhrs2)
print(f'Empty Slots = {empty_slots}')
