#/bin/bash

for i in 1 2 3 4 5 
do
  cp input$i input
  ./slam_shuffle.py TEST
done
