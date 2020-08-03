#!/bin/bash
function get_color {
  if [[ $1 == "11" ]]; then
    echo "black"
  elif [[ $1 == "22" ]]; then
    echo "pink"
  elif [[ $1 == "33" ]]; then
    echo "red"
  elif [[ $1 == "44" ]]; then
    echo "blue"
  elif [[ $1 == "55" ]]; then
    echo "purple"
  else
    echo "white"
  fi
}

for i in 11 22 33 44 55; do
  # shellcheck disable=SC2046
  _random="$(echo $(date +%s) % 10 | bc)"
  # shellcheck disable=SC2004
  random_temp=$(($_random + 59))
  # shellcheck disable=SC2004
  random_gravity=$(($_random + 1000 + $i))
  color=$(get_color $i)
  sqlite3 data/tilt.sqlite "insert into data (gravity, temp, color, mac) values (${random_gravity},${random_temp},'${color}','00:11:22:33:${i}')"
  sleep 1
done
