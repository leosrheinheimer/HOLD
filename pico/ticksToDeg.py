def ticksToDeg(ticks, zero_offset_ticks, ticks_per_output_turn, direction): 
    actual_ticks = ticks - zero_offset_ticks
    output_revolutions = actual_ticks/ticks_per_output_turn * direction
    output_degrees = output_revolutions * 360.0
    return output_degrees

def zeroOffsetTicks(encoder_count, output_deg, ticks_per_output_turn, direction):
    zero_offset = -(output_deg/360.0 * ticks_per_output_turn * direction - encoder_count)
    return zero_offset