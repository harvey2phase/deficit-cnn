cnn_data/
in_dir="e4_age80/200_annk/cohort1/5y_dead"
in_dir="e4_age80/100_annk/5y_dead"
out_dir="e4_age80/100_annk/cohort1/5y_unbiased_eval_ind"
num_to_move=415

ls $in_dir | sort -R | tail -$num_to_move | while read file; do

    mv $in_dir/$file $out_dir

done
