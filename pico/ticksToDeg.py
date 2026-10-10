def ticksToDeg(ticks, zero_offset_ticks, ticks_per_output_turn, direction): 
    actual_ticks = ticks - zero_offset_ticks
    output_revolutions = actual_ticks/ticks_per_output_turn * direction
    output_degrees = output_revolutions * 360.0
    return output_degrees

