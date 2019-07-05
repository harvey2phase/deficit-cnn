ls e5/tests_age_80/prob_of_death_at_80/5y_unbiased_eval_ind/dead | sort -R | tail -1890 | while read file; do

    rm e5/tests_age_80/prob_of_death_at_80/5y_unbiased_eval_ind/dead/$file

done
