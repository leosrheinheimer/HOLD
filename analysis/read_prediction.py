with open("data/torque_predictions.csv") as f: 
    lines = f.readlines()
    for line in lines[1:] : 
        line_list = line.split(",")
        arm_angle_deg = line_list[0]
        load_torque_nm = line_list[2]
        unloaded_torque_nm = line_list[1]
        payload_torque_nm = float(load_torque_nm) - float(unloaded_torque_nm)
        print("%.1f" % float(arm_angle_deg), "%.4f" % float(payload_torque_nm))