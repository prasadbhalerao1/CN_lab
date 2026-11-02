# Experiment 3: CRC for 7-bit / 8-bit ASCII


def ascii_to_binary(message, bits):
    binary = ""

    for ch in message:
        binary += format(ord(ch), f"0{bits}b")

    return binary


def mod2_division(data, generator):
    data = list(data)
    n = len(generator)

    for i in range(len(data) - n + 1):
        if data[i] == '1':
            for j in range(n):
                data[i+j] = str(int(data[i+j]) ^ int(generator[j]))

    return ''.join(data[-(n-1):])


# Main program
message = input("Enter message: ")
bits = int(input("Enter ASCII size (7 or 8): "))
generator = input("Enter generator: ")

data = ascii_to_binary(message, bits)
print("Binary Data:", data)

zeros = '0' * (len(generator) - 1)

crc = mod2_division(data + zeros, generator)
print("CRC Remainder:", crc)

codeword = data + crc
print("Transmitted Codeword:", codeword)

position = int(input("Enter error position (0 for no error): "))

received = list(codeword)

if position != 0 and 1 <= position <= len(codeword):
    index = position - 1
    received[index] = '1' if received[index] == '0' else '0'

received = ''.join(received)
print("Received Data:", received)

remainder = mod2_division(received, generator)
print("Receiver Remainder:", remainder)

if '1' in remainder:
    print("Error Detected!")
    print("Retransmitting...")

    received = codeword
    print("Retransmitted Data:", received)

    remainder = mod2_division(received, generator)

    if '1' not in remainder:
        print("Error Corrected Successfully!")
else:
    print("No Error Detected!")
