ls e4_age80_90/eval_individuals | sort -R | tail -27 | while read file; do

    mv e4_age80_90/eval_individuals/$file e4_age80_90/train_individuals/

done
