dir="e4_age80/100_annk/cohort1/5y_unbiased_train_ind/dead"
num_to_move=147

ls $dir | sort -R | tail -$num_to_move | while read file; do

    rm $dir/$file

done
