import subprocess

users = ["U16","U16","U32","U52","U62","U62","U62","U62","UX6","UX6","UX6","D21","D37","D57","D67","DX5","S21","S37","S57","S67","SX6","Q21","Q37","Q57","Q67","QX5","QX5","QC7","UC2","UC2","UC2","UC2","DC7","SC7"]
hostnames = ["peplap07963.pi.pvt","peplap07968.pi.pvt","pepldr03117.pi.pvt","peplap07896.pi.pvt","peplap09459.pi.pvt","peplap09458.pi.pvt","peplap09489.pi.pvt","peplap09488.pi.pvt","peplgp01316.pi.pvt","t01lap03580.pi.pvt","peplap09587.pi.pvt","peplap07883.pi.pvt","pepldr03037.pi.pvt","peplap07410.pi.pvt","peplap09067.pi.pvt","peplgp01254.pi.pvt","peplap08701.pi.pvt","pepldr02966.pi.pvt","peplap07491.pi.pvt","peplap08704.pi.pvt","peplgp01273.pi.pvt","peplap07967.pi.pvt","pepldr03113.pi.pvt","peplap07428.pi.pvt","peplap09224.pi.pvt","peplgp01255.pi.pvt","peplap09584.pi.pvt","peplap09230.pi.pvt","peplap09172.pi.pvt","peplap09173.pi.pvt","peplap09202.pi.pvt","peplap09185.pi.pvt","peplap09066.pi.pvt","peplap08703.pi.pvt"]
outputs = []

f = open("dbVersion.txt", "a")

for i,user in enumerate(users):
    try: 
        output = subprocess.check_output('pbrun -u {}adm -h {} SHELL -c "{}"'.format(user.lower(), hostnames[i], "sqlplus -v | grep -Po '(?<=Version )[^ ]+'"), shell=True)
    except:
        try: 
            output = subprocess.check_output('pbrun -u {}adm -h {} SHELL -c "{}"'.format(user.lower(), hostnames[i], "hdbsql -v | grep -Po '(?<=version )[^,]+'"), shell=True)
        except:
            output = "Error Connecting to the Server"

    f.write(user+"," + hostnames[i]+"," + output)

f.close()