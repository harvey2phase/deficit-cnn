ls all_individuals_at_80 | sort -R | tail -1 | while read file; do

    mv all_individuals_at_80/$file training_individuals/


done
