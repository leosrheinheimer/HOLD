from ticksToDeg import ticksToDeg

tolerance_deg = 0.01

harness_inputs_outputs = {
    "full_turn": ([1245.5, 0, 1245.5, 1],360.0),
    "not_round": ([313, 0, 1245.5, 1],90.47),
    "offset": ([722.75, 100, 1245.5, 1],180.0),
    "reversed": ([622.75, 0, 1245.5, -1],-180.0),
    "other_constant": ([748, 0, 748, 1],360.0),
}

for test in harness_inputs_outputs:      
    expected = harness_inputs_outputs[test][1]
    result = ticksToDeg(*harness_inputs_outputs[test][0])
    print(test+" "+str(abs(result-expected)<tolerance_deg))