from opentrons import protocol_api

metadata = {
    'protocolName': 'Test Protocol',
    'apiLevel': '2.11'
}


# 代表的な試薬条件で3サンプル分注する
def run(protocol: protocol_api.ProtocolContext):
    # ここの配置とlabware名は修正する
    well_plate_384 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 5)
    tube_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 8)
    tip_rack = protocol.load_labware('opentrons_96_tiprack_20ul', 10)

    #ピペットは p20
    pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tip_rack])
    pipette.starting_tip = tip_rack['A1']

    pipette.pick_up_tip(tip_rack['A1'])


    # Mg(80mM)を2ulずつ3ヶ所に分注
    for i in range(3):
        pipette.transfer(2, well_plate_384['A1'], tube_rack[f'A{i+1}'], new_tip='never')
        
    pipette.drop_tip()

    # K(800mM)を2ulずつ3ヶ所に分注
    for i in range(3):
        pipette.transfer(2, well_plate_384['A2'], tube_rack[f'A{i+1}'], new_tip='always')

    # K(800mM)を2ulずつ3ヶ所に分注
    for i in range(3):
        pipette.transfer(2, well_plate_384['A3'], tube_rack[f'A{i+1}'], new_tip='always')

    # アミノ酸(6mM)を5ulずつ3ヶ所に分注
    for i in range(3):
        pipette.transfer(5, well_plate_384['A3'], tube_rack[f'A{i+1}'], new_tip='always')

    # スペルミジン(10mM)を2ulずつ3ヶ所に分注
    for i in range(3):
        pipette.transfer(2, well_plate_384['A4'], tube_rack[f'A{i+1}'], new_tip='always')

    # NTP(15mM)を2ulずつ3ヶ所に分注
    for i in range(3):
        pipette.transfer(2, well_plate_384['A5'], tube_rack[f'A{i+1}'], new_tip='always')

    # 3-PGA(300mM)を2ulずつ3ヶ所に分注
    for i in range(3):
        pipette.transfer(2, well_plate_384['A6'], tube_rack[f'A{i+1}'], new_tip='always')