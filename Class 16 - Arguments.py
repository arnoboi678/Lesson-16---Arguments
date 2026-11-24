def total_w_tip(total_bill, tip_perc):
    tip = tip_perc/100 * total_bill
    total_w_tip = total_bill + tip
    return total_w_tip
print(f"The final total is {total_w_tip(999.94,10)}.")