from gravityTorque import gravityTorque
tolerance_torque = 0.00001

torque_harness_inputs_outputs = {
    "horizontal": ([0, 0.050, 0.150, 0.030, 0.075],0.09565),
    "thirty": ([30, 0.050, 0.150, 0.030, 0.075],0.08283),
    "forty_five": ([45, 0.050, 0.150, 0.030, 0.075],0.06763),
    "sixty": ([60, 0.050, 0.150, 0.030, 0.075],0.04782),
    "vertical": ([90, 0.050, 0.150, 0.030, 0.075],0.0),
    "unloaded": ([0, 0, 0.150, 0.030, 0.075],0.02207),
    "load_only": ([0, 0.050, 0.150, 0, 0.075],0.07358),
    "past_vertical": ([180, 0.050, 0.150, 0.030, 0.075],-0.09565),
}

for test_case in torque_harness_inputs_outputs: 
    expected = torque_harness_inputs_outputs[test_case][1]
    result = gravityTorque(*torque_harness_inputs_outputs[test_case][0])
    print(str(test_case)+" "+str((abs(expected-result)<tolerance_torque)))