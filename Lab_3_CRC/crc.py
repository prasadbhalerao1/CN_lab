# Experiment 3: CRC for 7-bit / 8-bit ASCII


def ascii_to_binary(message, bits):
    binary = ""

    for ch in message:
        value = ord(ch)
        if value >= 2 ** bits:
            raise ValueError("Character not supported for selected ASCII size!")
        binary += format(value, f"0{bits}b")

    return binary


def mod2_division(data, generator):
    data = list(data)
    n = len(generator)

    for i in range(len(data) - n + 1):
        if data[i] == '1':
            for j in range(n):
                data[i + j] = str(int(data[i + j]) ^ int(generator[j]))

    return ''.join(data[-(n - 1):])


# Main program
message = input("Enter the message: ")
bits = int(input("Enter ASCII size (7 or 8): "))
generator = input("Enter generator polynomial: ")

if bits not in (7, 8):
    print("Invalid ASCII size!")
elif (len(generator) < 2 or generator[0] != '1' or generator[-1] != '1'
      or any(bit not in '01' for bit in generator)):
    print("Invalid generator polynomial!")
else:
    try:
        data = ascii_to_binary(message, bits)
        print("\nOriginal Binary Data:", data)

        zeros = '0' * (len(generator) - 1)
        crc = mod2_division(data + zeros, generator)
        print("CRC Remainder:", crc)

        codeword = data + crc
        print("Transmitted Codeword:", codeword)

        position = int(input("\nEnter bit position to flip (0 for no error): "))

        if position < 0 or position > len(codeword):
            print("Invalid bit position!")
        else:
            received = list(codeword)

            if position != 0:
                index = position - 1
                received[index] = '1' if received[index] == '0' else '0'

            received = ''.join(received)
            print("\nReceived Data:", received)

            remainder = mod2_division(received, generator)
            print("Receiver Remainder:", remainder)

            if '1' in remainder:
                print("Error Detected!")
                print("Requesting retransmission...")

                received = codeword
                print("Retransmitted Data:", received)

                remainder = mod2_division(received, generator)
                print("New Remainder:", remainder)

                if '1' not in remainder:
                    print("Error Corrected Successfully!")
            else:
                print("No Error Detected!")

    except ValueError as error:
        print("Invalid input:", error)
