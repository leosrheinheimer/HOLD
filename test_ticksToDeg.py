from ticksToDeg import ticksToDeg

tolerance_deg = 0.01

harness_inputs_outputs = {
    "test_1": ([374, 0, 11, 34, 1],360.0),
    "test_2": ([94, 0, 11, 34, 1],90.48),
    "test_3": ([287, 100, 11, 34, 1],180.0),
    "test_4": ([187, 0, 11, 34, -1],-180.0),
    "test_5": ([1496, 0, 44, 34, 1],360.0)
}

for test in harness_inputs_outputs:      
    expected = harness_inputs_outputs[test][1]
    result = ticksToDeg(*harness_inputs_outputs[test][0])
    ##print(test, expected, result)
    print(test+" "+str(abs(result-expected)<tolerance_deg))

