print("=== Swimming Pool Entry Checker ===")
print("Answer 3 questions and I will tell you which pool you can use.")
print()

# Collecting the answers
age = int(input("How old are you? "))

can_swim = input("Can you swim 25 metres? (yes / no): ").lower()
adult_here = input("Is an adult with you? (yes / no): ").lower()


# Part 1 - Age group
if age < 4:
    print("Age group  : Toddler - splash pool only, always with an adult.")
elif age < 12:
    print("Age group  : Child - main pool with an adult.")
elif age < 18:
    print("Age group  : Teen - main pool alone if you can swim.")
else:
    print("Age group  : Adult - all pools open to you.")


# Part 2 - Check whether the answers are understood
if can_swim != "yes" and can_swim != "no":
    print("Input error : Please answer the swimming question with yes or no.")
    swim_known = False
else:
    swim_known = True

if adult_here != "yes" and adult_here != "no":
    print("Input error : Please answer the adult question with yes or no.")
    adult_known = False
else:
    adult_known = True


# Part 3 - Deep pool
if can_swim == "yes" and adult_here == "yes":
    print("Deep pool  : Allowed - you can swim and an adult is present.")


# Part 4 - Shallow end
if age < 12 or can_swim == "no":
    print("Shallow only: Stay in the shallow end today.")


# Part 5 - Lifeguard reminder
if adult_known == True and adult_here != "yes":
    print("Reminder   : Please have an adult nearby.")


# Part 6 - Final verdict
if swim_known == False or adult_known == False:
    print("Verdict    : Cannot decide until both questions are answered properly.")
elif age >= 18 and can_swim == "yes":
    print("Verdict    : Full access. Enjoy your swim.")
elif age >= 12 and can_swim == "yes" and adult_here == "yes":
    print("Verdict    : Main pool access with your adult nearby.")
elif can_swim == "no" and not (adult_here == "yes"):
    print("Verdict    : Shallow end only, and please find an adult first.")
else:
    print("Verdict    : Shallow end today - come back with an adult for more.")

print()
print("Have a safe swim!")