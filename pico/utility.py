def clamp(value: float, low: float, high: float):
    if value >= high: 
        return high 
    elif value <= low :
        return low
    else:
        return value