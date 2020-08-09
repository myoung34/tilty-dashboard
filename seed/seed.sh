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
  elif [[ $1 == "66" ]]; then
    echo "brown"
  elif [[ $1 == "77" ]]; then
    echo "yellow"
  elif [[ $1 == "88" ]]; then
    echo "green"
  elif [[ $1 == "99" ]]; then
    echo "gray"
  else
    echo "white"
  fi
}

calc() { awk "BEGIN{print $*}"; }

for i in 11 22 33; do
  # shellcheck disable=SC2034
  for j in {1..2}; do
    # shellcheck disable=SC2046
    _random="$(echo $(date +%s) % 10 | bc)"
    # shellcheck disable=SC2004
    random_temp=$(($_random + 59))
    # shellcheck disable=SC2004
    random_gravity=$(calc $(($_random + 1000 + $i)) / 1000)
    color=$(get_color $i)
    echo "Seeding ${random_gravity}@${random_temp}F for ${color} (00:11:22:33:${i})"
    sqlite3 data/tilt.sqlite "insert into data (gravity, temp, color, mac) values (${random_gravity},${random_temp},'${color}','00:11:22:33:${i}')"
    sleep 1
  done
done
