def go_back_n(total, window, lost):
    print("\n--- GO BACK N ---")

    base = 1

    while base <= total:
        end = min(base + window - 1, total)
        print("\nWindow:", base, "to", end)

        for i in range(base, end + 1):
            print("Sending Frame", i)

            if i == lost:
                print("Frame", i, "Lost!")
                print("Timeout! Retransmitting from Frame", i)

                for j in range(i, end + 1):
                    print("Retransmitting Frame", j)
                    print("ACK", j)

                lost = 0
                break

            else:
                print("ACK", i)

        base = end + 1

    print("\nGo-Back-N Completed!")


def selective_repeat(total, window, lost):
    print("\n--- SELECTIVE REPEAT ---")

    base = 1

    while base <= total:
        end = min(base + window - 1, total)
        print("\nWindow:", base, "to", end)

        for i in range(base, end + 1):
            print("Sending Frame", i)

            if i == lost:
                print("Frame", i, "Lost!")

            else:
                print("ACK", i)

        if lost >= base and lost <= end:
            print("\nTimeout! Retransmitting only Frame", lost)
            print("Retransmitting Frame", lost)
            print("ACK", lost)
            lost = 0

        base = end + 1

    print("\nSelective Repeat Completed!")


# Main program
total = int(input("Enter total frames: "))
window = int(input("Enter window size: "))
lost = int(input("Enter lost frame (0 for no loss): "))

if total <= 0 or window <= 0 or lost < 0 or lost > total:
    print("Invalid input!")

else:
    print("\n1. Go-Back-N")
    print("2. Selective Repeat")
    print("3. Both")

    choice = int(input("Enter choice: "))

    if choice == 1 or choice == 3:
        go_back_n(total, window, lost)

    if choice == 2 or choice == 3:
        selective_repeat(total, window, lost)

    if choice not in (1, 2, 3):
        print("Invalid choice!")