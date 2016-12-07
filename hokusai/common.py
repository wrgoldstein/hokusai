import os
import signal

APP_NAME = os.path.basename(os.getcwd())

HOKUSAI_CONFIG_FILE = os.path.join(os.getcwd(), '.hosukai.yml')

EXIT_SIGNALS = [signal.SIGHUP, signal.SIGINT, signal.SIGQUIT, signal.SIGPIPE, signal.SIGTERM]

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

YAML_HEADER = '---\n'