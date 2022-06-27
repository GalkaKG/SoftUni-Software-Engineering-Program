needed_experience = float(input())
count_of_battles = int(input())
total_sum = 0
battle = 0

for battle in range(1, count_of_battles + 1):
    experience_earned_per_battle = float(input())

    if battle % 3 == 0:
        experience_earned_per_battle += (experience_earned_per_battle * 0.15)

    if battle % 5 == 0:
        experience_earned_per_battle -= (experience_earned_per_battle * 0.10)

    if battle % 15 == 0:
        experience_earned_per_battle += (experience_earned_per_battle * 0.05)

    total_sum += experience_earned_per_battle

    if total_sum >= needed_experience:
        break

if total_sum < needed_experience:
    diff = abs(needed_experience - total_sum)
    print(f"Player was not able to collect the needed experience, {diff:.2f} more needed.")
elif total_sum >= needed_experience:
    print(f"Player successfully collected his needed experience for {battle} battles.")
