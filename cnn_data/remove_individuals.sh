dir="e5/tests_age_80/prob_of_death_at_80/5y_unbiased_eval_ind/dead"
num_to_move=1890

ls $dir | sort -R | tail -num_to_move | while read file; do

    rm $dir/$file

done
