import subprocess

users = ["QE9adm","U38adm","U58adm","U63adm","UE2adm","UE2adm","UE2adm","UE2adm","UE2adm","UE2adm","UE2adm","UE2adm","UE2adm","UE2adm","UE2adm","UE2adm","UX3adm","UX3adm","UX3adm","UX3adm","UX3adm","UX3adm","UX3adm"]
hostnames = ["pepldr03698.pi.pvt","peplgp01300.pi.pvt","peplap07439.pi.pvt","peplgp01299.pi.pvt","peplap07448.pi.pvt","peplap07449.pi.pvt","peplap07450.pi.pvt","peplap07457.pi.pvt","peplap07456.pi.pvt","peplap07458.pi.pvt","peplap07474.pi.pvt","peplap07473.pi.pvt","peplap07485.pi.pvt","peplap07484.pi.pvt","peplap07489.pi.pvt","peplap07488.pi.pvt","pepldr03123.pi.pvt","peplap09079.pi.pvt","peplap09078.pi.pvt","peplap09142.pi.pvt","peplap09141.pi.pvt","peplap09140.pi.pvt","peplap09139.pi.pvt"]
outputs = []

f = open("output.txt", "a")

for i,user in enumerate(users):
    output = subprocess.check_output(f'pbrun -u {user.lower()} -h {hostnames[i]} bash -c "cat /etc/os-release"', shell=True)
    f.write(f'{user},{hostnames[i]},{output}\n')

f.close()