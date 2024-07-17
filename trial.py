import subprocess

trial = {
    "peplgp01327.pi.pvt":"px6"
}

# f = open("dbVersionFinal2.txt", "a")



masterData = {
    # "Europe": europe,
    # "PGCS": pgcs,
    # "Global": glob,
    # "LATAM": latam,
    "Trial": trial
}

output = ""
script = r'''
whoami
sqlOutput=$(sqlplus -v | grep -Po "(?<=Version )[^ ]+")
hdbOutput=$(hdbsql -v | grep -Po "(?<=version )[^,]+")
osVersion=$(. /etc/os-release; echo "$PRETTY_NAME")
threads=$(lscpu | sed -n "s/Thread(s) per core:[ \\t]*//p")
cores=$(lscpu | sed -n "s/Core(s) per socket:[ \\t]*//p")
sockets=$(lscpu | sed -n "s/Socket(s):[ \\t]*//p")
cpus=$(lscpu | sed -n "s/CPU(s):[ \\t]*//p" | head -1)
mem=$(awk \'/MemTotal/ {print $2=$2/1024^2}\' /proc/meminfo)
sid=$(whoami)
sid="${sid^^}"
sid=$(echo $sid | sed "s/[ADM]//g")
profile="/sapmnt/${sid}/profile/DEFAULT.PFL"
sysType=$(cat $profile | awk \'/system\/type/ {print $3}\')
ker=$(disp+work | grep -Po "(?<=kernel make variant)[^\\n]+")
patchNumber=$(disp+work | grep -Po "(?<=patch number)[^\\n]+")


if [ -n "$sqlOutput" ] && [ -n "$hdbOutput" ]; then
    db="SQL: ${sqlOutput} and HDB: ${hdbOutput}"
elif [ -n "$sqlOutput" ]; then
    db="Oracle: ${sqlOutput}"
elif [ -n "$hdbOutput" ]; then
    db="HDB: ${hdbOutput}"
else
    db="N/A"
fi

echo $sid,$(hostname),$db,$sysType,$osVersion,$threads,$cores,$sockets,$cpus,$mem,$ker,$patchNumber
'''
for sector, sectorData in masterData.items():
    # f.write("Sector: " + sector + "\n\n")
    for host, user in sectorData.items():
        try:
            sqlCommand = """pbrun -u {}adm -h {} /bin/sh <<"ENDPBRUN"
            script='{}'
            echo -e "$script" > finder.sh
            bash finder.sh | tee ress.txt
ENDPBRUN""".format(user.lower(), host.lower(), script )
            output = subprocess.check_output(sqlCommand, shell=True)
            print(output)
        except:
            print("Shit")


# f.close()
