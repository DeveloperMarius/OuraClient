import math

packets = [
    "6110632a29001a24001e03000000000000cb6111642a2900230b00000400002800000200004612c02a2900350eab0d8a0c2f10380e910d6a0d4612182d2900370eae0d940c3310390e960d6c0d6112492d29001460635610e9ffffff12393577e04612702f2900340ea80d840c3210360e940d680d4612c8312900310ea80d8a0c2e10340e900d670d461220342900390eac0d990c2e103b0e940d6a0d5b108935290002b54c02bb0608060004d70a5b118a35290004cf00cf0035080000d6000000",
    "5b0f8b352900058640000007005c001f00461278362900330eab0d900c2d10380e930d6a0d4612d0382900370eac0d8e0c3210420e960d6b0d4612283b2900320eac0d900c3110390e910d6b0d4612803d2900370eaf0d8c0c3010390e970d6c0d4612d83f2900380eab0d910c2f10390e960d6a0d461230422900380eab0d910c2f103c0e960d6b0d4612884429003e0ead0d8c0c2f103d0e960d6b0d6112b94429001454635510e8ffffff0d3934aa174612e0462900350eaa0d940c2b103b0e970d690d",
    "461238492900340ea90d900c2f10370e930d680d4612904b2900330ea80d910c2810360e910d670d4612e84d2900340ea70d900c2910390e910d660d461240502900310ea60d8e0c2510330e900d650d461298522900330ea80d8c0c2910340e930d660d4612f0542900370ea80d890c2c103b0e930d660d461248572900320ea70d890c2e103c0e8e0d660d4612a0592900310ea50d8e0c2a10380e8e0d640d430d935b2900626174743a203130304310f75b29006571733b3064303332353033",
    "430df85b2900657173323b303230316109f95b290024645510016112fa5b290009dfc8d506bfe42e003d920400806112fb5b290028000000000000000000000000006112fc5b290028010000000000000000000000004612fd5b2900310ea20d850c2a10340e8e0d620d6112295c29001447635510e9ffffff033933dfad4612505e29002e0ea30d880c2710350e8e0d610d6906515e2900370e4612a86029002d0ea00d8d0c26102e0e950d5f0d4612006329002e0e9f0d860c2910360e8d0d5d0d",
    "461258652900280e9f0d860c2510320e8c0d5d0d4612b06729002a0e9b0d840c23102c0e8b0d5a0d4612086a29002a0e9b0d820c2610290e8d0d5a0d4612606c2900240e9d0d820c22102a0e8f0d5c0d4612b86e2900300e9c0d840c27102c0e8b0d5a0d4612107129002a0e9a0d7c0c20102d0e8d0d590d4612687329002b0e9a0d800c25102e0e870d580d611299732900143b635510e8fffffffe383310ae4612c0752900280e9b0d7e0c1e10290e8a0d590d461218782900240e9d0d820c22102b0e890d5b0d",
    "4612707a2900290e9d0d7e0c21102e0e8b0d5c0d4612c87c2900270e9e0d7c0c22102a0e8a0d5b0d4612207f2900240e9c0d820c1e10310e8b0d5b0d461278812900260e9e0d7e0c2310260e8d0d5d0d4612d0832900270ea10d850c26102a0e8e0d5f0d461228862900280ea20d840c2310290e8c0d5f0d461280882900280ea10d840c21102a0e8b0d5e0d4612d88a2900220e9f0d7c0c1c10240e890d5d0d6112098b2900142e635410e9fffffff93832448d4612308d2900200e9d0d760c2610240e880d5c0d",
    "4612888f2900220e9f0d800c2210240e8b0d5e0d4612e0912900240e9f0d790c2510280e8a0d5e0d461238942900220e9f0d7a0c21102c0e8a0d5e0d461290962900250e9e0d7a0c2610240e880d5e0d4612e8982900220e9f0d7c0c2310230e8c0d5d0d4612409b29001e0e9f0d800c2110280e850d5d0d4612989d2900250ea10d800c2710260e8f0d600d4612f09f2900250e9e0d800c2310270e890d5c0d461248a229001e0e970d7d0c2410250e7f0d560d611279a229001422635410e8ffffffef38317551",
    "4612a0a42900230e960d750c1f10240e830d540d6906a1a42900310e4612f8a62900260e9d0d850c2910290e880d5b0d461250a92900240e9e0d890c1e10300e8a0d5d0d4612a8ab29002c0ea00d7c0c26102d0e8d0d5e0d461200ae2900280ea00d790c2110270e920d5e0d461258b02900280ea00d850c26102c0e8c0d5f0d4612b0b22900270e9f0d800c2410280e8c0d5e0d461208b52900270e9f0d820c26102a0e8f0d5d0d461260b72900280e9f0d7e0c23102b0e8a0d5d0d",
    "4612b8b92900260ea00d850c2310310e8e0d5e0d6112e9b929001415635410e8ffffffea3830a6bf461210bc2900250e9f0d7d0c2b102a0e8a0d5e0d461268be2900200e9e0d740c2010240e850d5b0d4612c0c02900260e9f0d810c24102c0e880d5d0d461218c32900290ea10d8d0c23102e0e8b0d5e0d461270c529002d0ea20d7d0c20102c0e8e0d610d4612c8c72900280ea20d840c2710280e8e0d600d461220ca2900280ea20d840c27102b0e8c0d600d461278cc2900280ea20d820c2810310e8e0d600d",
    "4612d0ce2900270ea30d800c21102f0e8c0d610d461228d12900290ea30d850c25102c0e8f0d610d611259d129001409635310e8ffffffe0382fd9cf461280d32900310ea30d860c26102f0e910d620d4612d8d529002a0ea30d860c2210310e8d0d600d461230d82900270ea20d7e0c2210290e8c0d600d461288da2900210e9e0d780c2010230e860d5c0d4612e0dc2900210e9d0d7d0c2210270e860d5c0d461238df29002c0ea30d840c2a10310e8e0d600d461290e12900330ea20d7d0c2410290e8e0d600d",
    "4612e8e32900220ea00d810c26102a0e8a0d5e0d461240e62900260ea30d860c25102e0e8b0d600d430d33e82900626174743a20313030431097e829006571733b3032303132333031430d98e82900657173323b33303031610999e82900246453100146129ae82900260ea10d820c26102f0e8e0d5f0d6112b0e8290009dac0d506edf32e004f8b0400806112b1e8290028000000000000000000000000006112b2e8290028010000000000000000000000006112c9e8290014fc625310e9ffffffdb382f0edf",
    "4612f0ea2900270ea10d840c25102b0e8f0d5f0d6906f1ea29002a0e461248ed2900250e9f0d7e0c23102b0e8c0d5e0d4612a0ef2900260ea00d810c2d102f0e8c0d5e0d4612f8f129002c0ea10d890c27102e0e8c0d5f0d461250f42900280ea20d860c27102d0e8e0d600d4612a8f62900280ea20d7e0c26102a0e870d600d461200f92900250ea10d860c2b10280e900d5f0d461258fb29002c0ea20d7e0c2b102d0e8e0d600d4612b0fd2900290ea10d820c2a102b0e8a0d600d",
    "461208002a00260ea20d850c2510320e8a0d600d611239002a0014f0625210e9ffffffd1382e4314461260022a002a0ea40d7e0c27102b0e8c0d620d4612b8042a00280ea60d880c2910310e8c0d640d461210072a002c0ea60d840c27102f0e8b0d640d461268092a002c0ea60d810c26102e0e8f0d630d4612c00b2a00280ea40d820c23102d0e8d0d620d4612180e2a00260ea20d860c2510260e8b0d600d461270102a00260ea20d800c2210310e8c0d610d4612c8122a002a0ea20d820c27102c0e8a0d610d",
    "461220152a00270e9d0d7d0c2310280e8d0d5c0d461278172a00250e9e0d7e0c2a10290e860d5d0d6112a9172a0014e3625210e9ffffffcc382d77574612d0192a00240ea10d820c26102b0e8e0d600d4612281c2a002a0ea60d850c24102d0e900d630d4612801e2a002b0ea40d890c25102f0e8c0d620d4612d8202a00290ea40d820c2710280e910d630d461230232a002b0ea20d7c0c2910280e8e0d610d461288252a00240ea20d800c2b10300e890d600d4612e0272a00230ea10d820c2410290e8d0d5f0d",
    "4612382a2a00280ea20d810c2710300e8e0d610d4612902c2a002b0ea40d7e0c28102b0e8e0d630d4612e82e2a00270ea20d820c28102c0e8d0d600d6112192f2a0014d7625210e8ffffffc2382ca98c461240312a002d0ea30d860c28102f0e8e0d610d690641312a002a0e461298332a00270ea10d850c2510280e8d0d5f0d4612f0352a00250ea00d7e0c2610330e8b0d5f0d461248382a00290e9e0d7d0c2910280e890d5d0d4612a03a2a00220e9e0d850c2b10290e890d5d0d",
    "4612f83c2a00250e9f0d7d0c24102b0e870d5e0d4612503f2a00240ea00d7e0c2510270e8a0d5f0d4612a8412a00230ea20d7d0c24102f0e8b0d600d461200442a002a0ea20d7d0c2710270e8c0d610d461258462a00270ea30d840c2710300e8a0d610d611289462a0014c7625210e9ffffffbd382bddb74612b0482a00290ea60d840c2a10320e8d0d640d4612084b2a00280ea60d810c2810270e8e0d620d4612604d2a002f0ea70d840c2210290e8b0d640d4612b84f2a002c0ea70d840c28102d0e8e0d650d",
    "461210522a00290ea50d820c2b102d0e8f0d640d461268542a00260ea30d840c2a102f0e8b0d620d4612c0562a00290ea30d850c2610270e8f0d610d461218592a00290ea30d7d0c26102b0e880d610d4612705b2a00290ea10d810c2910260e8b0d5f0d4612c85d2a002a0ea20d7a0c29102c0e8c0d600d6112f95d2a0014bb625110e9ffffffb3382b1117461220602a00270ea00d840c2910280e8b0d5e0d461278622a00250e9f0d800c2410290e8f0d5c0d4612d0642a00230e9e0d810c2910230e8a0d5d0d",
    "461228672a00220e9d0d820c2710340e870d5c0d461280692a002e0e9e0d840c2910380e8a0d5d0d4612d86b2a00290ea10d880c2e102f0e8a0d5f0d4612306e2a00260e9d0d810c2610290e880d5b0d461288702a00260e9e0d810c2610280e880d5d0d4612e0722a00290ea10d7e0c2810260e8d0d5e0d430dd3742a00626174743a20313030431037752a006571733b3036303330303030430d38752a00657173323b30303030610939752a00246451100146123a752a00250ea00d7d0c2910270e8b0d5f0d",
    "611269752a0014ae625110e8ffffffae382a444861126a752a000963c1d5065cf32e00378b04008061126b752a00280000000000000000000000000061126c752a002801000000000000000000000000461290772a00250e9f0d7d0c2610260e8b0d5d0d690691772a00290e4612e8792a00260ea00d7e0c2310250e890d5e0d4612407c2a00240e9e0d810c2610250e8c0d5d0d4612987e2a00250ea00d840c2c10290e8d0d5e0d4612f0802a00250ea00d7c0c2a10290e890d5d0d",
    "461248832a00260e9f0d7d0c2610290e870d5e0d4612a0852a00250ea30d760c27102c0e880d610d4612f8872a002b0ea20d820c2710290e890d5f0d4612508a2a002a0ea20d820c2710380e8a0d5f0d4612a88c2a002a0ea30d810c2b102b0e930d600d6112d98c2a0014a2625110e9ffffffa9382979964612008f2a00240ea30d7e0c2410270e8c0d610d461258912a00260ea40d7a0c27102c0e8a0d620d4612b0932a00220ea20d7e0c2b10280e8b0d5f0d461208962a00220ea20d800c27102a0e8c0d5f0d",
    "461260982a00260ea60d880c2d102c0e8b0d630d4612b89a2a002e0ea50d810c2a102e0e8c0d620d4612109d2a00250ea40d810c2c102f0e8a0d630d4612689f2a00230ea20d820c2a102f0e860d600d4612c0a12a00240ea20d820c29102c0e8a0d600d461218a42a00250ea30d7e0c29102a0e8b0d610d611249a42a001495625010e9ffffff9f3828ada7461270a62a00260ea20d7a0c2510260e8b0d600d4612c8a82a00290ea50d7e0c2710310e8e0d630d461220ab2a00250ea20d7d0c2a102c0e8c0d610d",
    "461278ad2a00230ea30d800c26102c0e890d600d4612d0af2a00230ea50d7d0c24102e0e8c0d610d461228b22a00220ea30d800c26102c0e8c0d610d461280b42a00240ea40d810c30102b0e8b0d620d4612d8b62a00240ea60d820c23102b0e8d0d640d461230b92a00260ea50d850c29102f0e910d640d461288bb2a00240ea20d880c2910260e8c0d610d6112b9bb2a001489625010e9ffffff9a3827e2834612e0bd2a00280ea10d7d0c2410290e880d600d6906e1bd2a00260e",
    "461238c02a00250ea30d820c2910270e8b0d610d461290c22a00270ea20d7c0c29102c0e8c0d610d4612e8c42a00290ea20d7d0c2b102b0e8c0d600d461240c72a00270ea30d800c29102d0e8c0d600d461298c92a00250ea20d7e0c2810310e8c0d610d4612f0cb2a00210ea20d790c25102b0e8d0d5f0d461248ce2a00280ea50d7a0c2910280e8d0d620d4612a0d02a002a0ea40d800c26102d0e900d630d4612f8d22a002a0ea70d890c2a102d0e900d640d611229d32a00147c625010e9ffffff9038271730",
    "461250d52a00270ea50d7d0c2a102d0e8c0d630d4612a8d72a002d0ea10d7d0c2510290e8c0d610d461200da2a00250ea40d810c2410290e8e0d620d461258dc2a00240ea60d840c2510300e890d630d4612b0de2a00220ea10d790c25102b0e880d5f0d461208e12a00230ea20d7e0c2b102b0e8a0d5f0d461260e32a00250ea00d7a0c2510270e8b0d5e0d4612b8e52a00260ea10d7e0c26102b0e8d0d5e0d461210e82a00240ea40d820c2b102c0e890d610d461268ea2a002b0ea40d7d0c2a102a0e8d0d610d",
    "611299ea2a001470624f10e9ffffff8b38264b334612c0ec2a00260ea60d810c27102c0e8f0d640d461218ef2a00280ea50d800c2710290e8e0d630d461270f12a00230ea50d840c25102e0e8e0d620d4612c8f32a00290ea60d810c26102a0e8d0d640d461220f62a00280ea50d810c2310290e900d620d461278f82a00210ea20d850c2610290e890d600d4612d0fa2a00220ea40d7e0c2610290e8b0d610d461228fd2a00260ea50d880c2a102c0e8a0d620d461280ff2a002a0ea50d820c2a10290e920d620d",
    "430d73012b00626174743a203130304310d7012b006571733b3235303330323031",
    "1108ff00394501000300"
]

events = 0
for packet in packets:
    packet = bytes.fromhex(packet)
    print(f'Processing packet with {len(packet)} bytes and {len(packet)/20} Blocks')
    for i in range(0, len(packet), 20):
        block = packet[i:i + 20]
        print(f'Processing block {i} with {len(block)} bytes')
        events += 1
        # Parse block...
        if block[0] == 17:
            print('Last packaged, stopping read...')

print(f'Events found: {events}')

packet = bytes.fromhex(packets[-1])
packet_length = packet[1]
events_received = packet[2] & 0xff
sleep_analysis_progress = packet[3] & 0xff if packet_length >= 2 else -1
bytes_left = int.from_bytes(packet[4:8], 'little') if packet_length >= 6 else -1
print(f'Events Received: {events_received}')
print(f'Sleep Analysis Progress: {sleep_analysis_progress}')
print(f'Bytes Left: {bytes_left}')
