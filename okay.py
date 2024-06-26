import subprocess

europe = {
    "D21": "peplap07883.pi.pvt",
    "D37": "pepldr03037.pi.pvt",
    "D57": "peplap07410.pi.pvt",
    "D67": "peplap09067.pi.pvt",
    "DX5": "peplgp01254.pi.pvt",
    "DC7": "peplap09066.pi.pvt",
    "Q21": "peplap07967.pi.pvt",
    "Q37": "pepldr03113.pi.pvt",
    "Q57": "peplap07428.pi.pvt",
    "Q67": "peplap09224.pi.pvt",
    "QX5": "peplgp01255.pi.pvt",
    "QX5": "peplap09584.pi.pvt",
    "QC7": "peplap09230.pi.pvt",
    "S21": "peplap08701.pi.pvt",
    "S37": "pepldr02966.pi.pvt",
    "S57": "peplap07491.pi.pvt",
    "S67": "peplap08704.pi.pvt",
    "SX6": "peplgp01273.pi.pvt",
    "SC7": "PEPLAP08703.pi.pvt",
    "U16": "peplap07963.pi.pvt",
    "U16": "peplap07968.pi.pvt",
    "U32": "pepldr03117.pi.pvt",
    "U52": "peplap07896.pi.pvt",
    "U62": "peplap09459.pi.pvt",
    "U62": "peplap09458.pi.pvt",
    "U62": "peplap09489.pi.pvt",
    "U62": "peplap09488.pi.pvt",
    "UX6": "peplgp01316.pi.pvt",
    "UX6": "t01lap03580.pi.pvt",
    "UX6": "peplap09587.pi.pvt",
    "UC2": "peplap09172.pi.pvt",
    "UC2": "peplap09173.pi.pvt",
    "UC2": "peplap09202.pi.pvt",
    "UC2": "peplap09185.pi.pvt",
}

latam = {
    "D38": "peplgp01262.pi.pvt",
    "D58": "peplap07318.pi.pvt",
    "D63": "peplgp01263.pi.pvt",
    "DE2": "peplap07413.pi.pvt",
    "DX8": "pepldr03056.pi.pvt",
    "Q38": "peplgp01268.pi.pvt",
    "Q58": "peplap07393.pi.pvt",
    "Q63": "peplgp01269.pi.pvt",
    "QE2": "peplap07882.pi.pvt",
    "QE8": "peplgp01301.pi.pvt",
    "QX8": "pepldr03057.pi.pvt",
    "QX8": "peplap10213.pi.pvt",
    "QX8": "peplap10212.pi.pvt",
    "S38": "pepldr02930.pi.pvt",
    "S58": "t01lap01755.pi.pvt",
    "S68": "t01lgp00536.pi.pvt",
    "SE2": "peplap07524.pi.pvt",
    "SX8": "pepldr03055.pi.pvt",
    "QE9": "pepldr03698.pi.pvt",
    "U38": "peplgp01300.pi.pvt",
    "U58": "peplap07439.pi.pvt",
    "U63": "peplgp01299.pi.pvt",
    "UE2": "peplap07448.pi.pvt",
    "UE2": "peplap07449.pi.pvt",
    "UE2": "peplap07450.pi.pvt",
    "UE2": "peplap07457.pi.pvt",
    "UE2": "peplap07456.pi.pvt",
    "UE2": "peplap07458.pi.pvt",
    "UE2": "peplap07474.pi.pvt",
    "UE2": "peplap07473.pi.pvt",
    "UE2": "peplap07485.pi.pvt",
    "UE2": "peplap07484.pi.pvt",
    "UE2": "peplap07489.pi.pvt",
    "UE2": "peplap07488.pi.pvt",
    "UX3": "pepldr03123.pi.pvt",
    "UX3": "peplap09079.pi.pvt",
    "UX3": "peplap09078.pi.pvt",
    "UX3": "peplap09142.pi.pvt",
    "UX3": "peplap09141.pi.pvt",
    "UX3": "peplap09140.pi.pvt",
    "UX3": "peplap09139.pi.pvt",
}

pgcs = {
    "D22":"pepldr03103.pi.pvt",
"D35":"pepldr03100.pi.pvt",
"D55":"peplap09405.pi.pvt",
"DM2":"PEPLAP08585.pi.pvt",
"DS2":"PEPLDR02690.pi.pvt",
"DS2":"PEPLDZ00345.pi.pvt",
"DXA":"pepldr03116.pi.pvt",
"S17":"pepldr03058.pi.pvt",
"U17":"peplap08641.pi.pvt",
"U17":"peplap08640.pi.pvt",
"U17":"pepldr03375.pi.pvt",
"U35":"peplap08639.pi.pvt",
"U35":"PEPLAP08637.pi.pvt",
"U35":"pepldr03364.pi.pvt",
"U55":"peplap08591.pi.pvt",
"U55":"peplap08590.pi.pvt",
"US7":"PEPLDZ00346.pi.pvt",
"US7":"PEPLAP05958.pi.pvt",
"US7":"PEPLAP05962.pi.pvt",
"US7":"PEPLAP05959.pi.pvt",
"US7":"PEPLAP05960.pi.pvt",
"US7":"PEPLDR02738.pi.pvt",
"US7":"PEPLDR02733.pi.pvt",
"US7":"PEPLAP05957.pi.pvt",
"UM7":"PEPLAP08611.pi.pvt",
"UM7":"peplap08636.pi.pvt",
"UM7":"PEPLAP08583.pi.pvt",
"UM7":"PEPLAP08582.pi.pvt",
"UX7":"peplap09595.pi.pvt",
"UX7":"peplap09594.pi.pvt",
"UX7":"peplap09592.pi.pvt",
"UX7":"peplap09591.pi.pvt",
"UX7":"pepldr03379.pi.pvt",
"UX7":"pepldr03380.pi.pvt",
"UX7":"peplap09598.pi.pvt",
"S22":"pepldr03061.pi.pvt",
"S3A":"pepldr03060.pi.pvt",
"SM7":"PEPLAP08477.pi.pvt",
"SS7":"PEPLDR02766.pi.pvt",
"SS7":"PEPLDZ00352.pi.pvt",
"SXA":"pepldr03114.pi.pvt",
"Q22":"PEPLDR03104.pi.pvt",
"Q3A":"pepldr03101.pi.pvt",
"Q5A":"peplap09406.pi.pvt",
"QM2":"peplap08584.pi.pvt",
"QS2":"PEPLDZ00353.pi.pvt",
"QS2":"PEPLDR02795.pi.pvt",
"QXA":"PEPLGP01241.pi.pvt",
"T17":"pepldr03062.pi.pvt"
}

glob = {
    "D24":"pepldr03048.pi.pvt",
"D25":"peplgp01280.pi.pvt",
"D36":"peplgp01305.pi.pvt",
"D39":"pepldr03034.pi.pvt",
"D56":"peplap07437.pi.pvt",
"D56":"pepldh00120.pi.pvt",
"D59":"peplap07857.pi.pvt",
"D61":"pepldh00148.pi.pvt",
"D61":"peplap07533.pi.pvt",
"D71":"pepldr02979.pi.pvt",
"DC1":"pepldh00148.pi.pvt",
"DC1":"peplap09441.pi.pvt",
"DL1":"pepldz00640.pi.pvt",
"DX2":"peplgp01277.pi.pvt",
"DX9":"pepldr03047.pi.pvt",
"S20":"peplgp01270.pi.pvt",
"S61":"peplap09490.pi.pvt",
"SC1":"pepldh00148.pi.pvt",
"SC1":"peplap09442.pi.pvt",
"U19":"peplgp01244.pi.pvt",
"U20":"peplgp01279.pi.pvt",
"U31":"pepldr03385.pi.pvt",
"U39":"peplgp01243.pi.pvt",
"U51":"peplap07933.pi.pvt",
"U59":"peplap07928.pi.pvt",
"U61":"peplap09465.pi.pvt",
"U71":"pepldr03377.pi.pvt",
"UC1":"peplap09465.pi.pvt",
"UL1":"pepldz00642.pi.pvt",
"Ux2":"peplap09476.pi.pvt",
"Ux2":"peplap09475.pi.pvt",
"Ux2":"peplap09515.pi.pvt",
"Ux2":"peplap09481.pi.pvt",
"Ux2":"peplgp01276.pi.pvt",
"UX9":"peplap09068.pi.pvt",
"UX9":"peplap09069.pi.pvt",
"UX9":"peplap09100.pi.pvt",
"UX9":"peplap09074.pi.pvt",
"UX9":"pepldr03121.pi.pvt",
"S65":"pepldr03672.corp.pep.pvt",
"S70":"peplgp01309.corp.pep.pvt",
"SX0":"peplgp01308.corp.pep.pvt",
"DX0":"peplgp01312.pi.pvt",
"S10":"peplgp01313.corp.pep.pvt",
"S35":"peplgp01257.pi.pvt",
"S61":"pepldr03673.corp.pep.pvt",
"D10":"peplgp01315.corp.pep.pvt",
"D30":"peplgp01274.pi.pvt",
"G6S":"peplgp01283.corp.pep.pvt",
"G70":"peplgp01311.pi.pvt",
"DH0":"peplap07920.pi.pvt",
"SH0":"peplap07880.pi.pvt",
"GC7":"t01lap03296.pi.pvt",
"D5H":"peplap10263.corp.pep.pvt",
"S5H":"t01lap03868.pi.pvt",
"G60":"t01lap03299.pi.pvt"
}


f = open("dbVersionFinal.txt", "a")

stats = {
    'oracle': 0,
    'hana': 0,
    'issue': 0,
    'total': 0
}

masterData = {
    "Europe" : europe,
    "PGCS": pgcs,
    "Global": glob,
    "LATAM": latam
}
for sector, sectorData in masterData.items():
    stats = {
        'oracle': 0,
        'hana': 0,
        'issue': 0,
        'total': 0
    }
    ann = 0
    f.write("Sector: " + sector + "\n\n")
    for user,host in sectorData.items():
        ann = ann + 1
        print(user, host)
        try:
            sqlCommand = '''pbrun -u {}adm -h {} SHELL <<"ENDPBRUN"
sqlplus -v | grep -Po "(?<=Version )[^ ]+"
ENDPBRUN'''.format(user.lower(), host.lower())
            output = subprocess.check_output(sqlCommand, shell=True)
            output = output.split("\n")[1]
            f.write(user + "," + host +"," + output + "\n")
            stats['oracle'] = stats['oracle'] + 1
        except:
            try: 
                output = subprocess.check_output("pbrun -u {}adm -h {} bash -c '{}'".format(user.lower(), host.lower(), 'hdbsql -v | grep -Po "(?<=version )[^,]+"'), shell=True)
                stats['hana'] = stats['hana'] + 1
            except:
                output = "Error Connecting to the Server\n"
                stats['issue'] = stats['issue'] + 1
            finally:
                f.write(user + "," + host +"," + output)
        finally:
            stats['total'] = stats['total'] + 1
    print(ann)
    f.write("\n\n")
    f.write("Oracle," + str(stats['oracle']) + "\n")
    f.write("Hana," + str(stats['hana']) + "\n")
    f.write("Issue," + str(stats['issue']) + "\n")
    f.write("Total," + str(stats['total']) + "\n")
    f.write("\n\n")
    


f.close()
