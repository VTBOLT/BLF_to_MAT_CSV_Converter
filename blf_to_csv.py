import candas as cd
import scipy.io
import datetime

input_blf = "track1_run_3_ride_to_lot_(TriggerF081)"

# Provide database .dbc and .ini folder location
db = cd.load_dbc("BOLTVS_Ch1_Rev2")

# Provide file without extension
log_data = cd.from_file(db, "track1_run_3_ride_to_lot_(TriggerF081)")

# Signals can be accessed like this
# print(log_data["Pack_Voltage"])

###### Convert the times in the output .mat file to time since first event, not epoch
mat = scipy.io.loadmat(f'{input_blf}.mat')

# find start time
min_epoch_utc = float('inf')
for key, data_points in mat.items():
    if "__" not in key:
        # print(f'{key}: {data_points[0]}')
        this_time = data_points[0][0]
        if this_time < min_epoch_utc:
            min_epoch_utc = this_time

# report start time
local_dt = datetime.datetime.fromtimestamp(min_epoch_utc)
date_time_string = local_dt.strftime("%I:%M:%S %p %Z on %m/%d/%Y ")
print(f'First was datapoint at: {date_time_string}')

# change start times
for key, data_points in mat.items():
    if "__" not in key:
        for row in data_points:
            row[0] = row[0]-min_epoch_utc

print("Saving output .mat file...")
scipy.io.savemat(f'{input_blf}_seconds.mat', mat)
print("Finished saving.")

