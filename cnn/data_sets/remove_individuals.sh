ls e5/tests_age_80/5y_unbiased_train_ind/dead | sort -R | tail -3840 | while read file; do

    rm e5/tests_age_80/5y_unbiased_train_ind/dead/$file

done
