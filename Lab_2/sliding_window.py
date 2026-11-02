# Experiment 2: Go-Back-N and Selective Repeat


def go_back_n(total_frames, window_size, lost_frame):
    print("\n--- GO-BACK-N PROTOCOL ---")

    base = 1
    lost_once = False

    while base <= total_frames:
        end = min(base + window_size - 1, total_frames)
        expected = base

        print(f"\nSender Window: {base} to {end}")

        for frame in range(base, end + 1):
            print(f"Sender: Sending Frame {frame}")

            if frame == lost_frame and not lost_once:
                print(f"Frame {frame} lost!")
                lost_once = True
            elif frame == expected:
                print(f"Receiver: Frame {frame} received")
                expected += 1
                print(f"Receiver: Cumulative ACK {expected - 1}")
            else:
                print(f"Receiver: Frame {frame} discarded")
                print(f"Receiver: Duplicate ACK {expected - 1}")

        if expected <= end:
            print("\nTimeout occurred!")
            print("Go-Back-N: Retransmitting outstanding frames")

            for frame in range(expected, end + 1):
                print(f"Sender: Retransmitting Frame {frame}")
                print(f"Receiver: Frame {frame} received")
                expected += 1
                print(f"Receiver: Cumulative ACK {expected - 1}")

        base = end + 1

    print("\nAll frames transmitted successfully using Go-Back-N.")


def selective_repeat(total_frames, window_size, lost_frame):
    print("\n--- SELECTIVE REPEAT PROTOCOL ---")

    base = 1
    lost_once = False

    while base <= total_frames:
        end = min(base + window_size - 1, total_frames)
        acked = set()

        print(f"\nSender Window: {base} to {end}")

        for frame in range(base, end + 1):
            print(f"Sender: Sending Frame {frame}")

            if frame == lost_frame and not lost_once:
                print(f"Frame {frame} lost!")
                lost_once = True
            else:
                print(f"Receiver: Frame {frame} received")
                acked.add(frame)
                print(f"Receiver: ACK {frame}")

        missing = None
        for frame in range(base, end + 1):
            if frame not in acked:
                missing = frame
                break

        if missing is not None:
            print("\nTimeout occurred!")
            print(f"Retransmitting only Frame {missing}")
            print(f"Sender: Retransmitting Frame {missing}")
            print(f"Receiver: Frame {missing} received")
            acked.add(missing)
            print(f"Receiver: ACK {missing}")

        print("\nReceiver delivers frames in order:")
        for frame in range(base, end + 1):
            print(f"Frame {frame}", end=" ")
        print()

        base = end + 1

    print("\nAll frames transmitted successfully using Selective Repeat.")


# Main program
total_frames = int(input("Enter total number of frames: "))
window_size = int(input("Enter window size: "))
lost = int(input("Enter frame number to lose (0 for no loss): "))

if total_frames <= 0 or window_size <= 0:
    print("Invalid input!")
elif lost < 0 or lost > total_frames:
    print("Invalid lost frame number!")
else:
    print("\n1. Go-Back-N")
    print("2. Selective Repeat")
    print("3. Both")
    choice = int(input("Enter your choice: "))

    lost_frame = None if lost == 0 else lost

    if choice == 1 or choice == 3:
        go_back_n(total_frames, window_size, lost_frame)
    if choice == 2 or choice == 3:
        selective_repeat(total_frames, window_size, lost_frame)
    if choice not in (1, 2, 3):
        print("Invalid choice!")
