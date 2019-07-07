ls e4_age80_90/90s | sort -R | tail -527 | while read file; do

    mv e4_age80_90/90s/$file e4_age80_90/eval_individuals/

done
