#!/usr/bin/env bash

for i in 1 2 3 4; do
  echo "======================================================="
  echo "=====================start=test$i======================="
  cp input$i input
  ./many_world_interpreter.py
  echo "=======================end=test$i======================="
  echo "======================================================="
done
