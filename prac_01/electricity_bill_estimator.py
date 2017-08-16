# price_kWh_cents = int(input("Enter cents per kWh: "))
tariff = int(input("Which tariff? 11 or 31: "))
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
estimated_bill = 0
while tariff == 11 or tariff == 31:
    daily_kWh = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))
    if tariff == 11:
        estimated_bill = round(TARIFF_11 * daily_kWh * billing_days)
    elif tariff == 31:
        estimated_bill = round(TARIFF_31 * daily_kWh * billing_days)
    print("Estimated bill: ${}\n".format(estimated_bill))
    tariff = int(input("Which tariff? 11 or 31: "))

