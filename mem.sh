RAM = free -giga -h -t
LOCAL STORAGE = df -T -BG -l | awk '{total+=$3}END{print total}'