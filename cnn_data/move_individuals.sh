in_dir="e4_age80/100_annk/cohort2/train_ind"
out_dir="e4_age80/100_annk/cohort2/eval_ind"
num_to_move=1000

ls $in_dir | sort -R | tail -$num_to_move | while read file; do

    mv $in_dir/$file $out_dir/

done
