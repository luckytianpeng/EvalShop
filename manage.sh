#!/usr/bin/env bash
# manage.sh: command-line utility fro administrative tasks.
#_______________________________________________________________________________

PROGRAM=${0##*/}
VERSION="$PROGRAM version 1.0.0"


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

runserver
    codegeex_rest_api_server --path CodeGeeX_local_home_path

E.g.:
    ./manage.sh install codegeex_rest_api_server --path ../CodeGeeX
    ./manage.sh runserver codegeex_rest_api_server --path ../CodeGeeX
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

    if (( 0 == $? )); then
cat << EOF
Success.

Add key(s) to '$path/tests/codegeex_rest_api_server_api_keys.json' before \
performing '$PROGRAM runserver codegeex_rest_api_server'.
EOF
    else
        echo "Install codegeex_rest_api_server to '$1' failed!" 1>&2
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

function install {
    case $1 in
        'codegeex_rest_api_server' )
            shift
            install_codegeex_rest_api_server $@
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
    case $1 in
        '--path' )
            [ -z $2 ] && {
                echo "$PROGRAM runserver codegeex_rest_api_server: " \
                    "path is empty!" 1>&2
                exit 1
            }

            if [ -d $2 ]; then
                local path=$( realpath $2 )
                # Run codegeex_rest_api_server
                "$path/scripts/codegeex_rest_api_server_launcher.sh" 0
            else
                echo "$PROGRAM runserver codegeex_rest_api_server: " \
                    "path '$2' does NOT exists" 1>&2
                exit 1
            fi
        ;;
        * )
            echo "$PROGRAM runserver codegeex_rest_api_server: " \
                "missing --path" 1>&2
            exit 1
        ;;
    esac
}

function runserver {
    case $1 in
        'codegeex_rest_api_server' )
            shift
            run_codegeex_rest_api_server $@
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
