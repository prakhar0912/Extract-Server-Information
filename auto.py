import subprocess

users = ["U16adm","U16adm","U32adm","U52adm","U62adm","U62adm","U62adm","U62adm","UX6adm","UX6adm","UX6adm","D21adm","D37adm","D57adm","D67adm","DX5adm","S21adm","S37adm","S57adm","S67adm","SX6adm","Q21adm","Q37adm","Q57adm","Q67adm","QX5adm","QX5adm","QC7adm","UC2adm","UC2adm","UC2adm","UC2adm","DC7adm","SC7adm"]
hostnames = ["peplap07963.pi.pvt","peplap07968.pi.pvt","pepldr03117.pi.pvt","peplap07896.pi.pvt","peplap09459.pi.pvt","peplap09458.pi.pvt","peplap09489.pi.pvt","peplap09488.pi.pvt","peplgp01316.pi.pvt","t01lap03580.pi.pvt","peplap09587.pi.pvt","peplap07883.pi.pvt","pepldr03037.pi.pvt","peplap07410.pi.pvt","peplap09067.pi.pvt","peplgp01254.pi.pvt","peplap08701.pi.pvt","pepldr02966.pi.pvt","peplap07491.pi.pvt","peplap08704.pi.pvt","peplgp01273.pi.pvt","peplap07967.pi.pvt","pepldr03113.pi.pvt","peplap07428.pi.pvt","peplap09224.pi.pvt","peplgp01255.pi.pvt","peplap09584.pi.pvt","peplap09230.pi.pvt","peplap09172.pi.pvt","peplap09173.pi.pvt","peplap09202.pi.pvt","peplap09185.pi.pvt","peplap09066.pi.pvt","peplap08703.pi.pvt"]
outputs = []

f = open("finalOutput.txt", "a")

for i,user in enumerate(users):
    try: 
        output = subprocess.check_output("pbrun -u {} -h {} bash -c '{}'".format(user.lower(), hostnames[i], '. /etc/os-release; echo "$PRETTY_NAME"'), shell=True)
    except:
        output = "Error in connecting to the server\n"
    f.write(user+"," + hostnames[i]+"," + output)

f.close()