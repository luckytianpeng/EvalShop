#!/usr/bin/env bash
# manage.sh: command-line utility fro administrative tasks.
#_______________________________________________________________________________

PROGRAM=${0##*/}
VERSION="$PROGRAM version 1.6.0"


function display_usage {
cat << EOF
usage: $PROGRAM [--version] [--help]
                <command> [<args>]
EOF
}

function display_help {
    display_usage

cat << EOF

These are common manage commands used in various situations:

install
    codegeex_rest_api_server --path CodeGeeX_local_home_path
    humaneval_x_rest_api_server (sudo)
    codereval_rest_api_server

runserver
    codegeex_rest_api_server
    humaneval_x_rest_api_server
    codereval_rest_api_server

E.g.:
    ./manage.sh install codegeex_rest_api_server --path ../CodeGeeX
    ./manage.sh runserver codegeex_rest_api_server

    ./manage.sh install humaneval_x_rest_api_server
    ./manage.sh runserver humaneval_x_rest_api_server

    ./manage.sh install codereval_rest_api_server
    ./manage.sh runserver codereval_rest_api_server
EOF
}

function _install_codegeex_rest_api_server {
    local path=$( realpath $1 )
    cp -rf codegeex_rest_api_server/scripts "$path"
    # Key user's config files (.json)
    cp -n codegeex_rest_api_server/tests/*.json "$path/tests/"
    cp -f codegeex_rest_api_server/tests/*.py "$path/tests/"
    chmod +x "$path/scripts/codegeex_rest_api_server_launcher.sh"
    mkdir -p "$path/tests/logging"
    # Write CodeGeeX_home into manage.properties
    local escape_path=$( sed 's/\//\\\//g' <<< "$path" )
    sed -i "s/^[#]*\s*CodeGeeX_home=.*/CodeGeeX_home=$escape_path/" \
        manage.properties

    if (( 0 == $? )); then
cat << EOF
Success.

Add key(s) to '$path/tests/codegeex_rest_api_server_api_keys.json' before \
performing '$PROGRAM runserver codegeex_rest_api_server'.
EOF
    else
cat >&2 << EOF
Failure.

Install codegeex_rest_api_server to '$1' failed!"
EOF
        exit 1
    fi
}

function install_codegeex_rest_api_server {
    case $1 in
        '--path' )
            [ -z $2 ] && {
                echo "$PROGRAM install codegeex_rest_api_server: " \
                    "path is empty!" 1>&2
                exit 1
            }

            if [ -d $2 ]; then
                _install_codegeex_rest_api_server $2
            else
                echo "$PROGRAM install codegeex_rest_api_server: " \
                    "path '$2' does NOT exists" 1>&2
                exit 1
            fi
        ;;
        * )
            echo "$PROGRAM install codegeex_rest_api_server: " \
                "missing --path" 1>&2
            exit 1
        ;;
    esac
}

function _install_dock {
    # Ref:
    #    [The Docker Book](https://dockerbook.com/)

    # Adding prerequisite Ubuntu packages
    sudo apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common
    
    # Adding the Docker GPG key
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    # Adding the Docker APT repository
    sudo add-apt-repository -y \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"

    # Updating APT sources
    sudo apt-get update

    # Installing the Docker packages on Ubuntu
    sudo apt-get install -y docker-ce
}

function _install_gVisor {
    # Install from an apt repository
    # Ref:  
    # - https://gvisor.dev/docs/user_guide/install/

    # First, appropriate dependencies must be installed to allow apt
    # to install packages via https:
    sudo apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg

    # Next, configure the key used to sign archives and the repository:
    curl -fsSL https://gvisor.dev/archive.key | sudo gpg --dearmor -o /usr/share/keyrings/gvisor-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) \
        signed-by=/usr/share/keyrings/gvisor-archive-keyring.gpg] \
        https://storage.googleapis.com/gvisor/releases release main" \
        | sudo tee /etc/apt/sources.list.d/gvisor.list > /dev/null

    # Now the runsc package can be installed:
    sudo apt-get update && sudo apt-get install -y runsc

    # Configuring Docker
    # Ref:  
    # - https://gvisor.dev/docs/user_guide/quick_start/docker/

    # Configure Docker to use runsc by adding a runtime entry to your 
    # Docker configuration:
    sudo runsc install

    # Must restart the Docker daemon after installing the runtime:
    sudo systemctl restart docker
}

function is_codegeex_rest_api_server_installed {
    # Check if CodeGeeX_home exists
    . manage.properties
    if [ -z $CodeGeeX_home ]; then
cat >&2 << EOF
Please install codegeex_rest_api_server.
EOF
        exit 1
    fi
}

function install_humaneval_x_rest_api_server {
    # Check if CodeGeeX_home exists
    is_codegeex_rest_api_server_installed

    # Check if docker installed
    # docker -v &> /dev/null
    sudo docker info &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install humaneval_x_rest_api_server: " \
            "Install dock ..."
        _install_dock
    fi

    sudo docker info &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install humaneval_x_rest_api_server: " \
            "The automatic installation of the dock is failed." \
            "Please install the dock manually - " \
            "https://docs.docker.com/engine/install/" \
            1>&2
        exit $exit_status
    fi

    # Check if gVisor installed
    sudo docker run --runtime=runsc -it ubuntu dmesg &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install humaneval_x_rest_api_server: " \
            "Install gVisor ..."
        _install_gVisor
    fi

    sudo docker run --runtime=runsc -it ubuntu dmesg &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install humaneval_x_rest_api_server: " \
            "The automatic installation of gVisor is failed." \
            "Please install the gVisor manually - " \
            "https://gvisor.dev/docs/user_guide/install/" \
            1>&2
        exit $exit_status
    fi

    # Check if pip is installed
    python3 -m pip --version &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        sudo apt install -y python3-pip
    fi

    python3 -m pip --version &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install humaneval_x_rest_api_server: " \
            "The automatic installation of pip is failed." \
            "Please install python3-pip manually."
        exit $exit_status
    fi

    # Do NOT use Python virtualenv:
    #     sudo python3 humaneval_x_rest_api_server.py
    #     ModuleNotFoundError: No module named 'docker'


    # Install the requirements file for Python
    # Ref:
    #     https://pip.pypa.io/en/stable/cli/pip_freeze/
    #     https://pip.pypa.io/en/stable/cli/pip_install/

    # Docker SDK for Python
    # Ref:
    #     https://docker-py.readthedocs.io/en/stable/

    sudo pip3 show docker &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install humaneval_x_rest_api_server: " \
            "Install the requirements file for Python ..."
        sudo pip3 install -r ./humaneval_x_rest_api_server/requirements.txt
    fi

    # Build docker image (humaneval_x_sandbox)
    sudo docker image inspect humaneval_x_sandbox &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install humaneval_x_rest_api_server: " \
            "Build docker image (humaneval_x_sandbox) ..."
        sudo docker build --tag humaneval_x_sandbox \
            -f ./humaneval_x_rest_api_server/humaneval_x_sandbox/Dockerfile \
            ./humaneval_x_rest_api_server/humaneval_x_sandbox
    fi

    if (( 0 == $? )); then
cat << EOF
Success.
EOF
    else
cat >&2 << EOF
Failure.
EOF
        exit 1
    fi
}

function install_codereval_rest_api_server {
    # Check if docker installed
    sudo docker info &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install codereval_rest_api_server: " \
            "Install dock ..."
        _install_dock
    fi

    sudo docker info &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install codereval_rest_api_server: " \
            "The automatic installation of the dock is failed." \
            "Please install the dock manually - " \
            "https://docs.docker.com/engine/install/" \
            1>&2
        exit $exit_status
    fi

    # Check if gVisor installed
    sudo docker run --runtime=runsc -it ubuntu dmesg &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install codereval_rest_api_server: " \
            "Install gVisor ..."
        _install_gVisor
    fi

    sudo docker run --runtime=runsc -it ubuntu dmesg &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install codereval_rest_api_server: " \
            "The automatic installation of gVisor is failed." \
            "Please install the gVisor manually - " \
            "https://gvisor.dev/docs/user_guide/install/" \
            1>&2
        exit $exit_status
    fi

    # Check if pip is installed
    python3 -m pip --version &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        sudo apt install -y python3-pip
    fi

    python3 -m pip --version &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install codereval_rest_api_server: " \
            "The automatic installation of pip is failed." \
            "Please install python3-pip manually." \
            1>&2
        exit $exit_status
    fi

    # virtualenv:
    echo "$PROGRAM codereval_rest_api_server: " \
        "Install the virtual environment ..."
    sudo apt install -y python3-venv

    sudo pip3 show GitPython &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM codereval_rest_api_server: " \
            "Install the requirements file for Python ..."
        sudo -H pip3 install -r ./codereval_rest_api_server/requirements.txt
    fi

    # Clone and checkout all projects
    echo "$PROGRAM install codereval_rest_api_server: " \
        "Clone and checkout all projects ..."
    python3 ./codereval_rest_api_server/projects_checkout.py
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "Failure." 1>&2
        exit $exit_status
    fi

    # Set up environments
    echo "$PROGRAM install codereval_rest_api_server: " \
        "Set up environments ..."
    python3 ./codereval_rest_api_server/set_up_environments.py
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "Failure." 1>&2
        exit $exit_status
    fi

    # Verify test entry points
    echo "$PROGRAM install codereval_rest_api_server: " \
        "Verify test entry points ..."
    python3 ./codereval_rest_api_server/verify_test_entry_points.py
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "Failure." 1>&2
        exit $exit_status
    fi

    # Build docker image (codereval_sandbox)
    sudo docker image inspect codereval_sandbox &> /dev/null
    local exit_status=$?
    if [ 0 != $exit_status ]; then
        echo "$PROGRAM install codereval_rest_api_server: " \
            "Build docker image (codereval_sandbox) ..."
        sudo docker build --tag codereval_sandbox \
            -f ./codereval_rest_api_server/codereval_sandbox/Dockerfile \
            ./codereval_rest_api_server/codereval_sandbox
    fi

    if (( 0 == $? )); then
cat << EOF
Success.
EOF
    else
cat >&2 << EOF
Failure.
EOF
        exit 1
    fi
}

function install {
    case $1 in
        'codegeex_rest_api_server' )
            shift
            install_codegeex_rest_api_server $@
        ;;
        'humaneval_x_rest_api_server' )
            shift
            install_humaneval_x_rest_api_server $@
            exit $?
        ;;
        'codereval_rest_api_server' )
            shift
            install_codereval_rest_api_server $@
        ;;
        '' )
            echo "$PROGRAM install: missing option" 1>&2
        ;;
        * )
            echo "$PROGRAM install: unknown option: '$1'" 1>&2
            exit 1
        ;;
    esac
}

function run_codegeex_rest_api_server {
    is_codegeex_rest_api_server_installed

    "$CodeGeeX_home/scripts/codegeex_rest_api_server_launcher.sh" 0
}

function run_humaneval_x_rest_api_server {
    is_codegeex_rest_api_server_installed

    sudo python3 ./humaneval_x_rest_api_server/humaneval_x_rest_api_server.py
}

function run_codereval_rest_api_server {
    sudo python3 ./codereval_rest_api_server/codereval_rest_api_server.py
}

function runserver {
    case $1 in
        'codegeex_rest_api_server' )
            shift
            run_codegeex_rest_api_server $@
        ;;
        'humaneval_x_rest_api_server' )
            shift
            run_humaneval_x_rest_api_server $@
        ;;
        'codereval_rest_api_server' )
            shift
            run_codereval_rest_api_server $@
        ;;
        '' )
            echo "$PROGRAM runserver: missing option" 1>&2
        ;;
        * )
            echo "$PROGRAM runserver: unknown option: '$1'" 1>&2
            exit 1
        ;;
    esac
}

#-------------------------------------------------------------------------------

function main {
    local command=$1
    case $command in
        '' | 'help' | '--help' )
            display_help
        ;;
        'version' | '--version' )
            echo $VERSION
        ;;
        'install' )
            shift
            install $@
        ;;
        'runserver' )
            shift
            runserver $@
        ;;
        -* )
            echo "unknown option: $command" 1>&2
            display_usage
            exit 1
        ;;
        * )
            echo "$PROGRAM: '$command' is not a $PROGRAM command. " \
                "See '$PROGRAM --help'." 1>&2
            exit 1
        ;;
    esac
}

main $@
