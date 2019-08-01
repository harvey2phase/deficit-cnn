in_dir="e4_age80/cohort1/5y_alive_inds"
out_dir="e4_age80/cohort1/eval_inds"
num_to_move=1000

ls $in_dir | sort -R | tail -$num_to_move | while read file; do

    mv $in_dir/$file $out_dir

done
