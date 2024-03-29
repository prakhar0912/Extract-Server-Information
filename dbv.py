import subprocess

europeData = {
"D21":"peplap07883.pi.pvt",
"D37":"pepldr03037.pi.pvt",
"D57":"peplap07410.pi.pvt",
"D67":"peplap09067.pi.pvt",
"DX5":"peplgp01254.pi.pvt",
"DC7":"peplap09066.pi.pvt",
"Q21":"peplap07967.pi.pvt",
"Q37":"pepldr03113.pi.pvt",
"Q57":"peplap07428.pi.pvt",
"Q67":"peplap09224.pi.pvt",
"QX5":"peplgp01255.pi.pvt",
"QX5":"peplap09584.pi.pvt",
"QC7":"peplap09230.pi.pvt",
"S21":"peplap08701.pi.pvt",
"S37":"pepldr02966.pi.pvt",
"S57":"peplap07491.pi.pvt",
"S67":"peplap08704.pi.pvt",
"SX6":"peplgp01273.pi.pvt",
"SC7":"PEPLAP08703.pi.pvt",
"U16":"peplap07963.pi.pvt",
"U16":"peplap07968.pi.pvt",
"U32":"pepldr03117.pi.pvt",
"U52":"peplap07896.pi.pvt",
"U62":"peplap09459.pi.pvt",
"U62":"peplap09458.pi.pvt",
"U62":"peplap09489.pi.pvt",
"U62":"peplap09488.pi.pvt",
"UX6":"peplgp01316.pi.pvt",
"UX6":"t01lap03580.pi.pvt",
"UX6":"peplap09587.pi.pvt",
"UC2":"peplap09172.pi.pvt",
"UC2":"peplap09173.pi.pvt",
"UC2":"peplap09202.pi.pvt",
"UC2":"peplap09185.pi.pvt"
}


f = open("dbVersionFinal.txt", "a")

stats = {
    'oracle': 0,
    'hana': 0,
    'issue': 0,
    'total': 0
}

masterData = {
    "Europe" : europeData
}
for sector, sectorData in masterData.items():
    stats = {
        'oracle': 0,
        'hana': 0,
        'issue': 0,
        'total': 0
    }

    f.write("Sector: " + sector + "\n\n")
    for user,host in sectorData.items():
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
    f.write("Oracle," + stats['oracle'] + "\n")
    f.write("Hana," + stats['hana'] + "\n")
    f.write("Issue," + stats['issue'] + "\n")
    f.write("Total," + stats['total'] + "\n")
    f.write("\n\n")
    

f.close()