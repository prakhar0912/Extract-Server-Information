declare -A pirtDevSBX
pirtDevSBX=(["pepldr03048.pi.pvt"]="D24" ["peplgp01280.pi.pvt"]="D25" ["peplgp01305.pi.pvt"]="D36" ["pepldr03034.pi.pvt"]="D39" ["peplap07437.pi.pvt"]="D56" ["pepldh00120.pi.pvt"]="D56" ["peplap07857.pi.pvt"]="D59" ["pepldh00148.pi.pvt"]="D61" ["peplap07533.pi.pvt"]="D61" ["pepldr02979.pi.pvt"]="D71" ["pepldh00148.pi.pvt"]="DC1" ["peplap09441.pi.pvt"]="DC1" ["pepldz00640.pi.pvt"]="DL1" ["peplgp01277.pi.pvt"]="DX2" ["pepldr03047.pi.pvt"]="DX9" ["peplgp01270.pi.pvt"]="S20" ["peplap09490.pi.pvt"]="S61" ["pepldh00148.pi.pvt"]="SC1" ["peplap09442.pi.pvt"]="SC1" ["peplgp01244.pi.pvt"]="U19" ["peplgp01279.pi.pvt"]="U20" ["pepldr03385.pi.pvt"]="U31" ["peplgp01243.pi.pvt"]="U39" ["peplap07933.pi.pvt"]="U51" ["peplap07928.pi.pvt"]="U59" ["peplap09465.pi.pvt"]="U61" ["pepldr03377.pi.pvt"]="U71" ["peplap09465.pi.pvt"]="UC1" ["pepldz00642.pi.pvt"]="UL1" ["peplap09476.pi.pvt"]="Ux2" ["peplap09475.pi.pvt"]="Ux2" ["peplap09515.pi.pvt"]="Ux2" ["peplap09481.pi.pvt"]="Ux2" ["peplgp01276.pi.pvt"]="Ux2" ["peplap09068.pi.pvt"]="UX9" ["peplap09069.pi.pvt"]="UX9" ["peplap09100.pi.pvt"]="UX9" ["peplap09074.pi.pvt"]="UX9" ["pepldr03121.pi.pvt"]="UX9" ["pepldr03672.corp.pep.pvt"]="S65" ["peplgp01309.corp.pep.pvt"]="S70" ["peplgp01308.corp.pep.pvt"]="SX0" ["peplgp01312"]="DX0" ["peplgp01313.corp.pep.pvt"]="S10" ["peplgp01257.pi.pvt"]="S35" ["pepldr03673.corp.pep.pvt"]="S61" ["peplgp01315.corp.pep.pvt"]="D10" ["peplgp01274"]="D30" ["peplgp01283.corp.pep.pvt"]="G6S" ["peplgp01311"]="G70" ["peplap07920.pi.pvt"]="DH0" ["peplap07880.pi.pvt"]="SH0" ["t01lap03296.pi.pvt"]="GC7" ["peplap10263.corp.pep.pvt"]="D5H" ["t01lap03868.pi.pvt"]="S5H" ["t01lap03299.pi.pvt"]="G60")


echo "SID,Hostname,DB Version,System Type,OS Version,Threads,Cores,Sockets,CPUs,Memory,Kernel Version,Patch Number"


for host in "${!pirtDevSBX[@]}"
do
    pbrun -u "${pirtDevSBX["$host"],,}"adm -h $host /bin/sh << "ENDSHELL"
        script='
sqlOutput=$(sqlplus -v | grep -Po "(?<=Version )[^ ]+")
hdbOutput=$(hdbsql -v | grep -Po "(?<=version )[^,]+")
osVersion=$(. /etc/os-release; echo "$PRETTY_NAME")
threads=$(lscpu | sed -n "s/Threads per core:[ \t]*//p")
cores=$(lscpu | sed -n 's/Cores per socket:[ \t]*//p')
sockets=$(lscpu | sed -n 's/Sockets:[ \t]*//p')
cpus=$(lscpu | sed -n 's/CPUs:[ \t]*//p' | head -1)
mem=$(awk '/MemTotal/ {print $2=$2/1024^2}' /proc/meminfo)
sid=$(whoami)
sid="${sid^^}"
sid=${sid::-3}
profile="/sapmnt/${sid}/profile/DEFAULT.PFL"
sysType=$(cat $profile | awk '/system\/type/ {print $3}')
ker=$(disp+work | grep -Po "(?<=kernel make variant)[^\n]+")
patchNumber=$(disp+work | grep -Po "(?<=patch number)[^\n]+")


if [ -n "$sqlOutput" ] && [ -n "$hdbOutput" ]; then
    db="SQL: ${sqlOutput} and HDB: ${hdbOutput}"
elif [ -n "$sqlOutput" ]; then
    db="Oracle: ${sqlOutput}"
elif [ -n "$hdbOutput" ]; then
    db="HDB: ${hdbOutput}"
else
    db="N/A"
fi

echo $sid,$(hostname),$db,$sysType,$osVersion,$threads,$cores,$sockets,$cpus,$mem,$ker,$patchNumber'
        echo -e "$script" > startScript.sh
        bash startScript.sh
ENDSHELL
done