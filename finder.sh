sqlOutput=$(sqlplus -v 2> /dev/null | grep -Po "(?<=Version )[^ ]+")
hdbOutput=$(hdbsql -v 2> /dev/null | grep -Po "(?<=version )[^,]+")
instances=$(startsap -c 2>&1 | grep -oP "Instance \K\w+$")
osVersion=$(. /etc/os-release; echo "$PRETTY_NAME" 2>&1)
threads=$(lscpu 2>&1 | sed -n "s/Thread(s) per core:[ \t]*//p")
cores=$(lscpu 2>&1 | sed -n "s/Core(s) per socket:[ \t]*//p")
sockets=$(lscpu 2>&1 | sed -n "s/Socket(s):[ \t]*//p")
cpus=$(lscpu 2>&1 | sed -n "s/CPU(s):[ \t]*//p" | head -1)
ramInfo=$(free --giga -h -t 2>&1)
mainRam=$(echo "$ramInfo" | awk -v key="Mem:" '$1 == key {print $2}' 2>&1)
swapRam=$(echo "$ramInfo" | awk -v key="Swap:" '$1 == key {print $2}' 2>&1)
totalRam=$(echo "$ramInfo" | awk -v key="Total:" '$1 == key {print $2}' 2>&1)
storage=$(df -T -BG -l 2>&1 | awk '{total+=$3}END{print total}')
sid=$(whoami 2>&1)
sid="${sid^^}"
sid=${sid::-3}
profile="/sapmnt/${sid}/profile/DEFAULT.PFL"
sysType=$(cat $profile 2> /dev/null | awk "/system\/type/ {print \$3}")
ker=$(disp+work 2> /dev/null | awk "/kernel make variant/ {print \$4}")
patchNumber=$(disp+work 2> /dev/null | awk "/patch number/ {print \$3}")

if [ -n "$sqlOutput" ] && [ -n "$hdbOutput" ]; then
    db="SQL: ${sqlOutput} and HDB: ${hdbOutput}"
elif [ -n "$sqlOutput" ]; then
    db="Oracle: ${sqlOutput}"
elif [ -n "$hdbOutput" ]; then
    db="HDB: ${hdbOutput}"
else
    db="N/A"
fi

echo $sid,$(hostname),$sysType,$osVersion,$db,$threads,$cores,$sockets,$cpus,$mainRam,$swapRam,$totalRam,$instances,$storage,$ker,$patchNumber
