
import csv

# Open the cybersecurity risk register
with open("risk_register.csv", "r") as file:
    reader = csv.DictReader(file)

    print("SECURETRUST BANK - CYBERSECURITY RISK ASSESSMENT")
    print("-" * 55)

    for risk in reader:
        likelihood = int(risk["Likelihood"])
        impact = int(risk["Impact"])

        # Calculate the risk score
        risk_score = likelihood * impact

        # Classify the risk
        if risk_score >= 15:
            risk_level = "HIGH"
        elif risk_score >= 6:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        print(f"Risk: {risk['Risk_Description']}")
        print(f"Score: {risk_score}/25")
        print(f"Level: {risk_level}")
        print("-" * 55)
