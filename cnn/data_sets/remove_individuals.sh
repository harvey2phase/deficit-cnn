ls e4/tests_age_80/prob_of_death_at_80/unbiased_train_ind/y5_dead | sort -R | tail -370 | while read file; do

    rm e4/tests_age_80/prob_of_death_at_80/unbiased_train_ind/y5_dead/$file

done
