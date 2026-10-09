def ticksToDeg(ticks, zero_offset_ticks, ticks_per_motor_turn, gear_ratio, direction): 
    actual_ticks = ticks - zero_offset_ticks
    motor_revolutions = actual_ticks / ticks_per_motor_turn
    output_revolutions = motor_revolutions / gear_ratio * direction
    output_degrees = output_revolutions * 360.0
    return output_degrees

