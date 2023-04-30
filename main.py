# A program for checking hash value of windows 11 ISO file

def value_comparing():
    user_data = input("Enter the hash value of the ISO file: ")

    hash_values = {
        'Arabic 64-bit': '393C928718AFE938CAB0C81B657F9513C563AED63528F8C8DDDF87FD23443160',
        'Bulgarian 64-bit': '326CF197DEE443B7DB429356C3F825EB8EA48B2CAB1EED0B22D854F64C192459',
        'Danish 64-bit': 'C29A404614E5B75DD6E3CC1F901942E53036D6E4E0F878123B7D9274673E7BDD',
        'German 64-bit': '2AD545B9091E67BABB25DDBA5EACFED2018B388557D82A1F2002597DC559661B',
        'Greek 64-bit': '6EA4FAEB127A34DEDC1B0FFCDC3CAAA3B6DB5C96AE8791671E4DAAAAF8D55AB0',
        'English International 64-bit': 'F115CD6B31734BC091BC94B964D5AD43984285BF229503481E2F7EF94AB7140E',
        'English 64-bit': '0DF2F173D84D00743DC08ED824FBD174D972929BD84B87FE384ED950F5BDAB22',
        'Spanish 64-bit': '2AC6A7B2DA30937FB435C71945BE2DBB0CD1B6768850CE9FEC61AFF8E727E15A',
        'Spanish (Mexico) 64-bit': '8D67F2EA1B5FC42EF6EE3DA51D61EDDBF8A05EABCF3029AEC76A08F29647B2C1',
        'Estonian 64-bit': '9FDDF91F6EA467B1D37F7E1A762D611DF60C5EC400D55E814B38488FEB659323',
        'Finnish 64-bit': '52F866E8E902E5F3ADC33282283081D378721C5635A1370AA1888CC6F2557931',
        'French Canadian 64-bit': '40DEDFBBD25977D9245A645190C902DEB24FFEF4B4B46B823733189B3F378AB0',
        'French 64-bit': 'DD5082F658887AC012DD5532834E9D2BF4E57829DFC6D2A2F1EC328ECFE91BF2',
        'Hebrew 64-bit': 'ED4342F76B55E2E1B7850110D90058EDDFA4CEAEB8B392BAA363F2FF1BBE539E',
        'Croatian 64-bit': '690AA36215FFBCF883CB7217FD857283EF2B415F8B79D6F9257B6A03ADDFEA14',
        'Hungarian 64-bit': 'FF1CFCCA88A3E514D1381FF3F03FD53F776C32F072F4281D6AAF7EA7835908C1',
        'Italian 64-bit': 'BC36716D566D5ABF1F6551EFE0F8161C3955EDDCB0113680E169CAF23F5A9E14',
        'Japanese 64-bit': '6393559146B2A32F3A33DE430EAF1BC59B61133A12E2580A2F163540AC43E463',
        'Korean 64-bit': '901E3EC44053E0955F96B03A2A3D795F5F086A385E669226124912D85D4677A4',
        'Lithuanian 64-bit': 'EA492CC90CB08CDBF6B73EC6E1EDB0567823029CA4EBDF948DD10AAC8C8F181B',
        'Latvian 64-bit': '14DE9C1D641F963B49F31345C1F9DC702F9D6E8E27957C94E5967692ACAAC970',
        'Norwegian 64-bit': 'C96BAF3E4325456E477488D02E7559A8A281BE0BFA347AE76F5E9411E6C533C7',
        'Dutch 64-bit': 'D3B61F2332D60E5B2FD64D6C499033B18735C6A0A84F445FF0153E6AE43F6CF7',
        'Polish 64-bit': 'D57F431D392743AEC19C5666AE45B3388084880E699E23C4C827946B7DC17760',
        'Brazilian Portuguese 64-bit': 'A73A5362ABAEE00E55B4C5E1C704CDA3AA270E2E2240EF40CE737E0BC5D684EE',
        'Portuguese 64-bit': 'C995F5CA4F60B1021003C8E7CEE9A07D6FAFF95660199E7EE44C833FB1CF0452',
        'Romanian 64-bit': '72C4FEB2EE85C2934490AD7B92C6703353A167739D98804AFD38EA84960FFAFE',
        'Russian 64-bit': '8CEC8785CDBE2FA8D4CE4DA230D332F610D165482EBBBF446E056EE4D4202735',
        'Slovak 64-bit': '7A4877211E16997ED767F588001F8FBE207B7B2C4D183A8E8A45F5E07F885591',
        'Slovenian 64-bit': '8B3B558A222E5237BA0C77971C0DE7BC1EC0570D970E6142F346C148457CF43A',
        'Serbian Latin 64-bit': 'BB27D9A503EDC8EEF0A6A087A83AC258BFD11DAEC9F21F32D750D66BA9279BE8',
        "Swedish 64-bit": "3B5C70D56AC833FD6FA1182E900B42CE891D0ED8A31835EBB23F0406EB78C3B3",
        "Thai 64-bit": "E8E9C5BBEB4BFFE9F8320512B191E7A5F08B7DF302F6D77898F8340EEF577412",
        "Turkish 64-bit": "F23709784575AD33599D4B310B98AB8F1B0D989840F5DEB74E38BBBD5369ACEE",
        "Ukrainian 64-bit": "B5DDC3628E191F30CDD801AC27C0D630E7E7FDB2B50ACDBB50E1A2000962DEB2",
        "Chinese Simplified 64-bit": "3ED12FC9EE8A84C040637AE51ABF2795CEA6A7291319B1C456A4DF1CBC1D625D",
        "Chinese Traditional 64-bit": "F622D3654FAC2D391AA8658C1A31907B130A82F2E60F528086D2A4752BC00046"

    }

    for keys in hash_values.keys():
        if hash_values[keys] == user_data:
            print('Your ISO file is not corrupted\n')
            print('Information about your ISO is given below:')
            print(f'{keys}:{hash_values[keys]}')
            print(
                f'for more info go to https://www.microsoft.com/en-us/software-download/windows11?subid1=20221002-0458'
                f'-37f7-b0ff-dd8c61cb46ce\n')
            break

    else:
        print('Your ISO file is corrupted\n')


while True:
    value_comparing()
    answer = input('Do you want to quit? Type "y" to quit or type "n" to continue\n')

    if answer == 'y':
        break
    elif answer == 'n':
        continue
