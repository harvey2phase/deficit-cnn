ls e5/prob_of_death_at_80/train_individuals | sort -R | tail -10000 | while read file; do

    mv e5/prob_of_death_at_80/train_individuals/$file e5/prob_of_death_at_80/eval_individuals/

done
