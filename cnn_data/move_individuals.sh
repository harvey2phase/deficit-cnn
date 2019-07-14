in_dir="e4_age80/100_annk/cohort1/train_ind/5y_dead"
out_dir="e4_age80/100_annk/cohort1/5y_unbiased_train_ind"
num_to_move=878

ls $in_dir | sort -R | tail -$num_to_move | while read file; do

    cp $in_dir/$file $out_dir/

done
