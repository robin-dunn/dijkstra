# Example usage: ./run.sh {startNodeId} {endNodeId}
# E.g. ./run.sh 314185938 1320557460

is_python_installed=
python_command="python3"
python_aliases=("python3" "python" "py3" "py")

for a in "${python_aliases[@]}"
do
  # Try to run the python get version command to see which, 
  # if any, is the correct python alias
  check_python=$($a -V 2>&1)
  if [[ $check_python == *"Python 3"* ]] ; then
    is_python_installed=true
    python_command="$a"
  fi
done

if [ -z "$is_python_installed" ] ; then
  echo "This script requires Python v3, but it looks like it's not installed on this machine."
  echo "Please download and install Python v3 (https://www.python.org/downloads/) and try running the script again." 
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
