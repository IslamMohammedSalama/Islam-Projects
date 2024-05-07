#!/bin/bash
# read -N 1 -d " " -t 5 -sp "kill you : " name
# echo "Hello $1 $2 $3 ; numbers of args = $# `pwd ; echo islam ` . $name "
read -p "enter a number : " number # 20
read -p "enter a number : " numberr # 10
echo $((number + numberr)) # 30
echo $((number - numberr)) # 10
echo $((number * numberr)) # 200
echo $((number / numberr)) # 2
echo $((number ** numberr)) # 
echo $((number % numberr)) # 2 

echo `expr $number + $numberr`
echo `expr $number - $numberr`
echo `expr $number \* $numberr`
echo `expr $number / $numberr`
echo `expr $number % $numberr`

read -p "enter your name" name

echo `expr length  $name`