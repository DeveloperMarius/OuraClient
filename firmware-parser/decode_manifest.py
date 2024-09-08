
with open('../app/resources/assets/ota/firmware_gen2x/2.9.32/firmware_2_9_32.cyacd2', 'r') as file:
    for line in file:
        line = line.rstrip()
        if line.startswith('@APPINFO:'):
            # Application verification information: An application verification information row is of the format:
            # @APPINFO:[__cy_app_verify_start],[__cy_app_verify_length].
            # The start and length data are used by the host program in the Set Application Metadata to the DFU module.
            data = line.split(':')[1].split(',')
            print(f'Appinfo:[__cy_app_verify_start={data[0]}],[__cy_app_verify_length={data[1]}]')
        elif line.startswith('@EIV:'):
            # Encryption initial vector: An encryption initial vector row is of the format @EIV:<bytes>. The data in <bytes>
            # is used by the host program in the Set EIVector to the DFU module
            data = line.split(':')[1]
            print(f'Encryption Initial Vector: {data}')
        elif line.startswith(':'):
            # Header            | Address  | Data
            # 1 character: “:”  | 4 bytes  | N bytes
            print(f'Data: 0x{line[1:9]}: {line[10:]}')
            exit()
        else:
            #  Header: A header row has the structure shown in Table 11.
            # Table 11 cyacd2 header row structure
            # File version | Silicon ID | Silicon revision |Checksum type | App ID | Product ID
            # 1 byte       |  4 bytes   | 1 byte           | 1 byte       | 1 byte | 4 Bytes
            # - File Version: Numbered starting at 1
            # - Silicon ID, Silicon Revision, Product ID: Used to prevent the application from being downloaded to the
            # wrong device
            # - Checksum Type: The method used to verify a DFU packet (see Command/Response Packet Structure).
            # 0 = checksum, 1 = CRC
            # - App ID: See Figure 6. This also controls which portion of the application metadata is updated for this
            # application
            data = bytes.fromhex(line)
            print(len(data))
            print(f'File Version: {hex(data[0])}; Silicon ID: 0x{data[1:5].hex()}, Silicon revision: {hex(data[5])}, Checksum type: {hex(data[6])}, App ID: {hex(data[7])}, Product ID: 0x{data[8:12].hex()}')
