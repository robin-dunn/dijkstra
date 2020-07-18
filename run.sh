# Example usage: ./run.sh 314185938 1320557460

is_python_installed=
python_command="python3"

# Check if python is installed
check_python=$(python3 -V 2>&1)
if [[ $check_python == *"Python 3"* ]] ; then
  is_python_installed=true
  python_command="python3"
fi

check_python=$(python -V 2>&1)
if [[ $check_python == *"Python 3"* ]] ; then
  is_python_installed=true
  python_command="python"
fi

check_python=$(py3 -V 2>&1)
if [[ $check_python == *"Python 3"* ]] ; then
  is_python_installed=true
  python_command="py3"
fi

check_python=$(py -V 2>&1)
if [[ $check_python == *"Python 3"* ]] ; then
  is_python_installed=true
  python_command="py"
fi

if [ -z "$is_python_installed" ] ; then
  echo "This script requires python v3, but it looks like it's not installed on this machine."
  echo "Please download and install python v3 from https://www.python.org/downloads/ and try running the script again." 
  exit 1;
fi

# Prepare start and end node parameters
start_node_id=$1
end_node_id=$2

is_integer() {
  if [[ $1 =~ ^[0-9]+$ ]] ; then
    true
  else
    false
  fi
  return
}

# Check the provided node IDs are integers
errors=0
if ! is_integer "$start_node_id" ; then
  echo "Error: first argument must be the start node ID (integer)."
  (( errors++ ))
fi

if ! is_integer "$start_node_id" ; then
  echo "Error: second argument must be the end node ID (integer)."
  (( errors++ ))
fi

if (( errors > 0 )); then
  exit 1;
fi

# Run python script to calculate shortest distance between nodes
$python_command Main.py $start_node_id $end_node_id
