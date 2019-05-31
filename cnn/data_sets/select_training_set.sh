ls eval_individuals | sort -R | tail -124 | while read file; do

    mv eval_individuals/$file training_individuals/


done
