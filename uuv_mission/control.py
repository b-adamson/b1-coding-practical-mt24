# fixed gains
KP = 0.15
KD = 0.6

def pd_controller(error, prev_error):
    """Return u[t] from the errors e[t] and e[t-1]."""
    return float(KP * error + KD * (error - prev_error))
