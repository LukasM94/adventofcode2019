for i in 1 2 3 4 5
do
	cp input$i input
  ./space_stoichiometry.py > out
  OUT=$(tail --lines=1 out)
  echo $OUT
done
