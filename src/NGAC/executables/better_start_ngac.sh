# Starts the NGAC servers
# Check what os we are running on, there are 3 options: Debian, Arch, Mac
if [ -f /etc/debian_version ]; then
    # We are running on Debian
    echo "Starting NGAC server on Debian"
    ./linux/ngac_server --jsonresp &
    ./linux/cme &
    ./linux/pep_server &
    exit
    elif [ -f /etc/arch-release ]; then
    # We are running on Arch
    echo "Starting NGAC server on Arch"
    ./arch/ngac_server --jsonresp &
    ./arch/cme &
    ./arch/pep_server &
    exit
    elif [ -f /etc/os-release ]; then
    # We are running on Mac
    echo "Starting NGAC server on Mac"
    ./mac/ngac_server --jsonresp &
    ./mac/cme &
    ./mac/pep_server &
    exit
else
    # Unknown.
    echo "Unknown OS"
fi
